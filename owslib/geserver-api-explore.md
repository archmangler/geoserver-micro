1. List WMS capabilities:

```
(venv) traiano@Traianos-iMac owslib % python
Python 3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> from owslib.wms import WebMapService
>>> wms = WebMapService('http://localhost:8080/geoserver/wms', version='1.1.1')
>>> wms.identification.type
'OGC:WMS'
>>> wms.identification.version
'1.1.1'
>>> wms.identification.title
'GeoServer Web Map Service'
>>> 
>>> 
>>> wms.identification.abstract
'A compliant implementation of WMS plus most of the SLD extension (dynamic styling). Can also generate PDF, SVG, KML, GeoRSS'
>>> 
>>> 
>>> 
```

2. Available Layers:

```
>>> list(wms.contents)
['spearfish', 'tasmania', 'tiger-ny', 'ne:world', 'ne:countries', 'ne:disputed_areas', 'ne:coastlines', 'ne:boundary_lines', 'ne:populated_places', 'nurc:Arc_Sample', 'nurc:Img_Sample', 'nurc:Pk50095', 'sf:archsites', 'sf:bugsites', 'tiger:giant_polygon', 'nurc:mosaic', 'tiger:poi', 'tiger:poly_landmarks', 'sf:restricted', 'sf:roads', 'sf:sfdem', 'topp:states', 'sf:streams', 'topp:tasmania_cities', 'topp:tasmania_roads', 'topp:tasmania_state_boundaries', 'topp:tasmania_water_bodies', 'tiger:tiger_roads']
>>
```


3. List details of a given layer:

```
>>> 
>>> wms['ne:coastlines'].title
'Coastlines'
>>> 
 
```
>>> 
>>> wms['ne:coastlines'].title
'Coastlines'
>>> 
>>> 
>>> wms['ne:countries'].title
'Countries'
>>> 
>>> wms['tasmania'].title
'Tasmania'
>>> 
>>> wms['ne:countries'].boundingBoxWGS84
(-180.0, -90.0, 180.0, 83.64513)
>>> 

>>> wms['ne:countries'].styles
{'default-style-ne:world': {'title': 'ne:world style', 'legend': 'http://localhost:8080/geoserver/wms?request=GetLegendGraphic&version=1.1.1&format=image%2Fpng&width=20&height=20&layer=ne%3Aworld'}, 'ne:countries_mapcolor9': {'title': 'Countries Mapcolor9', 'legend': 'http://localhost:8080/geoserver/wms?request=GetLegendGraphic&version=1.1.1&format=image%2Fpng&width=20&height=20&layer=ne%3Acountries'}, 'polygon': {'title': 'Default Polygon', 'legend': 'http://localhost:8080/geoserver/wms?request=GetLegendGraphic&version=1.1.1&format=image%2Fpng&width=20&height=20&layer=ne%3Acountries&style=polygon'}, 'ne:countries': {'title': 'Countries', 'legend': 'http://localhost:8080/geoserver/wms?request=GetLegendGraphic&version=1.1.1&format=image%2Fpng&width=20&height=20&layer=ne%3Acountries&style=countries'}}


>>> wms['ne:countries'].boundingBox
(-180.0, -90.0, 180.0, 83.64513, 'EPSG:4326')
>>> 
>>> wms['ne:countries'].boundingBoxWGS84
(-180.0, -90.0, 180.0, 83.64513)

```


* Available methods, their URLs, and available formats:

```
>>> wms.getOperationByName('GetMap').methods
[{'type': 'Get', 'url': 'http://localhost:8080/geoserver/wms?SERVICE=WMS&'}]
```

* Available methods, their URLs, and available formats:

```
>>> wms.getOperationByName('GetMap').formatOptions

['image/png', 'application/atom xml', 'application/atom+xml', 'application/json;type=utfgrid', 'application/openlayers', 'application/openlayers2', 'application/openlayers3', 'application/pdf', 'application/rss xml', 'application/rss+xml', 'application/vnd.google-earth.kml', 'application/vnd.google-earth.kml xml', 'application/vnd.google-earth.kml+xml', 'application/vnd.google-earth.kml+xml;mode=networklink', 'application/vnd.google-earth.kmz', 'application/vnd.google-earth.kmz xml', 'application/vnd.google-earth.kmz+xml', 'application/vnd.google-earth.kmz;mode=networklink', 'atom', 'image/geotiff', 'image/geotiff8', 'image/gif', 'image/gif;subtype=animated', 'image/jpeg', 'image/png8', 'image/png; mode=8bit', 'image/svg', 'image/svg xml', 'image/svg+xml', 'image/tiff', 'image/tiff8', 'image/vnd.jpeg-png', 'image/vnd.jpeg-png8', 'kml', 'kmz', 'openlayers', 'rss', 'text/html; subtype=openlayers', 'text/html; subtype=openlayers2', 'text/html; subtype=openlayers3', 'utfgrid']
```

* Check available styles for a given layer:

```
>>> list(wms.contents)
['spearfish', 'tasmania', 'tiger-ny', 'ne:world', 'ne:countries', 'ne:disputed_areas', 'ne:coastlines', 'ne:boundary_lines', 'ne:populated_places', 'nurc:Arc_Sample', 'nurc:Img_Sample', 'nurc:Pk50095', 'sf:archsites', 'sf:bugsites', 'tiger:giant_polygon', 'nurc:mosaic', 'tiger:poi', 'tiger:poly_landmarks', 'sf:restricted', 'sf:roads', 'sf:sfdem', 'topp:states', 'sf:streams', 'topp:tasmania_cities', 'topp:tasmania_roads', 'topp:tasmania_state_boundaries', 'topp:tasmania_water_bodies', 'tiger:tiger_roads']
>>> 
>>> print(wms['tasmania'].styles)
{'default-style-tasmania': {'title': 'tasmania style', 'legend': 'http://localhost:8080/geoserver/wms?request=GetLegendGraphic&version=1.1.1&format=image%2Fpng&width=20&height=20&layer=tasmania'}}
>>> 
```

* Everything needed to make a request for imagery:

```
img = wms.getmap(   layers=['tasmania'],
                    styles=['default-style-tasmania'],
                    srs='EPSG:4326',
                    bbox=(-112, 36, -106, 41),
                    size=(300, 250),
                    format='image/jpeg',
                    transparent=True
                    )

>>> out = open('tasmania.jpg', 'wb')
>>> 

>>> out.write(img.read())
981

>>> 
>>> out.close()
>>> 

img = wms.getmap(   layers=['ne:world'],
                    styles=['default-style-tasmania'],
                    srs='EPSG:4326',
                    bbox=(-112, 36, -106, 41),
                    size=(300, 250),
                    format='image/jpeg',
                    transparent=True
                    )

>>> from owslib.wms import WebMapService
>>> wms = WebMapService('http://localhost:8080/geoserver/wms', version='1.1.1')
>>> 
>>> 
>>> print(wms['ne:world'].styles)
{'default-style-ne:world': {'title': 'ne:world style', 'legend': 'http://localhost:8080/geoserver/wms?request=GetLegendGraphic&version=1.1.1&format=image%2Fpng&width=20&height=20&layer=ne%3Aworld'}}
>>> 
>>> img = wms.getmap(   layers=['ne:world'],
...                     styles=['default-style-ne:world'],
...                     srs='EPSG:4326',
...                     bbox=(-112, 36, -106, 41),
...                     size=(300, 250),
...                     format='image/jpeg',
...                     transparent=True
...                     )
>>> 
>>> out = open('ne-world.jpg', 'wb')
>>> out.write(img.read())
3348
>>> out.close()
>>> 
```


```
from owslib.wms import WebMapService
wms = WebMapService('http://localhost:8080/geoserver/wms', version='1.1.1')
print(wms['ne:world'].styles)
img = wms.getmap(   layers=['ne:world'],
                     styles=['default-style-ne:world'],
                     srs='EPSG:4326',
                     bbox=(-112, 36, -106, 41),
                     size=(600, 500),
                     format='image/jpeg',
                     transparent=True
                     )
out = open('ne-world.jpg', 'wb')
out.write(img.read())
out.close()
```


Example:

```
(venv) traiano@Traianos-iMac owslib % python                   
Python 3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from owslib.wms import WebMapService
>>> wms = WebMapService('http://localhost:8080/geoserver/wms', version='1.1.1')
>>> print(wms['ne:world'].styles)
{'default-style-ne:world': {'title': 'ne:world style', 'legend': 'http://localhost:8080/geoserver/wms?request=GetLegendGraphic&version=1.1.1&format=image%2Fpng&width=20&height=20&layer=ne%3Aworld'}}
>>> img = wms.getmap(   layers=['ne:world'],
...                      styles=['default-style-ne:world'],
...                      srs='EPSG:4326',
...                      bbox=(-1012, 360, -1006, 410),
...                      size=(1024, 768),
...                      format='image/jpeg',
...                      transparent=True
...                      )
>>> out = open('ne-world.jpg', 'wb')
>>>  out.write(img.read())
  File "<python-input-6>", line 1
    out.write(img.read())
IndentationError: unexpected indent
>>> out.write(img.read())
5133
>>> out.close()
>>> quit
```

* The following code should generate extracts from the world map (North east/nw layer) within a specified bounding box:

```
from owslib.wms import WebMapService
wms = WebMapService('http://localhost:8080/geoserver/wms', version='1.1.1')

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
```







4. Connect to a WFS and inspect its capabilities.

```
(venv) traiano@Traianos-iMac owslib % python            
Python 3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 16.0.0 (clang-1600.0.26.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from owslib.wfs import WebFeatureService
>>> 
>>> 
>>> [operation.name for operation in wfs11.operations]

['GetCapabilities', 'DescribeFeatureType', 'GetFeature', 'GetGmlObject', 'LockFeature', 'GetFeatureWithLock', 'Transaction']
```

5. List FeatureTypes

```



```