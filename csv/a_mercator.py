import os
import csv
import numpy as np
import matplotlib.pyplot as plt



directory_merc='/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_mercator'


directory_norm='/Users/pedroguillermarnanzcoll/Documents/AI/repo/dataset/1260/1260_normalized'

for filename in os.listdir(directory_norm):
	if filename.endswith(".csv"):
		edificio= filename[:-4]
		#carpeta=os.mkdir(directory_merc+'/'+edificio)
		print(os.path.join(directory_merc, filename))
		with open(directory_norm+'/14.csv',"r+") as file:
			csv_in = csv.reader(file, delimiter=",")
			a=[]
			for indice,row in enumerate(csv_in):
				
				print(indice)
				matriz=np.asarray(row[5:]).reshape(60,21).T.astype(np.float)
					
				plt.axis('off')
				plt.imshow(matriz, interpolation='bilinear')
				plt.savefig(directory_merc+'/'+edificio+'/'+edificio+'_'+str(format(indice,'05d'))+'.png')
				
				#a.append(matriz)
				continue
			#a=np.array(a)
			#np.save(directory_merc+'/'+edificio, a)
			

		continue
	else:
		continue

