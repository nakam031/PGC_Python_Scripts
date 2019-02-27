'''This script is to check how many unique CATALOG_ID exist in the order and check if there is any missing.
This script is designed for making the workflow better at the PGC.
'''
import os
rawfilepath=raw_input("file path to the footprint txt? ")
filepath=os.path.abspath(rawfilepath)
lines=[]
with open(filepath) as f:
	lines=[line.strip()for line in f]
unique_ids=set(lines)
print "unique id is ", unique_ids
print "the number of unique id is ", len(unique_ids)
originalfile=raw_input("file path to requested txt? ")
originalfilepath=os.path.abspath(originalfile)
lists=[]
with open(originalfilepath) as f:
	lists=[line.strip()for line in f]
print len(lists)
for l in lists:
	if l not in lines:
		print "missing: ",l
	else:
		pass
