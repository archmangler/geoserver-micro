#NOt sure what's supposed to go on here
#FIX THIS!!!
from owslib.ogcapi.coverages import Coverages
w = Coverages('https://dev.api.weather.gc.ca/coverages-demo')
print(w.url)

api = w.api()  # OpenAPI document

#collections = w.collections()
#
#print("length of collections: ",len(collections['collections']))
#
#coverages = w.coverages()
#
#print("Number of coverages: ",len(coverages))
#
#gdps = w.collection('gdps-temperature')
#
#print(gdps['id'])
#print(gdps['title'])
#print(gdps['description'])
#
#print(gdps['extent']['spatial']['grid'][0])
#print({"cellsCount": 2400, "resolution": 0.15000000000000002 })
#
#print(gdps['extent']['spatial']['grid'][1])
#
#schema = w.collection_schema('gdps-temperature')
#
#print("Length of schema : ",len(schema['properties']))
#
#print(schema['properties']['1']['type'])
#
#gdps_coverage_data = w.coverage('gdps-temperature', range_subset=[1])
#
#print("GDPS Coverage data: ",gdps_coverage_data)
