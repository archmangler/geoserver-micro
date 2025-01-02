#!/bin/bash
#including CSW plugin
#VERSION=2.25.2
VERSION=2.26.x
docker run -d \
  -p 8080:8080 \
  --name geoservice \
  -e GEOSERVER_ADMIN_PASSWORD=geoserver \
  -e COMMUNITY_EXTENSIONS=gwc-sqlite-plugin,ogr-datastore-plugin,querylayer-plugin \
  -e ACTIVE_EXTENSIONS=csw-plugin \
  kartoza/geoserver:2.26.1
#  docker.osgeo.org/geoserver:2.26.x
