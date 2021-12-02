# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:05:41 2020

@author: yi
"""
import ogr, gdal, os, osr

def gdal_polygonize(in_image,out_shp,band=1):
    ''' uses gdal to polyognize a raster:
        in_image: path to raster to be polygonized
        out_shp: path of output shapefile
        band: band number that has to be polygonized
        '''
       
    #assertions    
    print(out_shp)
    assert os.path.exists(in_image), '<in_image> does not exist!'
    out_dir = os.path.dirname(os.path.abspath(out_shp))
    assert os.path.exists(out_dir), '<out_shp> directory does not exist!'

    # open input image
    ds_in = gdal.Open(in_image)
    gt = ds_in.GetGeoTransform()

    
    assert type(ds_in) != type(None), '<in_file> {} not recognised by GDAL!'.format(in_image)
    band_in = ds_in.GetRasterBand(band)
    srs = osr.SpatialReference()
    srs.ImportFromWkt(ds_in.GetProjectionRef())
    assert type(band_in) != type(None), 'Could not find <band>number in <in_file>'

    # ini out_shp
    driver = ogr.GetDriverByName('ESRI Shapefile')
    ds_out = driver.CreateDataSource(out_shp)
    lyr_out = ds_out.CreateLayer('',srs)
    


    # perform polygonization
    gdal.Polygonize(band_in,band_in,lyr_out,-1,[],callback=None)


    
   

    # clear
    ds_out.Destroy()
    ds_in = None
    
    #ensure output is polygon (sometimes it is linestring for some reason, this is a porblem)
    #out_ds = ogr.Open(out_shp, 1) 
    #out_lyr = out_ds.GetLayer(0)
    #assert out_lyr.GetGeomType() != ogr.wkbLineString, 'outlayer, is linestring, not a polygon'
    #out_ds = None
    


    return


gdal_polygonize()