'''This script is created to produce sql that could be used in ArcMap.
This is used when PGC users have list of catalog_ID or SCENE_ID request. '''
import os 

fieldname=raw_input("Field name? ")
rawfilepath=raw_input("file path? ")
filepath=os.path.abspath(rawfilepath)
method=raw_input("TYPE: AND, OR? ")
lines=[]
with open(filepath) as f:
        lines=[line.strip()for line in f]
	#line in f:
	    #line = line.strip()
	    #lines.append(line)
mylist=[]	
for l in lines:
	argument="{} = '{}' {}".format(fieldname,l,method)
	mylist.append(argument)

stringlist = " ".join(mylist)
if method =="OR":
        outputarg = stringlist[:-2]
else:
        outputarg = stringlist[:-3]
print outputarg
