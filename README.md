# Data Shapy

Simple utility for getting shape of data from python data. Works for any nested combination
of lists, dicts, tuples and ground types like numbers, strings and None.

Includes a command line utility to summarize the shape of the data in a json file.

## Installation

```
$ pip3 install .
```

Example: let's say you have some json file, e.g a topojson file, and you want to get a quick idea
of the shape of its data:

```
$ json-shape /media/ngv/dev-data/osm/16-17522-24258.topojson 
{'arcs': [[[332, 262]]],
 'objects': {'boundaries': {'geometries': [], 'type': 'GeometryCollection'},
             'buildings': {'geometries': [{'arcs': [[0]],
                                           'properties': {'addr_housenumber': '101',
                                                          'addr_street': 'East '
                                                                         'Huron '
                                                                         'Street',
                                                          'area': 5911,
                                                          'id': 225705735,
                                                          'kind': 'building',
                                                          'kind_detail': 'public',
                                                          'min_zoom': 13.0,
                                                          'name': 'Washtenaw '
                                                                  'County '
                                                                  'Courthouse',
                                                          'scale_rank': 3,
                                                          'sort_rank': 475,
                                                          'source': 'openstreetmap.org'},
                                           'type': 'Polygon'}],
                           'type': 'GeometryCollection'},
             'earth': {'geometries': [{'arcs': [[341]],
                                       'properties': {'area': 1495710,
                                                      'kind': 'earth',
                                                      'sort_rank': 10,
                                                      'source': 'openstreetmapdata.com'},
                                       'type': 'Polygon'}],
                       'type': 'GeometryCollection'},
             'landuse': {'geometries': [{'arcs': [[342]],
                                         'properties': {'area': 21580,
                                                        'id': 256670716,
                                                        'kind': 'school',
                                                        'min_zoom': 15.0,
                                                        'operator': 'Ann Arbor '
                                                                    'Public '
                                                                    'Schools',
                                                        'sort_rank': 79,
                                                        'source': 'openstreetmap.org',
                                                        'tier': 6},
                                         'type': 'Polygon'}],
                         'type': 'GeometryCollection'},
             'places': {'geometries': [{'coordinates': [2081, 3238],
                                        'properties': {'area': 366999,
                                                       'id': 85875895,
                                                       'kind': 'neighbourhood',
                                                       'kind_tile_rank': 3,
                                                       'max_zoom': 18.0,
                                                       'min_zoom': 15.0,
                                                       'name': 'Kerrytown',
                                                       'source': 'whosonfirst.mapzen.com'},
                                        'type': 'Point'}],
                        'type': 'GeometryCollection'},
             'pois': {'geometries': [{'coordinates': [1352, 823],
                                      'properties': {'area': 254,
                                                     'id': -7385996,
                                                     'kind': 'shoemaker',
                                                     'min_zoom': 16.56,
                                                     'name': 'Park Shoe Repair',
                                                     'osm_relation': True,
                                                     'source': 'openstreetmap.org'},
                                      'type': 'Point'}],
                      'type': 'GeometryCollection'},
             'roads': {'geometries': [{'arcs': [138],
                                       'properties': {'footway': 'sidewalk',
                                                      'id': 454364588,
                                                      'kind': 'path',
                                                      'kind_detail': 'footway',
                                                      'min_zoom': 15.0,
                                                      'sort_rank': 354,
                                                      'source': 'openstreetmap.org'},
                                       'type': 'LineString'}],
                       'type': 'GeometryCollection'},
             'transit': {'geometries': [], 'type': 'GeometryCollection'},
             'water': {'geometries': [], 'type': 'GeometryCollection'}},
 'transform': {'scale': [1.3411e-06, 9.922e-07],
               'translate': [-83.7487792969, 42.2813730219]},
 'type': 'Topology'}
```