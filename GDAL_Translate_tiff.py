import os
import subprocess


input_folder = r'D:\temp\StereoImagery\01_TIFF'
output_folder = r'D:\temp\StereoImagery\02_JEPG'

osgeo_path = r'C:\Program Files\QGIS 2.18\OSGeo4W.bat'

for input_file in os.listdir(input_folder):
    if input_file.endswith('.tif') :
        imagefile = os.path.join(input_folder,input_file)
        output_imagefile = os.path.join(output_folder,input_file.replace('.tif','.jpg'))
        if not os.path.exists(output_imagefile):
#            os.system(r'cmd /c "C:\Program Files\QGIS 2.18\OSGeo4W.bat" gdal_translate {inputfile} {outputfile}'.format(inputfile = imagefile,outputfile = output_imagefile))
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            process = subprocess.Popen([osgeo_path,'gdal_translate',imagefile, output_imagefile], stdout=subprocess.PIPE, startupinfo=startupinfo)
            while True:
                output = process.stdout.readline()
                if output == b'':
                    break
                print (output)
