###This code is to create RGB band imagery from Landsat 7 data downloaded from USGS Earth Explorer.
###Also, with the user's preference, it will mosaic the imagery created with this code.
import os
import arcpy
arcpy.CheckOutExtension("Spatial")
##1. Type in the new folder name for 3 band imagery, and the file path where you want the new folder to be located
compFolderName = raw_input("Name for a new folder for rgb band. ")
directory = raw_input("Where do you want to create a new directory? ")
compFolder = os.path.join(directory,compFolderName)
if os.path.exists(compFolder):
    print "Folder name already exists."
else:
    os.makedirs(compFolder)

    ##2. main leads to the folder all the imagery are stored. Type in the folder path until 'L7 ETM_ C1 Level-1' folder
    main = raw_input("Directory where raw images are located. ")
    #get the list of what's in the main directory
    mainfiles = os.listdir(main)
    print mainfiles
    #create an empty list to store all the file paths to the imagery
    mainlist =[]
    #create an empty list so that later in the process it can store
    #red, green, blue band imagery
    comp=[]
    #get the folder path which leads to individual imagery folders
    for f in mainfiles:
        #if it is a folder.
        if not f.endswith("tar.gz") and f != compFolderName:
            #fSub = f[:-4]
            fpath = os.path.join(main,f)
            #append the file path to the list
            mainlist.append(fpath)
        #if it is not a folder.
        else:
            print "not a directory"
            pass
    #print mainlist
    #open the folder in the mainlist, and obtain blue, red, green band imagery path.
    for i in mainlist:
        #print i
        bname = i[-40:]
        subfiles = os.listdir(i)
        for s in subfiles:
            if s == bname+'_B1.TIF':
                blue = os.path.join(i,s)

            elif s == bname+'_B2.TIF':
                green = os.path.join(i,s)

            elif s == bname+'_B3.TIF':
                red = os.path.join(i,s)

            else:
                pass
        ##3. specify the name of the RGB band imagery
        outname = "compband.tif"
        outpath = compFolder+'/'+bname+outname
        comp.append(outpath)
        #if the imagery does not exist, create a 3 band imagery.
        if not os.path.exists(outpath):
            
            arcpy.CompositeBands_management(blue+';'+green+';'+red,outpath)
            #in each band, make 0 to NoData
            outRas = arcpy.SetRasterProperties_management(outpath,"GENERIC","","",[["1",0],["2",0],["3",0]])

###MOSAIC process, comment out the following codes if you do not want to create mosaic.
    ##4. Type in the new folder name for mosaic imagery, and the file path where you want the new folder to be located
    mosaicFolderName = "mosaic"
    MosaicFolder = os.path.join(directory,mosaicFolderName)
    #if the folder name does not exist, create new folder and keep going.
    if os.path.exists(MosaicFolder):
        print "Folder name already exists."
    else:
        os.makedirs(MosaicFolder)
        ##5. type in the parameters for mosaic
        compMosaic = ";".join(comp)
        print compMosaic
        mosaicName = "MosaicComp.tif"
        coordinate = ""
        pixelType = "16_BIT_UNSIGNED"
        cellSize = "30"
        numberBand = "3"
        method = "MEAN"
        colorMode = "MATCH"

        if not os.path.exists(os.path.join(MosaicFolder,mosaicName)):
            Mosaic = arcpy.MosaicToNewRaster_management(compMosaic,MosaicFolder,mosaicName,coordinate,pixelType,
                                                    cellSize,numberBand,method,colorMode)
arcpy.CheckInExtension("Spatial")
