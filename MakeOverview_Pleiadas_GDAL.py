import os
import subprocess


blur_dir = r'\\doerian\E\Z057_Wallonia\02_Pleiades\__TEST'



for blur_file in os.listdir(blur_dir):
    if blur_file.endswith('.tif'):
        imagefile = os.path.join(blur_dir,blur_file)
        os.system(r'cmd /c "C:\Program Files\QGIS 2.18\OSGeo4W.bat" gdaladdo --config COMPRESS_OVERVIEW JPEG --config PHOTOMETRIC_OVERVIEW RGB --config INTERLEAVE_OVERVIEW PIXEL -ro {imagefile} 2 4 8 16 32'.format(imagefile = imagefile))

