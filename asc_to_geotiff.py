import numpy, os
import osr, gdal
import pdb
from os import listdir
from os.path import isfile, join

path = './data'

from os import walk

paths = []
for (dirpath, dirnames, filenames) in walk(path):
    for f in filenames:
        if f[-3:] == 'asc':
            paths.append(os.path.join(dirpath, f))

for p in paths:
    drv = gdal.GetDriverByName('GTiff')
    ds_in = gdal.Open(p)

    # geotiff_path = p.replace('./data', './geotiffs').replace('.asc', '.tif')
    geotiff_path = p.replace('.asc', '.tif')
    ds_out = drv.CreateCopy(geotiff_path, ds_in)
    srs = osr.SpatialReference()
    srs.ImportFromEPSG(4326)
    ds_out.SetProjection(srs.ExportToWkt())
    ds_in = None
    ds_out = None
