# MTA Service Alerts API

The MTA's 'API' for service alerts by service type and line is found [here](http://web.mta.info/status/serviceStatus.txt).

The goal of this project is twofold:
* Make the current 'API' (an XML document that updated every few minutes) more-easily digested for developers. Ideally, as a JSON.
* Expand upon that to make a more useful API.
  * Parse the alerts to effectively categorize/tag by line, alert type, station, etc.
  * Expose endpoints to make them easily accessible.

### Resources:
[JSON API](http://jsonapi.org/): A standard specification for JSON formatting. This project should hew closely to it.
[MBTA API](http://www.mbta.com/rider_tools/developers/): The API of the MBTA (Mass. Bay Transportation Authority). Should give a basis for designing the API.  
[Archived data](http://data.mytransit.nyc/): Archive of all service status, GTFS, and other MTA-related data
