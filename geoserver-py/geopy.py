from osgeo import gdal
#import gdal
from geoserver import GeoServer

# Connect to a GeoServer instance
geoserver = GeoServer(
    service_url="http://localhost:8080/geoserver",
    username="admin",
    password="geoserver"
)

# Get all workspaces
workspaces = geoserver.get_workspaces()
print("Printing workspaces: ",workspaces)

# Create a workspace
#NOTE: This operation is not idempotent - it errors if the workspace does already exist.
#geoserver.create_workspace_from_name(name="antedeluvian")
# or geoserver.create_workspace(body={"workspace": {"name": "my_workspace"}})

#To delete a workspace:
#geoserver.delete_workspace(workspace="antedeluvian", recurse=True)

# Get all datastores
the_workspace="antedeluvian"
datastores = geoserver.get_data_stores(workspace=the_workspace)
print("Listing datastores: ",datastores)

# Upload a Shapefile
#geoserver.upload_data_store(file="./gis-osm/gis_osm_water_a_free_1.shp", workspace="antedeluvian")
#NOTE: At this point you should have a layer

#Add another layer from a shapefile
#geoserver.upload_data_store(file="./gis-osm/gis_osm_buildings_a_free_1.shp", workspace="antedeluvian")

# Upload a GeoTIFF
#geoserver.upload_coverage_store(file="./geotiff-sample.tif", format="geotiff", workspace="antedeluvian")

#Create a new data stores from a file already present in the GeoServer instance
#Now that we have uploaded a file gis_osm_water_a_free_1.shp to the GeoServer instance, we can create a new data store from this file.

# Using JSON format
body={
    "dataStore": {
        "name": "gis_osm_water_a_free_2",
        "connectionParameters": {
            "entry": [
                {"@key":"url", "$": "file:/opt/geoserver/data_dir/data/antedeluvian/gis_osm_water_a_free_1/gis_osm_water_a_free_1.shp"},
                {"@key":"filetype", "$": "shapefile"},
            ]
        }
    }
}

# Using XML format
#body = """
#<dataStore>
#    <name>buildings_v2</name>
#    <connectionParameters>
#        <entry key="url">file:/opt/geoserver/data_dir/data/antedeluvian/gis_osm_water_a_free_1/gis_osm_water_a_free_1.shp</entry>
#        <entry key="filetype">shapefile</entry>
#    </connectionParameters>
#</dataStore>
#"""

#print(geoserver.create_data_store(body=body, workspace="antedeluvian"))

#Datasource from PostGIS Database
#Using Docker: https://github.com/postgis/docker-postgis
#postgis/postgis:17-3.5
#docker run --name geoserver  -e POSTGRES_PASSWORD=geoserver -d postgis/postgis
# Client container
#docker run -it --rm postgis/postgis psql -h some-postgis -U postgres

#?
#! ogr2ogr -f PostgreSQL PG:"host=localhost port=5432 user=postgres dbname=geoserver-gis password=geoserver" ./data/gis_osm_landuse_a_free_1.shp -nlt PROMOTE_TO_MULTI -lco OVERWRITE=YES
#You may need to do this: export PROJ_DATA="/opt/homebrew/Cellar/proj/9.5.1/share/proj/"

#Once added, you should also publish the feature types contained in the data store. Use the create_feature_type method to do this.
# Using JSON format:
body = {
    "featureType": {
        "name": "landuse",
        "title": "landuse",
        "advertised": "true",
    }
}

#geoserver.create_feature_type(body=body, workspace="antedeluvian", store="gis_osm_water_a_free_2")

#Printing workspaces:  {'workspaces': {'workspace': [{'name': 'antedeluvian', 'href': 'http://localhost:8080/geoserver/rest/workspaces/antedeluvian.json'}]}}
#Listing datastores:  {'dataStores': {'dataStore': [{'name': 'gis_osm_buildings_a_free_1', 'href': 'http://localhost:8080/geoserver/rest/workspaces/antedeluvian/datastores/gis_osm_buildings_a_free_1.json'}, {'name': 'gis_osm_water_a_free_1', 'href': 'http://localhost:8080/geoserver/rest/workspaces/antedeluvian/datastores/gis_osm_water_a_free_1.json'}, {'name': 'gis_osm_water_a_free_2', 'href': 'http://localhost:8080/geoserver/rest/workspaces/antedeluvian/datastores/gis_osm_water_a_free_2.json'}]}}
#Traceback (most recent call last):
#  File "/Users/traiano/Desktop/geoserver-micro/geoserver-py/geopy.py", line 89, in <module>
#    geoserver.create_feature_type(body=body, workspace="antedeluvian", store="gis_osm_water_a_free_2")
#  File "/opt/anaconda3/lib/python3.12/site-packages/geoserver/geoserver.py", line 1164, in create_feature_type
#    self._request(method="post", url=url, body=body)
#  File "/opt/anaconda3/lib/python3.12/site-packages/geoserver/base.py", line 110, in _request
#    raise GeoServerError(message=message, status_code=response.status_code)
#geoserver.exceptions.GeoServerError: Error 400: Trying to create new feature type inside the store, but no attributes were specified. The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).
#

print(geoserver.get_data_store(name="gis_osm_water_a_free_2", workspace="antedeluvian"))

#Clear a datastore cache:
print(geoserver.reset_data_store_caches(name="gis_osm_water_a_free_2", workspace="antedeluvian"))
