"""
Generates a pickup/dropoff event geojson file from one or mote SharedStreets
weekly binned linear reference tiles. This geojson file is suitable for
visualizing in a tool like kepler.

See the SharedStreetsWeeklyBinnedLinearReferences protobuf schema here:
https://github.com/sharedstreets/sharedstreets-ref-system/blob/master/proto/linear_references.proto
"""

import json
import re
from os import listdir
from os.path import isfile, join
from sharedstreets.linear_references import load_binned_events
from sharedstreets.tile import get_tile, make_geojson
from shapely.geometry import LineString


def createLineString(geom, is_forward):
    ls = LineString([(geom.lonlats[i], geom.lonlats[i + 1])
                     for i in range(0, len(geom.lonlats), 2)])
    offset = .000045
    if is_forward:
        ls = ls.parallel_offset(offset, 'right')
    else:
        ls = ls.parallel_offset(offset, 'left')
    return ls


def processTile(out, file_name):
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
        scaled_counts = None

        # Loop over each reference
        forward_count = 0
        backward_count = 0
        no_match_count = 0
        for event in binned_events:
            geom = None
            forward = None
            scaled_counts = event.scaled_counts
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

            line = createLineString(geom, forward)

            # data indexed as a multi-dimentional array {dataType}{binPosition}{periodOffset}
            types = ['pickup', 'dropoff']
            for t in types:
                if t not in event.data:
                    continue
                datum = event.data.get(t)
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
                            'eventType': t,
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

# You can read all tiles from a specific directory if you want
input_path = '/Users/dschnurr/Downloads/ss-dc-tiles/output_tiles/2017-10-30/events'
input_files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

# However that is *a lot* of data, for now we'll just pick a few tiles downtown
# input_files = [
    #'12-1170-1566.events.pbf',
    #'12-1170-1567.events.pbf',
    #'12-1170-1565.events.pbf',
    #'12-1171-1566.events.pbf',
    #'12-1171-1567.events.pbf',
    #'12-1171-1565.events.pbf',
    #'12-1172-1566.events.pbf',
    #'12-1172-1567.events.pbf',
    #'12-1172-1565.events.pbf'
# ]

for i, filename in enumerate(input_files):
    print("Processing file (%d of %d)" % (i + 1, len(input_files)))
    processTile(output, join(input_path, filename))

print("Length %d" % len(output))
geojson = dict(type='FeatureCollection', features=output)
out_file = open("output.json", "w")
out_file.write(json.dumps(geojson, indent=2))
out_file.close()
