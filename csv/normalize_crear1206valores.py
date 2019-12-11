 import os
import csv


directory_norm='/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_normalized'
directory_trans='/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_translated'
xmaxglobal=0
ymaxglobal=0
zmaxglobal=0
xminglobal=0
yminglobal=0
zminglobal=0
with open(directory_trans+'/maximos.csv',"r") as file_max:
	csvmax= csv.reader(file_max, delimiter=",")
	for index, row in enumerate(csvmax):
		if index==0:
			xmaxglobal=float(row[0])
			ymaxglobal=float(row[1])
			zmaxglobal=float(row[2])
		if index==1:
			xminglobal=float(row[0])
			yminglobal=float(row[1])
			zminglobal=float(row[2])
print(xmaxglobal,ymaxglobal,zmaxglobal)
print(xminglobal,yminglobal,zminglobal)

for filename in os.listdir(directory_trans):
	if filename.endswith(".csv"):
		if filename != "maximos.csv": 
			print(os.path.join(directory_trans, filename))
			with open(directory_trans+'/'+filename,"r+") as file:

				csv_in = csv.reader(file, delimiter=",")
				with open(directory_norm+'/'+filename,"w") as file_out: 
					csv_out = csv.writer(file_out, delimiter=",")
					for row in csv_in:
						x= 2*((float(row[0])-xminglobal)/(xmaxglobal-xminglobal))-1
						y= 2*((float(row[1])-yminglobal)/(ymaxglobal-yminglobal))-1
						z= 2*((float(row[2])-zminglobal)/(zmaxglobal-zminglobal))-1
						print(row[4])
						csv_out.writerow([x,y,z]+row[3:6] + row[5:])
					
		continue
	else:
		continue

