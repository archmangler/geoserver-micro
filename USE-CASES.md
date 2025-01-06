# Use Case analysis

* This is an analysis of the key use-cases that might be covered by the microservices in this this repo.

## Location coordinate plotting (Geolocation)

* User will provide a location co-ordinate, and geoservice will return a map layer with the location plotted as a point
* The objective is to use coordinates extracted from other sources (w.g GPS tracker) and show it as a location on the country Map layer along with any custom map layers that may be of interest to the organisation.

## Path Plotting

* User will provide a series of location co-ordinates, and geoservice will return a map layer with the coordinates plotted as a series of points ('path').
* The objective is to plot the path of an entity (vehicle, person, etc) on the map layers relevant to the organisation.

## 3. User will provide a description of the location and the geoservice will return the location coordinates

* Given a textual description of the location, possibly including an address, the geolocation system will locate the description as one or more possible locations defined by:

 - A map layer
 - A bounding box coordinate system
 - a set of point-coordinates

* The objective is to return a location provided as a text description in the form of an exact collection of coordinates which can be shown on custom map layers.

