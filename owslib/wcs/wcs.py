#Web Coverage Service
import matplotlib.pyplot as plt
import xarray as xr
from owslib.wcs import WebCoverageService

# NBVAL_IGNORE_OUTPUT
wcs_url = "http://geo.weather.gc.ca/geomet/?lang=en&service=WCS"
#This might work but needs auth:
#wcs_url = "http://localhost:8080/geoserver/?lang=en&service=WCS"

# Connect to service
wcs = WebCoverageService(wcs_url, version="2.0.1")
print(wcs.identification.title)

# List some of the content available
print(sorted(list(wcs.contents.keys()))[:10])

# Get some information about a given layer
# In this case it's the "salinity" property which has been included
# in the layer metadata
layerid = "OCEAN.GIOPS.3D_SALW_0000"
temp = wcs[layerid]

# Title
print("Layer title :", temp.title)

# bounding box
print("BoundingBox :", temp.boundingBoxWGS84)

# supported data formats - we'll use geotiff
print("Formats :", temp.supportedFormats)

# grid dimensions
print("Grid upper limits :", temp.grid.highlimits)

#To request data, we need to call the getCoverage service, which requires us specifying the 
# geographic projection, the bounding box, the resolution and format of the output. 
# With GeoMet 2.0.1, we can now get layers in the netCDF format.

format_wcs = "image/netcdf"
bbox_wcs = temp.boundingboxes[0]["bbox"]  # Get the entire domain
crs_wcs = temp.boundingboxes[0]["nativeSrs"]  # Coordinate system
w = int(temp.grid.highlimits[0])
h = int(temp.grid.highlimits[1])

print("Format:", format_wcs)
print("Bounding box:", bbox_wcs)
print("Projection:", crs_wcs)
print(f"Resolution: {w} x {h}")

output = wcs.getCoverage(
    identifier=[
        layerid,
    ],
    crs=crs_wcs,
    bbox=bbox_wcs,
    width=w,
    height=h,
    format=format_wcs,
)

#We then save the output to disk, open it normally using xarray and plot it’s variable.
fn = layerid + ".nc"
with open(fn, "wb") as fh:
    fh.write(output.read())

ds = xr.open_dataset(fn)
print(ds.data_vars)
ds.Band1.plot()
plt.show()


