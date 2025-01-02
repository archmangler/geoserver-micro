#Testing the Geoserver REST API using python module `geoserverw-rest`
#python -m venv .venv
from geo.Geoserver import Geoserver
geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')

