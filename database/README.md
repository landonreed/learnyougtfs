The basics of putting GTFS into a database with the [OneBusAway GTFS Hibernate CLI](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current/onebusaway-gtfs-hibernate-cli.html)

## Usage

1. Move into this directory `cd learnyougtfs/database`

2. Create a sql database of your choice.

3. Run hibernate (full documentation is [here](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current-SNAPSHOT/onebusaway-gtfs-transformer-cli.html))

```bash
java -classpath onebusaway-gtfs-hibernate-cli-1.3.3.jar:your-database-jdbc.jar \
 org.onebusaway.gtfs.GtfsDatabaseLoaderMain \
 --driverClass=... \
 --url=... \
 --username=... \
 --password=... \
 gtfs_path
```

### Examples
To change the transformations you perform on your gtfs feed, open `match.json` and change the arguments to suit your needs.

Here are some examples (use one at a time):
