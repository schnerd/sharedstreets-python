"""
Generates a events geojson file from one or more SharedStreets
binned linear reference tiles. This geojson file is suitable for
visualizing in a tool like kepler.

See the SharedStreetsWeeklyBinnedLinearReferences protobuf schema here:
https://github.com/sharedstreets/sharedstreets-ref-system/blob/master/proto/linear_references.proto
"""

import json
import re
import sys
from os import listdir
from os.path import isfile, join
from sharedstreets.linear_references import load_binned_events
from sharedstreets.tile import get_tile, make_geojson
from shapely.geometry import LineString

if len(sys.argv) < 3:
    sys.exit("Usage: python events-to-geojson.py [input_path] [output_file]")

input_path = sys.argv[1]
output_file = sys.argv[2]


def create_line_string(geom, is_forward):
    ls = LineString([(geom.lonlats[i], geom.lonlats[i + 1])
                     for i in range(0, len(geom.lonlats), 2)])
    offset = .000045
    if is_forward:
        ls = ls.parallel_offset(offset, 'right')
    else:
        ls = ls.parallel_offset(offset, 'left')
    return ls


def process_tile(out, file_name):
    # Parse zoom, x, y, out of file name
    groups = re.search("(\d+)-(\d+)-(\d+).events.pbf", file_name).groups()
    zoom = int(groups[0])
    x = int(groups[1])
    y = int(groups[2])

    print("Processing tile %d-%d-%d" % (zoom, x, y))

    with open(file_name, 'rb') as file:
        # Event tiles were build using planet-180430 build, use that as the tile tempalte URI
        tile = get_tile(
            zoom, x, y, data_url_template='https://tiles.sharedstreets.io/osm/planet-180430/{z}-{x}-{y}.{layer}.6.pbf')

        # Create hashmap of referenceId to geometry (for both forward/backware direction)
        geomsByForwardRef = dict([(g.forwardReferenceId, g)
                                  for g in tile.geometries.values()])
        geomsByBackwardRef = dict([(g.backReferenceId, g)
                                   for g in tile.geometries.values()])
        print("Forward refs %d" % len(geomsByForwardRef.keys()))
        print("Backward refs %d" % len(geomsByBackwardRef.keys()))

        # Parse the event pbf files into a list of binned events (one for each reference id)
        fileContent = file.read()
        print("Loading binned events")
        binned_events = load_binned_events(fileContent)
        print("Loaded %d binned events" % len(binned_events))

        # Loop over each reference
        forward_count = 0
        backward_count = 0
        no_match_count = 0
        for event in binned_events:
            geom = None
            forward = None
            bin_length = event.get_bin_length()
            reference_length = event.reference_length

            # Get the geometry associated with this reference, and whether its forward or backward
            if event.reference_id in geomsByForwardRef:
                geom = geomsByForwardRef.get(event.reference_id)
                forward = True
                forward_count += 1
            elif event.reference_id in geomsByBackwardRef:
                geom = geomsByBackwardRef.get(event.reference_id)
                forward = False
                backward_count += 1
            else:
                no_match_count = no_match_count + 1
                print("Could not find geom for ref %s" % event.reference_id)
                continue

            line = create_line_string(geom, forward)

            # data indexed as a multi-dimentional array {dataType}{binPosition}
            for event_type, datum in event.data.items():
                for bin_pos, bin_obj in datum.items():
                    total_ct = 0
                    for period_offset, obs in bin_obj.items():
                        total_ct += obs.get('count')

                    # Get point along line for the given bin
                    dist = bin_length * int(bin_pos)
                    dist_norm = dist / reference_length
                    pt = line.interpolate(dist_norm, normalized=True)

                    # Add a geojson feature to output for this point
                    out.append({
                        'type': 'Feature',
                        'properties': {
                            'referenceId': event.reference_id,
                            'eventType': event_type,
                            'eventCount': total_ct,
                            'tile': "%d-%d-%d" % (zoom, x, y)
                        },
                        'geometry': {
                            'type': 'Point',
                            'coordinates': [pt.x, pt.y]
                        }
                    })
        print("Forward matches: %d" % forward_count)
        print("Backward matches: %d" % backward_count)
        print("%d of %d events had no reference" %
              (no_match_count, len(binned_events)))


output = []


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
    process_tile(output, file_path)

print("Length %d" % len(output))
geojson = dict(type='FeatureCollection', features=output)
out_file = open(output_file, "w")
out_file.write(json.dumps(geojson, indent=2))
out_file.close()
