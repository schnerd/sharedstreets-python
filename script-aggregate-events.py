"""
Aggregates hourly weekly binned linear references into a daily

This script takes weekly binned linear reference tiles, which normally have
24 values for each bin (one for each hour in the day), and aggregates
those 24 values into a single value for the whole day, outputing the resulting
tiles into a file on disk.

See the SharedStreetsWeeklyBinnedLinearReferences protobuf schema here:
https://github.com/sharedstreets/sharedstreets-ref-system/blob/master/proto/linear_references.proto
"""

import json
import re
from os import listdir
from os.path import isfile, join
from sharedstreets.linear_references import load_binned_events
from sharedstreets.linear_references_pb2 import SharedStreetsWeeklyBinnedLinearReferences, SharedStreetsBinnedLinearReferences, DataBin
from sharedstreets.tile import get_tile, make_geojson
import google.protobuf.message
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintEncoder


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

def processTile(file_name):
    # Parse zoom, x, y, out of file name
    groups = re.search("(\d+)-(\d+)-(\d+).events.pbf", file_name).groups()
    zoom = int(groups[0])
    x = int(groups[1])
    y = int(groups[2])

    print("Processing tile %d-%d-%d" % (zoom, x, y))

    # Write into the adjacent events_agg folder
    file_name_out = file_name.replace('events_filtered', 'events_agg')

    with open(file_name_out, 'wb') as file_out:
        with open(file_name, 'rb') as file:
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


# You can read all tiles from a specific directory if you want
input_path = '/Users/dschnurr/Downloads/ss-dc-tiles/output_tiles/2017-10-30/events_filtered'
input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

# However that is *a lot* of data, for now we'll just pick a few tiles downtown
input_files = [
    #'12-1170-1565.events.pbf',
    #'12-1170-1566.events.pbf',
    #'12-1170-1567.events.pbf',
    #'12-1171-1565.events.pbf',
    '12-1171-1566.events.pbf'
    #'12-1171-1567.events.pbf',
    #'12-1172-1565.events.pbf'
    #'12-1172-1566.events.pbf',
    #'12-1172-1567.events.pbf',
]

for i, filename in enumerate(input_files):
    if filename.startswith('.'):
        continue
    print("Processing file (%d of %d)" % (i + 1, len(input_files)))
    processTile(join(input_path, filename))

