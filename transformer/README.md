The basics of processing GTFS with the [OneBusAway GTFS Transformer CLI](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current/onebusaway-gtfs-transformer-cli.html)

## Usage

1. Move into this directory `cd learnyougtfs/transformer`

2. Run transformer (full documentation is [here](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current-SNAPSHOT/onebusaway-gtfs-transformer-cli.html))
  * `java -jar -Xmx4G -server onebusaway-gtfs-transformer-cli-1.3.3.jar --transform=match.json ../data/google_transit.zip ../data/gtfs_out.zip`

### Examples
To change the transformations you perform on your gtfs feed, open `match.json` and change the arguments to suit your needs.

Here are some examples (use one at a time):
```json
{"op":"retain", "match":{"file":"routes.txt", "route_short_name":"RED"}}

{"op":"retain", "match":{"file":"trips.txt", "trip_id":"2139539"}}

{"op":"retain", "match":{"file":"trips.txt", "trip_id":"2139539"}, "retainBlocks":false}
```
