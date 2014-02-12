The basics of processing GTFS with the [OneBusAway GTFS Transformer CLI](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current/onebusaway-gtfs-transformer-cli.html)


## Setup

1. Make sure Java 1.6 is installed
  * Open a command prompt/terminal and type `java -version`
  * if you get something like...
  ```
      java version "1.6.0_65"
	  Java(TM) SE Runtime Environment (build 1.6.0_65-b14-462-11M4609)
	  Java HotSpot(TM) 64-Bit Server VM (build 20.65-b04-462, mixed mode)
  ```
    ...you're good to go. Otherwise, download and install [Java SDK 6](http://www.oracle.com/technetwork/java/javase/archive-139210.html) **(not 7!)**.

2. Download source code

  [![alt text](zip.png "Download this repository as a zip file")](https://github.com/landonreed/learnyougtfs/archive/master.zip)
  * or `git clone git@github.com:landonreed/learnyougtfs.git`

## Usage

1. Move into directory `cd learnyounode`

2. Run transformer (full documentation is [here](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current-SNAPSHOT/onebusaway-gtfs-transformer-cli.html))
  * `java -jar -Xmx4G -server onebusaway-gtfs-transformer-cli-1.3.3.jar --transform=match.json data/google_transit.zip data/gtfs_out.zip`

### Examples
To change the transformations you perform on your gtfs feed, open `match.json` and change the arguments to suit your needs.

Here are some examples (use one at a time):
```json
{"op":"retain", "match":{"file":"routes.txt", "route_short_name":"RED"}}

{"op":"retain", "match":{"file":"trips.txt", "trip_id":"2139539"}}

{"op":"retain", "match":{"file":"trips.txt", "trip_id":"2139539"}, "retainBlocks":false}
```
