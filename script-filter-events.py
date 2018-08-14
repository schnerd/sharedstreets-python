"""
Filters irrelevant events ouf of binner linear reference tiles

The SharedStreets matcher generates tiles given input GPS traces, however
those tiles sometimes also contain the "gpsSpeed" events instead of just the
"pickup" and "dropoff" events we care about. This can bloat the tiles ~10-20x
in size.

In order to make tiles easier to work with, we can use this script to filter
out any events that aren't pickup or dropoff, and write the output tiles.

See the SharedStreetsWeeklyBinnedLinearReferences protobuf schema here:
https://github.com/sharedstreets/sharedstreets-ref-system/blob/master/proto/linear_references.proto
"""

import json
import re
from os import listdir
from os.path import isfile, join
from sharedstreets.linear_references import load_binned_events
from sharedstreets.linear_references_pb2 import SharedStreetsWeeklyBinnedLinearReferences
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

# Took 7 minutes and 26 seconds just to convert the biggest tile
# But it became 4.17% of the size!

def processTile(file_name):
    # Parse zoom, x, y, out of file name
    groups = re.search("(\d+)-(\d+)-(\d+).events.pbf", file_name).groups()
    zoom = int(groups[0])
    x = int(groups[1])
    y = int(groups[2])

    print("Processing tile %d-%d-%d" % (zoom, x, y))
    file_name_out = file_name.replace('/events/', '/events_filtered/')

    with open(file_name_out, 'wb') as file_out:
        with open(file_name, 'rb') as file:
            for o in read_objects(0, file.read(), SharedStreetsWeeklyBinnedLinearReferences):
                filter_bins(o)
                if len(o.binPosition) < 1:
                    continue
                pbf_data = o.SerializeToString()
                size_of_data = len(pbf_data)
                _VarintEncoder()(file_out.write, size_of_data, True)
                file_out.write(pbf_data)

def filter_bins(o):
    i = 0
    while i < len(o.binnedPeriodicData):
        out = filter_periods(o.binnedPeriodicData[i])
        if out is None:
            del o.binPosition[i]
            del o.binnedPeriodicData[i]
        else:
            i += 1

def filter_periods(o):
    i = 0
    while i < len(o.bins):
        out = filter_values(o.bins[i])
        if out is None:
            del o.bins[i]
            del o.periodOffset[i]
        else:
            i += 1
    if len(o.bins) < 1:
        return None
    return o

def filter_values(o):
    i = 0
    while i < len(o.dataType):
        if o.dataType[i] == 'pickup' or o.dataType[i] == 'dropoff':
            i += 1
        else:
            del o.dataType[i]
            del o.count[i]
            del o.value[i]
    if len(o.dataType) < 1:
        return None
    return o


output = []

# You can read all tiles from a specific directory if you want
input_path = '/Users/dschnurr/Downloads/ss-dc-tiles/output_tiles/2017-10-30/events'
input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]
input_files.sort()

# However that is *a lot* of data, for now we'll just pick a few tiles downtown
# input_files = [
    #'12-1170-1565.events.pbf',
    #'12-1170-1566.events.pbf',
    #'12-1170-1567.events.pbf',
    #'12-1171-1565.events.pbf',
    #'12-1171-1566.events.pbf'
    #'12-1171-1567.events.pbf',
    #'12-1172-1565.events.pbf'
    #'12-1172-1566.events.pbf',
    #'12-1172-1567.events.pbf',
# ]

for i, filename in enumerate(input_files):
    if filename.startswith('.'):
        continue
    print("Processing file (%d of %d)" % (i + 1, len(input_files)))
    processTile(join(input_path, filename))

