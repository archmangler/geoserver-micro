# Interacting with CSW services hosted by geoserver

## Overview of CSW

```
Catalogue Service for the Web (CSW), sometimes seen as Catalogue Service - Web, is a standard for exposing a catalogue of geospatial records in XML on the Internet (over HTTP). The catalogue is made up of records that describe geospatial data (e.g. KML), geospatial services (e.g. WMS), and related resources.

CSW is one part (or "profile") of the OGC Catalogue Service, which defines common interfaces to discover, browse, and query metadata about data, services, and other potential resources. Version 2.0 of the specification was released in May 2004. The most recent release is 2.0.2, which was published in 2007.[1][2]

The records are in XML according to the standard. Typically the records include Dublin Core, ISO 19139 or FGDC metadata, encoded in UTF-8 characters. Each record must contain certain core fields including: Title, Format, Type (e.g. Dataset, DatasetCollection or Service), BoundingBox (a rectangle of interest, expressed in latitude and longitude), Coordinate Reference System, and Association (a link to another metadata record).

Operations defined by the CSW standard include:[1][3]

GetCapabilities: "allows CSW clients to retrieve service metadata from a server"
DescribeRecord: "allows a client to discover elements of the information model supported by the target catalogue service. The operation allows some or all of the information model to be described".
GetRecords: search for records, returning record IDs
GetRecordById: "retrieves the default representation of catalogue records using their identifier"
GetDomain (optional): "used to obtain runtime information about the range of values of a metadata record element or request parameter"
Harvest (optional): create/update metadata by asking the server to 'pull' metadata from somewhere
Transaction (optional): create/edit metadata by 'pushing' the metadata to the server
Requests can encode the parameters in three different ways:

GET with URL parameters
POST with form-encoded payload
POST with XML payload
Responses are in XML.
```


## Enabling CSW Service in Geoserver (Plugin)

```
The CSW extension is listed among the other extension downloads on the GeoServer download page.

The installation process is similar to other GeoServer extensions:

Download the geoserver-2.27.x-csw-plugin.zip

Verify that the version number in the filename corresponds to the version of GeoServer you are running (for example 2.27-SNAPSHOT above).

Extract the contents of the archive into the WEB-INF/lib directory in GeoServer. Make sure you do not create any sub-directories during the extraction process.

Restart GeoServer or the servlet container, as appropriate to your configuration.

Verify that the module was installed correctly by navigating to the Welcome page of the Web administration interface and seeing the CSW entry is listed in the Service Capabilities list, and the CSW modules are listed in the Web administration interface Module list.




```
