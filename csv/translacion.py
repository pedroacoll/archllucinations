import os
import csv

directory= '/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260'
directory_trans='/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_translated'
xmaxglobal=0
ymaxglobal=0
zmaxglobal=0
xminglobal=0
yminglobal=0
zminglobal=0
for filename in os.listdir(directory):
	if filename.endswith(".csv"): 
		print(os.path.join(directory, filename))
		x,y,z=0,0,0
		with open(directory+'/'+filename,"r+") as file:

			csv_in = csv.reader(file, delimiter=",")
			with open(directory_trans+'/'+filename,"w") as file_out: 
				csv_out = csv.writer(file_out, delimiter=",")
				for index, row in enumerate(csv_in):
					if index == 0:
						coordenadas = row[0].split(",") 
						
						x= float(coordenadas[0])
						y=float(coordenadas[1])
						z=float(coordenadas[2])

						csv_out.writerow([0,0,0]+row[1:])
					else:
						print(index)
						coordenadasn = row[0].split(",") 
						xn= float(coordenadasn[0])-x
						yn=float(coordenadasn[1])-y
						zn=float(coordenadasn[2])-z 
						if xn>xmaxglobal: xmaxglobal=xn
						if yn>ymaxglobal: ymaxglobal=yn
						if zn>zmaxglobal: zmaxglobal=zn	
						if xn<xminglobal: xminglobal=xn
						if yn<yminglobal: yminglobal=yn
						if zn<zminglobal: zminglobal=zn										
						csv_out.writerow([xn,yn,zn] + row[1:])

				"""print(x,y,z)	"""
		continue
	else:
		continue
with open(directory_trans+'/maximos.csv',"w") as file_max:
	csvmax_out = csv.writer(file_max, delimiter=",")
	csvmax_out.writerow([xmaxglobal,ymaxglobal,zmaxglobal])
	csvmax_out.writerow([xminglobal,yminglobal,zminglobal])
