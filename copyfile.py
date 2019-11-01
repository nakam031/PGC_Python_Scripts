#This script allows you to look for files and copy them to a different directory.
#create a text file that contains file names without an extention
# eg) file name: 15_44_1_1_2m_v3.0_reg_dem
#

import os
import shutil


rootFolder = raw_input("path to the root folder: ")

extention = raw_input("Look for files that end with (like .txt): ")

txtFile = raw_input("path to the text folder with file names: ")

outputDir = raw_input("Path where you want to copy data: ")
fullPathList = []
with open(txtFile) as txtF:
	for f in txtF:
		tileFolder = f[0:5]
		if f.endswith('\n'):
			path = os.path.join(rootFolder, tileFolder, f[:-1])
			fileName = f[:-1] + extention
		else:
			path = os.path.join(rootFolder, tileFolder, f)
			fileName = f + extention
		
		fullPath = path + extention
		
		fullPathList.append(fileName)
		if os.path.isfile(fullPath):
			if os.path.exists(os.path.join(outputDir, fileName)):
				print fileName + " exists"
			else:
				shutil.copy(fullPath, outputDir)
				print fileName + " copied"
print fullPathList
