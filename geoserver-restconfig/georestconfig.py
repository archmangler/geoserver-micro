from geoserver.catalog import Catalog
cat = Catalog("http://localhost:8080/geoserver/rest")
topp = cat.get_workspace("topp")
#shapefile_plus_sidecars = shapefile_and_friends("states")
