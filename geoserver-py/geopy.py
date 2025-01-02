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
geoserver.upload_data_store(file="./gis-osm/gis_osm_water_a_free_1.shp", workspace="antedeluvian")
#NOTE: At this point you should have a layer

#Add another layer from a shapefile
geoserver.upload_data_store(file="./gis-osm/gis_osm_buildings_a_free_1.shp", workspace="antedeluvian")

# Upload a GeoTIFF
geoserver.upload_coverage_store(file="./", format="geotiff", workspace="my_workspace")

