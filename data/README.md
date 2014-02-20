The basics of downloading and cleaning gtfs data.

## Downloading Data

1. `Use get_agencies.py` (or whatever other method you like) to snag a list of all of the agencies with GTFS:

`wget http://www.gtfs-data-exchange.com/api/agencies -O agencies.json`

2. Check for the URL of the most recent GTFS feed for your agency of choice

`wget http://www.gtfs-data-exchange.com/api/agency?agency=metropolitan-atlanta-rapid-transit-authority -O marta.json`

3. Download that feed!

`wget http://gtfs.s3.amazonaws.com/metropolitan-atlanta-rapid-transit-authority_20140115_0110.zip -O gtfs.zip`

## Validating Data

* Reasons not to check data
  * You really trust the tech folks at the agency
  * You’re ok with hitting possible errors
* Reasons to check
  * Sometimes people put weird stuff in GTFS
    * Nested folders
    * pdf license agreements
  * Sometimes the data is super messy
  * Measure twice, cut once?

### GTFS Feed Validator

This validation tool can be found at https://code.google.com/p/googletransitdatafeed/wiki/FeedValidator 
1. Download compressed folder
2. Untar/unzip
3. Change directory and run

`cd transitfeed-1.2.12` (make sure the version is correct)

`python feedvalidator.py path/to/gtfs.zip`

4. Errors will pop up in a your web browser

### Conveyal Validator

New java-based tool in development

https://github.com/conveyal/gtfs-validator