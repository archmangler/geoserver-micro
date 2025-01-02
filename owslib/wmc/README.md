# Web Map Context Documents (WMS)

## Overview of WMC

* A Web Map Context Document specifies how a grouping of one or more maps coming from one or more Web Map Services servers can be described in a portable, platform-independent format for storage in a repository or for transmission between clients.

A Web Map Context Document can:

* Provide default views for particular users and applications;
* Save the state for a Viewer Client during a session; and
* Allow a view saved by one client to be used by a different client to view the same content.
* This WMC specification is designed as a companion specification to the Web Map Service (WMS), but can be used by a broad range of services providing content in the form of a catalogue, for WMS layers. Context Documents can also be catalogued and discovered, and are analogous to 'projects' in common desktop applications of Geographic Information Systems (GIS).

Alternative explanation:

```
This specification states how a specific grouping of one or more maps from one or more map servers can be described in a portable, platform-independent format for storage in a repository or for transmission between clients. This description is known as a “Web Map Context Document,” or simply a “Context.” A Context document includes information about the server(s) providing layer(s) in the overall map, the bounding box and map projection shared by all the maps, sufficient operational metadata for Client software to reproduce the map, and ancillary metadata used to annotate or describe the maps and their provenance for the benefit of human viewers. A Context document is structured using eXtensible Markup Language (XML). If you are interested in a more powerful alternative that supports web services beyond WMS consider using OWS Context.
```
-- Reference: https://www.ogc.org/publications/standard/wmc/#:~:text=This%20standard%20specification%20applies%20to,to%20recreate%20the%20application%20state.


