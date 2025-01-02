import os
os.environ["USE_PYGEOS"] = "0"  # force use Shapely with GeoPandas

import geopandas as gpd

# Import WFS from owslib
from owslib.wfs import WebFeatureService
wfs_url = "http://localhost:8080/geoserver/wfs"  # TEST_USE_PROD_DATA

# Connect to GeoServer WFS service.
wfs = WebFeatureService(wfs_url, version="2.0.0")

# Print the list of available layers
print(sorted(wfs.contents.keys()))

#Example output should be:
#['ne:boundary_lines', 'ne:coastlines', 'ne:countries', 'ne:disputed_areas', 'ne:populated_places', 'sf:archsites', 'sf:bugsites', 'sf:restricted', 'sf:roads', 'sf:streams', 'tiger:giant_polygon', 'tiger:poi', 
# 'tiger:poly_landmarks', 'tiger:tiger_roads', 'topp:states', 'topp:tasmania_cities', 'topp:tasmania_roads', 'topp:tasmania_state_boundaries', 'topp:tasmania_water_bodies']

sorted_layer_ids = list(sorted(wfs.contents.keys()))

print("sorted layer ids: ",sorted_layer_ids)

tiger_admin_landmarks_index = sorted_layer_ids.index("tiger:poly_landmarks")

print(tiger_admin_landmarks_index)

for layerID in sorted_layer_ids[
    tiger_admin_landmarks_index - 1 : tiger_admin_landmarks_index + 2
]:
    layer = wfs[layerID]
    print("Layer ID:", layerID)
    print("Title:", layer.title)
    print("Boundaries:", layer.boundingBoxWGS84, "\n")

#Example output:
#
#Layer ID: tiger:poi
#Title: Manhattan (NY) points of interest
#Boundaries: (-74.0118315772888, 40.70754683896324, -74.00857344353275, 40.711945649065406) 
#
#Layer ID: tiger:poly_landmarks
#Title: Manhattan (NY) landmarks
#Boundaries: (-74.047185, 40.679648, -73.90782, 40.882078) 
#
#Layer ID: tiger:tiger_roads
#Title: Manhattan (NY) roads
#Boundaries: (-74.02722, 40.684221, -73.907005, 40.878178) 
#

#Getting features from a layer:
#We can then perform a GetFeatures call using the layer name as a target. 
#This returns an IOstream that can be written as a geoJSON file, a common file format for vector data served throughout the web. 
#To reduce the download size, we’ll only fetch the features (here polygons), intersecting a small region defined by a bounding box.

layer_id = "tiger:tiger_roads"
meta = wfs.contents[layer_id]

#Let's get the title
print(meta.title)

# Get the actual data
data = wfs.getfeature(
    typename="tiger:tiger_roads",
    bbox=(-74.02722, 40.684221, -73.907005, 40.878178),
    outputFormat="JSON",
)

fn = "output.geojson"

with open(fn, "wb") as fh:
    fh.write(data.read())

#Graph the features on a plot:
layers = gpd.read_file(fn)
layers.plot()






