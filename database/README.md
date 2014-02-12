The basics of putting GTFS into a database with the [OneBusAway GTFS Hibernate CLI](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current/onebusaway-gtfs-hibernate-cli.html)

## Setup

1. Move into this directory `cd learnyougtfs/database`

2. Create a database called `gtfs` with the sql flavor of your choice.  If you're not familiar with or don't have a database software installed, the easiest to use is probably just HSQLDB (does not require setting up a separate database software). 

3. Run hibernate (full documentation is [here](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/current-SNAPSHOT/onebusaway-gtfs-transformer-cli.html))

### Generic
```bash
java -classpath onebusaway-gtfs-hibernate-cli-1.3.3.jar:your-database-jdbc.jar \
 org.onebusaway.gtfs.GtfsDatabaseLoaderMain \
 --driverClass=... \
 --url=... \
 --username=... \
 --password=... \
 gtfs_path
```

### HSQLDB (default)
```bash
java -classpath onebusaway-gtfs-hibernate-cli-1.3.3.jar:hsqldb.jar \
 org.onebusaway.gtfs.GtfsDatabaseLoaderMain \
 --driverClass=org.hsqldb.jdbcDriver \
 --url=jdbc:hsqldb:file:gtfs \
 --username=user \
 --password=pass \
 ../data/google_transit.zip
```

After a successful gtfs import, run `java -jar sqltool.jar` to open the sql tools command line interface.

To connect to the `gtfs` database in sql tools, type `\j user pass jdbc:hsqldb:file:gtfs`

### Postgresql (assumes version 9.3)
```bash
java -classpath onebusaway-gtfs-hibernate-cli-1.3.3.jar:postgresql-9.3-1100.jdbc4.jar \
 org.onebusaway.gtfs.GtfsDatabaseLoaderMain \
 --driverClass=org.postgresql.Driver \
 --url=jdbc:postgresql://localhost/gtfs \
 --username=postgres \
 --password= \
 ../data/google_transit.zip
```

