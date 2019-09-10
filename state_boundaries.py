import arcpy
import os

arcpy.env.overwriteOutput = True

shp = "G:/world/tl_2017_us_state_wgs.shp"

arcpy.MakeFeatureLayer_management(shp,"state_lyr")

directory = "G:/world/states"

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
		affili = row[7].replace(" ","")
		arcpy.SelectLayerByAttribute_management("state_lyr", "NEW_SELECTION", '"FID" = ' + str(fid))
		outname = row[8].replace(" ", "")
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
		arcpy.CopyFeatures_management('state_lyr', outSelect)
		arcpy.Erase_analysis(inCover, "state_lyr", outCover,"")
