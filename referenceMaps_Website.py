# Created by Hitomi Nakamura (PGC) for producing a txt file for tamcamp.org reference Maps' section.

'''This script will create a .txt file that contains reference map's name, scale, author and map links in html format.
Input table has to be csv file.
CMD needs pandas and numpy modules to be able to run
Once .txt file is created, open the file. Then copy and paste the text to the tamcamp website by following: Maps, data & imagery > Edit > Switch to plain text editor'''

import pandas as pd, numpy as np, os

filePath = raw_input("What is the file path to the csv file? ")

data = pd.read_csv(filePath, skiprows = 1)
df = data.replace(np.nan, '', regex=True)
contentLs = []

# This will divide whether the row in csv file has map links (publicly available) or not (restricted access data)
for index, row in df.iterrows():
    mapTitle = row['Map Title']
    mapScale = "1:" + str(row['Map Scale'])
    mapAuthor = "(" + row['Map Author'] + ")"
    target = '"' + "_blank" + '"'
    firstLine = "<p>{mapTitle}: {mapScale} {mapAuthor}</p>".format(mapTitle=mapTitle, mapScale=mapScale, mapAuthor=mapAuthor)
    
    if row['GeoTIFF link'] == '':
        catalogID = '"' + str(row['PGC Map Catalog ID']) + '"'
        contact = '"https://www.pgc.umn.edu/about/findus/"'
        secondLineB = "<p>This map is available upon request. Visit <a href={catalogID} target={target}>Map Details</a> to request the map. Please <a href={contact} target={target}>contact the PGC</a> if you have any questions.</p>".format(catalogID=catalogID, contact=contact, target=target)

        fullContentB = firstLine + secondLineB
        contentLs.append(fullContentB)
    else:
        
        geoTiff = '"' + row['GeoTIFF link'] + '"'
        tiff = '"' + row['TIFF link'] + '"'
        pdf = '"' + row['PDF Link'] + '"'
        jpeg = '"' + row['Preview JPEG link'] + '"'
        

        secondLineA = "<p><a href={geoTiff} target={target}>GeoTIFF</a> &nbsp;|&nbsp;<a href={tiff} target={target}>TIFF</a> &nbsp;|&nbsp;<a href={pdf} target={target}>PDF</a> &nbsp;|&nbsp;<a href={jpeg} target={target}>Preview JPEG</a>".format(geoTiff=geoTiff, tiff=tiff, pdf=pdf, jpeg=jpeg, target=target)

        fullContentA = firstLine + secondLineA
        contentLs.append(fullContentA)

# print contentLs

savePath = raw_input("Where to save the text file? ")
fileName = raw_input("Name the file with .txt extention: ")
save = os.path.join(savePath, fileName)

np.savetxt(save, np.asarray(contentLs), delimiter=',', fmt="%s")