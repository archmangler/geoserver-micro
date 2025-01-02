# Working with Web Coverage Service

## Overview


```
The Open Geospatial Consortium (OGC) Web Coverage Service (WCS) Interface Standard defines a web-based interface for the retrieval of coverages—that is, digital geospatial information representing space/time-varying phenomena. By providing direct access to underlying geospatial data rather than just static map images, WCS enables more advanced analysis, modeling, and processing of GIS data.

A Web Coverage Service (WCS) provides access to coverage data in forms that are useful for client-side rendering, as input into scientific models, and for other analytical clients. It may be compared to the OGC Web Feature Service (WFS) and the Web Map Service (WMS). As with WMS and WFS service instances, a WCS allows clients to choose portions of a server's information holdings based on spatial constraints and other query criteria.

Unlike the OGC Web Map Service (WMS), which portrays spatial data as static, server-rendered images (maps), the Web Coverage Service delivers underlying data values along with their detailed descriptions. This enables a rich syntax for queries against the data and returns information with its original semantics, rather than just pictures, allowing for interpretation, extrapolation, and complex client-side analysis.

Unlike the OGC Web Feature Service (WFS), which returns discrete geospatial features, a WCS returns coverages—representations of space/time-varying phenomena mapping a spatio-temporal domain to a (possibly multidimensional) range of properties. As such, WCS focuses on coverages as a specialized class of features and defines streamlined functionality for their retrieval.

Subsequent versions of WCS, notably the WCS 2.0 series, adopted a modular specification approach, refining requirements and clarifying ambiguities to improve interoperability.[1][2][3] Core operations such as GetCapabilities, DescribeCoverage, and GetCoverage enable clients to request and obtain coverage data in various formats and coordinate reference systems, facilitating more sophisticated data processing and analysis scenarios than simple map portrayal.

WCS uses the coverage model of the OGC GML Application Schema for Coverages,[4] thereby supporting all coverage types defined by that schema. As a result, WCS is not limited to quadrilateral grid coverages, extending beyond what earlier versions of the service supported.

```

-- Wikipedia

## WCS and Geoserver

* Basic WCS API and geoserver
