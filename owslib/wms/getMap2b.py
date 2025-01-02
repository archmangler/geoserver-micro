from owslib.wms import WebMapService

wms_url = "https://ows.terrestris.de/osm/service"

wms = WebMapService(wms_url, version="1.3.0")

print(f"WMS version: {wms.identification.version}")
print(f"WMS title: {wms.identification.title}")
print(f"WMS abstract: {wms.identification.abstract}")
print(f"Provider name: {wms.provider.name}")
print(f"Provider address: {wms.provider.contact.address}")

#Check the Capabilities response directly from the server

#1. Available WMS layers:
print(list(wms.contents))

#2. Get the bounding box property for tiger:poi
print(wms.contents['SRTM30-Colored'].boundingBox)

print(wms.contents['SRTM30-Colored'].boundingBoxWGS84)

#3. Get styles
print(wms.contents['SRTM30-Colored'].styles)


#Get the available methods supported by this WMS service:
#Available methods, their URLs, and available formats:

#operations supported
print([op.name for op in wms.operations])

#
wms.getOperationByName('GetMap').methods

#
wms.getOperationByName('GetMap').formatOptions

#The above can now be combined to get a full map:
img = wms.getmap(
    layers=['SRTM30-Colored'],
    size=[600, 400],
    srs="EPSG:4326",
    bbox=[1.0, 50.0, 10.0, 54.0],
    format="image/jpeg")

#NOTE: you need jupyter notebook installed and working for
from IPython.display import Image
Image(img.read())