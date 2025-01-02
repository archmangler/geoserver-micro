from owslib.wcs import WebCoverageService
# Create coverage object
#my_wcs = WebCoverageService('http://ows.rasdaman.org/rasdaman/ows', version='2.0.1')
my_wcs = WebCoverageService('http://localhost:8080/geoserver/wcs', version='2.0.1')

# Get list of coverages
print(my_wcs.contents.keys())
#Example output:
#dict_keys(['nurc__Arc_Sample', 'nurc__Img_Sample', 'nurc__Pk50095', 'sf__sfdem', 'nurc__mosaic'])
#['RadianceColor', 'test_irr_cube_2', 'test_mean_summer_airtemp', 'test_double_1d', 'INSPIRE_EL', 'AverageChlorophyllScaled', 'INSPIRE_OI_RGB', 'Temperature4D', 'INSPIRE_OI_IR', 'visible_human', 'INSPIRE_WS_LC', 'meris_lai', 'climate_earth', 'mean_summer_airtemp', 'multiband', 'ls8_coastal_aerosol', 'NN3_3', 'NN3_2', 'NN3_1', 'NN3_4', 'AvgTemperatureColorScaled', 'AverageChloroColorScaled', 'lena', 'Germany_DTM', 'climate_cloud', 'FiLCCoverageBit', 'AverageChloroColor', 'LandsatMultiBand', 'RadianceColorScaled', 'AvgLandTemp', 'NIR', 'BlueMarbleCov']

# Get geo-bounding boxes and native CRS
print(my_wcs.contents['nurc__Arc_Sample'].boundingboxes)
#example:
#[{'nativeSrs': 'http://www.opengis.net/def/crs/EPSG/0/4326', 'bbox': (-90.0, -180.0, 90.0, 180.0)}]

# Get axis labels
print(my_wcs.contents['nurc__Arc_Sample'].grid.axislabels)
#E.g: ['i', 'j']

#
# Get dimension
print(my_wcs.contents['nurc__Arc_Sample'].grid.dimension)

# Get grid lower and upper bounds
print(my_wcs.contents['nurc__Arc_Sample'].grid.lowlimits)
#E.g [0,0]

print(my_wcs.contents['nurc__Arc_Sample'].grid.highlimits)
#['719', '359']

# Get offset vectors for geo axes
print(my_wcs.contents['nurc__Arc_Sample'].grid.offsetvectors)
#[['0.0', '0.5'], ['-0.5', '0.0']]

# For coverage with time axis get the date time values
my_wcs.contents['AverageChlorophyllScaled'].timepositions










