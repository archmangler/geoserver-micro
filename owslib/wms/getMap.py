#WMS: Get a section of a map defined by a bounding box.
from owslib.wms import WebMapService
wms = WebMapService('http://localhost:8080/geoserver/wms', version='1.1.1')

#Return an image of given format from the WMS service:
img = wms.getmap(   layers=['ne:world'],
                     styles=['default-style-ne:world'],
                     srs='EPSG:4326',
                     bbox=(-448, 36, -424, 41),
                     size=(600, 500),
                     format='image/jpeg',
                     transparent=True
                     )
out = open('ne-world.jpg', 'wb')
out.write(img.read())
out.close()
