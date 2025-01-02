#1. Connect to a WFS and inspect its capabilities.
from owslib.wfs import WebFeatureService
wfs11 = WebFeatureService(url='http://localhost:8080/geoserver/wfs', version='1.1.0')

#2. Test getting a basic attribute
print(wfs11.identification.title)

#3. Get the capabilities supported by the WFS on this geoserver
print("Web Feature Service Capabilities")
print([operation.name for operation in wfs11.operations])

#4. list feature types
print(list(wfs11.contents))

#E.g: ['ne:boundary_lines', 'ne:coastlines', 'ne:countries', 'ne:disputed_areas', 'tiger:poly_landmarks', 'tiger:poi', 'tiger:tiger_roads', 'ne:populated_places', 'sf:archsites', 'sf:bugsites', 'sf:restricted', 'sf:roads', 'sf:streams', 'topp:tasmania_cities', 'topp:tasmania_roads', 'topp:tasmania_state_boundaries', 'topp:tasmania_water_bodies', 'topp:states', 'tiger:giant_polygon']

#5. Download GML using typename, bbox and srsname.
#OWSLib will switch the axis order from EN to NE automatically if designated by EPSG-Registry
response = wfs11.getfeature(typename='ne:coastlines', bbox=(4500000,5500000,4500500,5500500), srsname='urn:x-ogc:def:crs:EPSG:4326')

print("downloading GML")
print(response)

#6. Return a FeatureType’s schema via DescribeFeatureType. The dictionary returned is compatible with a Fiona schema object.
#Follow up research: What is a Fiona schema object?
dict=wfs11.get_schema('ne:boundary_lines')

print("Return a FeatureType’s schema via DescribeFeatureType")
print(dict)

#Download GML using typename and filter. OWSLib currently only supports filter building for WFS 1.1 (FE.1.1).
from owslib.fes import *
from owslib.etree import etree
wfs11 = WebFeatureService(url='http://localhost:8080/geoserver/wfs', version='1.1.0')

#Not too sure how this filter works. Will have to figure it out later.
filter = PropertyIsLike(propertyname='geom', literal='Ingolstadt', wildCard='*')
filterxml = etree.tostring(filter.toXML()).decode("utf-8")
print("Using filter specfication: ", filterxml)

response = wfs11.getfeature(typename='ne:countries', filter=filterxml)
print("Response: ",response)

#save the above response to a file:
out = open('./data.gml', 'wb')
out.write(response.read())
out.close()

#Download GML using StoredQueries(only available for WFS 2.0 services)
wfs20 = WebFeatureService(url='http://localhost:8080/geoserver/wfs', version='2.0.0')

# List StoredQueries
print("Listing the available stored queries: ")
for item in [storedquery.id for storedquery in wfs20.storedqueries]:
    print(item)

# List Parameters for StoredQuery[1]
print([parameter.name for parameter in wfs20.storedqueries[0].parameters])

#Play around with this a bit.   
#response = wfs20.getfeature(storedQueryID='urn:ogc:def:query:OGC-WFS::GetFeatureById', storedQueryParams={'ID':'gmd_ex.1'})
#print(response)


