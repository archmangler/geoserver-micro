# Use Case analysis

* This is an analysis of the key use-cases that might be covered by the microservices in this this repo.

## Location coordinate plotting (Geolocation)

* 1. User will provide a location co-ordinate, and geoservice will return a map layer with the location plotted as a point

## Path Plotting

* 2. User will provide a series of location co-ordinates, and geoservice will return a map layer with the coordinates plotted as a series of points ('path').

## 3. User will provide a description of the location and the geoservice will return the location coordinates

Given a textual description of the location, possibly including an address, the geolocation system will locate the description as one or more possible locations defined by:

 - A map layer
 - A bounding box coordinate system
 - a set of point-coordinates

