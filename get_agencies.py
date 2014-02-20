import urllib2, json, time
def get_agencies():
	#Base URL, json comes back by default
	base = 'http://www.gtfs-data-exchange.com/api/agencies'

	# No queries here
	query=''

	# Formulate URL request and format response as json object
	response = urllib2.urlopen(base + query, timeout=30)
	str_response = response.read().decode('utf-8')
	agencies = json.loads(str_response)['data']



	# Prints entirety of json response
	#print(buses)

	output = ''

	# For each agency in response, print a few pieces of data.
	for agency in agencies:
		output = agency['name'] + ' in ' + agency['state'] + ', ' + agency['country'] + ' was last updated on ' + time.strftime('%b %d, %Y', time.localtime(agency['date_last_updated']))

		print output


if __name__ == '__main__':
	get_agencies()