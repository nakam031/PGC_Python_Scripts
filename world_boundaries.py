import arcpy
import os

arcpy.env.overwriteOutput = True

shp = "G:/world/world_west.shp"

arcpy.MakeFeatureLayer_management(shp,"worldsub_lyr")

directory = "G:/world/shp"

fields = arcpy.ListFields(shp)
field_name = []
for f in fields:
	field_name.append(f.name)
print field_name
# fields = ['OID@','ISO_2DIGIT','ISO_3DIGIT','NAME','LONG_NAME','SHAPE@']

# shpcursor = arcpy.SearchCursor(shp)

inCover = "G:/world/AOI_west.shp"
with arcpy.da.SearchCursor(shp,field_name) as cursor:
	for row in cursor:
		fid = row[0]
		affili = row[8].replace(" ","")
		arcpy.SelectLayerByAttribute_management("worldsub_lyr", "NEW_SELECTION", '"FID" = ' + str(fid))
		outname = row[5].replace(" ", "")
		outDirectory = os.path.join(directory,affili)

		if os.path.exists(outDirectory):
			pass
		else:
			os.makedirs(outDirectory)

		outSelect = os.path.join(outDirectory, outname + ".shp")
		print "outSelect = " + outSelect
		outCover = os.path.join(outDirectory, outname + "Inv.shp")
		print "outCover = " + outCover
		featureType = "POLY"
		arcpy.CopyFeatures_management('worldsub_lyr', outSelect)
		arcpy.Erase_analysis(inCover, "worldsub_lyr", outCover,"")
