'''This script is to extract the tarfile downloaded from EarthExplorer (USGS). 
This is designed to use for the fast ice project in PGC. 
After using this script, use bandcomp.py to create a rgb images.'''

import tarfile, os, sys

# fname = 
fpath = raw_input("File path? ")
print "getting the list of files in the directory"
flist = os.listdir(fpath)
print flist
ffulllist = []
dnamelist = []
for file in flist:
	fulllist = os.path.join(fpath,file)
	foldername = fulllist[:-7]
	# print fulllist, foldername
	ffulllist.append(fulllist)
	dnamelist.append(foldername)
fcount = 0
for f in ffulllist:
	print "f:" + f
	if not os.path.exists(f[:-7]):
		n = dnamelist[fcount]
		tar = tarfile.open(f)

		tar.extractall(os.path.join(fpath,n))

		tar.close()
		fcount +=1
	else:
		print f + " exists."