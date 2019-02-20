# SharedStreets (Python)

This fork has utilities for turning event SharedStreets event tiles into geojson.

See https://github.com/sharedstreets/sharedstreets-python for source project README.

## Setup

1. Clone this fork

        git clone git@github.com:schnerd/sharedstreets-python.git
        cd sharedstreets-python

1. Prepare a [Python virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenv) running Python 3.

1.  Install the `sharedstreets` module, keeping it editable
    
        pip install --editable .

1.  Install shapely dependency
    
        pip install shapely

## Use

### Convert events tile to.

If you just ran the [SharedStreets matcher](https://github.com/sharedstreets/sharedstreets-matcher), chances are you ended up with tiles containing `SharedStreetsWeeklyBinnedLinearReferences`. You can use `events-to-geojson.py` to convert this to a geojson file, suitable for visualization in kepler.

```
python events-to-geojson.py [input_path] [output_file]
```

For example:
```
python events-to-geojson.py ../event_tiles ./events.geojson
```

### Other scripts

`events-aggregate.py` can be used to convert `SharedStreetsWeeklyBinnedLinearReferences` to `SharedStreetsBinnedLinearReferences`.

`events-filter.py` can be used to filter out non-desirable event types from tiles.
