import os
import csv


directory='/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_normalized'


for filename in os.listdir(directory):
	if filename.endswith(".csv"):
		if filename != "maximos.csv":
			edificio=filename[:-4]
			print(edificio)
			carpeta=os.mkdir(directory+'/'+edificio)
			
			with open(directory+'/'+filename,"r+") as file:
				edificio
				csv_in = csv.reader(file, delimiter=",")
				print(directory+'/'+edificio+'/'+edificio+'_puntos.csv')
				
				with open('/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_divided/1260_puntos/'+edificio+'_puntos.csv',"w") as file_puntos, open('/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_divided/1260_distancias/'+edificio+'_distancias.csv',"w") as file_direcciones: 
					csv_puntos = csv.writer(file_puntos, delimiter=",")
					csv_direc=csv.writer(file_direcciones, delimiter=",")
					for row in csv_in:
						csv_puntos.writerow((row[0],row[1],row[2],row[4]))
						csv_direc.writerow(row[5:])
		continue
	else:
		continue

