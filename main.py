from geoserver import GeoServer
from geoserver.exceptions import GeoServerError

geoserver = GeoServer(
    "http://localhost:8080/geoserver", 
    username="admin", 
    password="geoserver"
)

workspaces = geoserver.get_workspaces()

try:
    # Already exists
    geoserver.create_workspace( 
        body={"workspace": {"name": "topp"}}
    )
except GeoServerError as e:
    print(f"Status Code: {e.status_code}")
    print(f"Error: {e.message}")


print(workspaces)
