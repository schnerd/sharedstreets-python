"""
Aggregates hourly weekly binned linear references into a daily

This script takes event tiles with SharedStreetsWeeklyBinnedLinearReferences events,
which normally have 24 values for each bin (one for each hour in the day), and aggregates
those 24 values into a single value for the whole day, writing the resulting
tiles in SharedStreetsBinnedLinearReferences format to the output directory

See the the various event type protobuf schemas here:
https://github.com/sharedstreets/sharedstreets-ref-system/blob/master/proto/linear_references.proto
"""

import json
import re
import sys
from os import listdir
from os.path import isfile, join, isdir, basename
from sharedstreets.linear_references import load_binned_events
from sharedstreets.linear_references_pb2 import SharedStreetsWeeklyBinnedLinearReferences, SharedStreetsBinnedLinearReferences, DataBin
from sharedstreets.tile import get_tile, make_geojson
import google.protobuf.message
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintEncoder

if len(sys.argv) < 3:
    sys.exit("Usage: python events-aggregate.py [input_path] [output_path]")

input_path = sys.argv[1]
output_path = sys.argv[2]

if not isdir(output_path):
    sys.exit("%s is not a directory" % output_path)


def read_objects(position, content, DataClass):
    while position < len(content):
        message_length, new_position = _DecodeVarint32(content, position)
        position = new_position
        message = content[position:position+message_length]
        position += message_length

        try:
            object = DataClass()
            object.ParseFromString(message)
        except google.protobuf.message.DecodeError:
            # Empty tile? Shrug.
            continue
        else:
            yield object


def process_tile(file_path):
    # Parse zoom, x, y, out of file name
    groups = re.search("(\d+)-(\d+)-(\d+).events.pbf", file_path).groups()
    zoom = int(groups[0])
    x = int(groups[1])
    y = int(groups[2])

    print("Processing tile %d-%d-%d" % (zoom, x, y))

    # Write into the adjacent events_agg folder
    file_path_out = join(output_path, basename(file_path))

    with open(file_path_out, 'wb') as file_out:
        with open(file_path, 'rb') as file:
            for o in read_objects(0, file.read(), SharedStreetsWeeklyBinnedLinearReferences):
                # Create a new linear reference with the same settings
                out = SharedStreetsBinnedLinearReferences()
                out.referenceId = o.referenceId
                out.scaledCounts = o.scaledCounts
                out.referenceLength = o.referenceLength
                out.numberOfBins = o.numberOfBins
                out.binPosition.extend(o.binPosition)

                # But aggregate the event data
                for b in o.binnedPeriodicData:
                    out.bins.extend([agg_bin(b)])

                # Write the data
                pbf_data = out.SerializeToString()
                size_of_data = len(pbf_data)
                _VarintEncoder()(file_out.write, size_of_data, True)
                file_out.write(pbf_data)

# Aggregates all the time periods in a bin into a single bin with a single time period


def agg_bin(b):
    counts = {}
    values = {}
    for v in b.bins:
        i = 0
        while i < len(v.dataType):
            d = v.dataType[i]
            if d not in counts:
                counts[d] = 0
                values[d] = 0
            counts[d] += v.count[i]
            values[d] += v.value[i]
            i += 1

    new_bin = DataBin()
    for dataType, count in counts.items():
        new_bin.dataType.append(dataType)
        new_bin.count.append(count)
        new_bin.value.append(values[dataType])

    return new_bin


def is_pbf_file(path):
    return isfile(path) and path.endswith('.events.pbf')


if input_path.endswith('.pbf'):
    input_files = [input_path]
else:
    input_files = [join(input_path, f) for f in listdir(input_path)]

input_files = [f for f in input_files if is_pbf_file(f)]

if len(input_files) < 1:
    sys.exit("No files found in input path")

for i, file_path in enumerate(input_files):
    print("Processing file (%d of %d)" % (i + 1, len(input_files)))
    process_tile(file_path)
