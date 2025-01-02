import json
from owslib.ogcapi.records import Records

record_data = './record.json'

url = 'http://localhost:8080/geoserver'
collection_id = 'metadata:main'

r = Records(url)
#
#cat = r.collection(collection_id)
#
#with open(record_data) as fh:
#   data = json.load(fh)
#
#identifier = data['id']
#
#r.collection_item_delete(collection_id, identifier)
#
## insert metadata
#r.collection_item_create(collection_id, data)
#
## update metadata
#r.collection_item_update(collection_id, identifier, data)
#
## delete metadata
#r.collection_item_delete(collection_id, identifier)
