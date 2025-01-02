#OGC API - Features - Part 1: Core 1.0¶
#The OGC API standards are a clean break from the traditional OGC service architecture using current design patterns (RESTful, JSON, OpenAPI). 
#As such, OWSLib the code follows the same pattern.

from owslib.ogcapi.features import Features
w = Features('https://demo.pygeoapi.io/master')
print(w.url)

conformance = w.conformance()
print(conformance)

api = w.api()  # OpenAPI document/
collections = w.collections()
print(len(collections['collections']))
feature_collections = w.feature_collections()
print("feature collections: ",feature_collections)

lakes = w.collection('lakes')
#print("lakes in collection: ",lakes)
print(lakes['id'])
print(lakes['title'])
print(lakes['description'])
lakes_queryables = w.collection_queryables('lakes')
print(lakes_queryables)

lakes_query = w.collection_items('lakes')
print(lakes_query['features'][1]['properties'])

