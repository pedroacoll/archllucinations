import csv
import math


filename= '1260/17_a.csv'
filedirec = 'direcciones1260.csv'
with open(filedirec, 'r') as d:
    readerd = csv.reader(d)
    for ind,row in enumerate(readerd):
        print(len(row))
with open(filename, 'r') as f:
    
    reader = csv.reader(f)

      
    for ind,row in enumerate(reader):
        print(len(row))
        if ind == 0:
            distancias=[]
            for indice,column in enumerate(row):
                if indice == 0 : x=float(column)
                elif indice == 1 : y=float(column)
                elif indice == 2 : z=float(column)
                elif indice == 3: continue
                elif indice == 4: continue
                else:
                    distancias.append(float(column))
            print(len(distancias))
        else: break