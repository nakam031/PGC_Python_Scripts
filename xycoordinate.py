import csv
import numpy as np

myarray = []
filename = 'E:/geocell_deck/shp/geocell_antarctic_xypoint.csv'
#create empty csv file
writefile = open('E:/geocell_deck/shp/geocell_antarctic_xypoint_result.csv','wb')

FID = 0
xmin,ymin = np.inf,np.inf
xmax,ymax = -np.inf, -np.inf
with open(filename) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		#print row
		
		#print int(row["ORIG_FID"])
		
		#print type(float(row["x"]))
		if FID == int(row["FID"]):
			ORIG = int(row["ORIG_FID"])
			#print ORIG
			xmin = min(xmin,float(row["x"]))
			ymin = min(ymin,float(row["y"]))
			xmax = max(xmax,float(row["x"]))
			ymax = max(ymax,float(row["y"]))	
		else:
			#ORIG = int(row["ORIG_FID"])
			myarray.append([ORIG,int(FID), float(xmin), float(ymin), float(xmax), float(ymax)])
			xmin,ymin = float(row["x"]),float(row["y"])
			xmax,ymax = float(row["x"]),float(row["y"])
			FID += 1
	if FID == 122:
		myarray.append([ORIG,int(FID), float(xmin), float(ymin), float(xmax), float(ymax)])
		#print FID
print myarray



with writefile:
	writer = csv.writer(writefile, delimiter=",")
	for line in myarray:
		writer.writerow(line)
	#writer.writeheader()
	#writer.writerows(myarray)
print "writing complete"
