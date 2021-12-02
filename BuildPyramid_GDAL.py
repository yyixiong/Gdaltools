# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:46:04 2021

@author: yi
"""
from osgeo import gdal

def Build_Pyramid_GDAL(input_image, method = 0): # 0 = read-only, building external pyramid (recommand), 1 = read-write. building internal pyramid
    """
    Building pyramid using GDAL
    """
    
    Image = gdal.Open(input_image, method) 
    nr_of_bands = Image.RasterCount
    
    if nr_of_bands == 3:
        gdal.SetConfigOption('PHOTOMETRIC_OVERVIEW', 'YCBCR')
        gdal.SetConfigOption('COMPRESS_OVERVIEW', 'JPEG')
    else:
        gdal.SetConfigOption('PHOTOMETRIC_OVERVIEW', '')
        gdal.SetConfigOption('COMPRESS_OVERVIEW', '')
   
    gdal.SetConfigOption('INTERLEAVE_OVERVIEW', 'PIXEL') 
    Image.BuildOverviews("average", [2,4,8,16,32])
    del Image
    print('pyramid created...')
    
    
if __name__ == '__main__': 
    image_list = [r"d:\mytif.tif"]
    for InputImage in image_list:
        Build_Pyramid_GDAL(InputImage)
