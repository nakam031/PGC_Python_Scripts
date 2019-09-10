import os
import glob
import arcpy

arcpy.CheckOutExtension("Spatial")

mosaicFolderName = raw_input("Name for a new folder to create Mosaic. ")
directory = raw_input("Where do you want to create a new directory? ")
mosaicFolder = os.path.join(directory,mosaicFolderName)

if os.path.exists(mosaicFolder):
	print "Folder name already exists."

else:
	os.makedirs(mosaicFolder)

	rasterDirectory = raw_input("Where is the directory raster files are located? ")

	tifList = glob.glob(rasterDirectory + '/*/*.tif')

	tifFullPath = ";".join(tifList)
	print tifFullPath
	mosaicName = raw_input("Name for the mosaic with extension? ")
	coordinate = ""
	pixelType = "32_BIT_FLOAT"
	cellsize = "5"
	numberBand = "1"
	method = "LAST"
	colorMode = "FIRST"

	if not os.path.exists(os.path.join(mosaicFolder,mosaicName)):
		Mosaic = arcpy.MosaicToNewRaster_management(tifFullPath,mosaicFolder,mosaicName,coordinate,
			pixelType,cellsize,numberBand,method,colorMode)


arcpy.CheckInExtension("Spatial")


