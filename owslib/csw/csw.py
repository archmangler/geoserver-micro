#interact with geoserver via csw service
from owslib.csw import CatalogueServiceWeb
csw = CatalogueServiceWeb('http://localhost:8080/geoserver/csw')

print(csw.identification.type)

#Print the capabilities of this CSW
print([op.name for op in csw.operations])

#E.g output: ['GetCapabilities', 'DescribeRecord', 'GetDomain', 'GetRecords', 'GetRecordById']

#Get supported resultTypes:

csw.getdomain('GetRecords.resultType')
print(csw.results)

#Get some data from a particular layer
from owslib.fes import PropertyIsEqualTo, PropertyIsLike, BBox
birds_query = PropertyIsEqualTo('csw:AnyText', 'birds')

csw.getrecords2(constraints=[birds_query], maxrecords=20)
print(csw.results)

for rec in csw.records:
    print(csw.records[rec].title)

#Search for bird data in Canada
bbox_query = BBox([-141,42,-52,84])
csw.getrecords2(constraints=[birds_query, bbox_query])
print(csw.results)

#Using CQL: Search using CQL
print("Searching using CQL: ...")
print(csw.getrecords2(cql='csw:AnyText like "%birds%"'))

#The following examples based on the documentation don't seem to work.

#Transaction: insert
#Note: first populate file.xml with something "sensible".

#csw.transaction(ttype='insert', typename='gmd:MD_Metadata', record=open("file.xml").read())

#Update all records
# update ALL records

#csw.transaction(ttype='update', typename='csw:Record', propertyname='dc:title', propertyvalue='New Title')

#csw.transaction(ttype='update', typename='csw:Record', propertyname='dc:title', propertyvalue='New Title', keywords=['birds','fowl'])

# update records satisfying BBOX filter
#csw.transaction(ttype='update', typename='csw:Record', propertyname='dc:title', propertyvalue='New Title', bbox=[-141,42,-52,84])

#csw.harvest('http://host/url.xml', 'http://www.isotc211.org/2005/gmd')
