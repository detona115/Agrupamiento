import pandas as pd
import numpy as np
import math
import sys
import random


def leArquivo(dataset):
	data = []
	data = pd.read_csv("DS/"+dataset+".data")
	return data["A1"].values, data["A2"].values, data["cluster"].values

def centroides(minX, maxX, minY, maxY):
	x = random.uniform(minX, maxX)
	y = random.uniform(minY, maxY)
	return (x,y)

def calculaEuclidiana(C, P):
	distE = pow(C[0] - P[0],2) + pow(C[1] - P[1],2)
	distE = math.sqrt(distE)
	return distE

def menorDistancia(distancias):
	valor = min(distancias)
	posicao = distancias.index(valor)
	return posicao

def novoCentroides(pontos):
	X = 0
	Y = 0
	for tupla in pontos:
		X += tupla[0]
		Y += tupla[1]
	#print X, len(pontos)
	x1 = X / len(pontos)
	y1 = Y / len(pontos)
	return (x1, y1)

#def SSE():
	

if __name__ == '__main__':
	
	SSEi = []
	dataset = sys.argv[1]
	x, y, clusters = leArquivo(dataset)
	totalClusters = clusters[len(clusters)-1]
	#print "\nDados iniciais:\nx: ", x, "\ny: ", y, "\nclusters: ", clusters, "\n"
	#print "Total de Clusters: ", totalClusters, "\n"
	
	# Aplicar o algoritmo 10 vezes
	# informacoes a ser coletadas em cada turno --> Soma do erro quadratico
	# Um turno deve ter no maximo 50 interacoes
	turno = 1
	while turno <= 10:
		turno+=1

		minX = min(x)
		maxX = max(x)
		minY = min(y)
		maxY = max(y)

		# Primeiramente sao gerados 'totalClusters' centroides aleatorios atraves da funcao CENTROIDES, esses serao
		# nossos centroides iniciais.
		#print "Centroides iniciais: "
		centroidesList = []
		i = 0	
		while i < totalClusters:
			centroidesList.append(centroides(minX, maxX, minY, maxY))
			#print "\n", i+1,": ",centroidesList[i] 
			i = i+1
		print "Primeiros Clusters: ", centroidesList
		clusters = np.array(clusters).tolist()	
		while(True):
			interacoes = 1
			finais = []
			clusterFinal = []
			i = 0
			while i < totalClusters:
				finais.append([])
				i += 1
			
			flag = 0
			# Transformando o array numpy em um arrayList normal
			
			clusters_aux = clusters[:]

			for x1, y1 in zip(x,y):
				i = 0
				centroidesDistancesParcial = []

				#print "\n\nDistancias Parciais/Euclidiana do objeto (",x1,",",y1,"):"
				while i < totalClusters:
					centroidesDistancesParcial.append(calculaEuclidiana(centroidesList[i], (x1,y1)))
					#print "Centroide ", centroidesList[i], " eh ", centroidesDistancesParcial[i]
					i = i + 1
				posicao = menorDistancia(centroidesDistancesParcial) 
				clusters[flag] = posicao + 1
				flag = flag + 1
				finais[posicao].append((x1,y1))
				#print "A menor distancia foi com o centroide ", posicao+1
			
			#print "\nClusters Antigos:", clusters_aux," \nClusters Novos: ", clusters
			#for f in finais:
				#print "Objetos mudaram de cluster ou nao: ", f

			if clusters != clusters_aux and interacoes <= 50:
				interacoes = interacoes+1
				centroidesList = []
				i = 0 
				while i < totalClusters:
					centroidesList.append(novoCentroides(finais[i]))
					i = i + 1
			else:
				break
				#exit(0)
			#exit(0)

		#SSE()
		SSEparcial = 0
		i=0
		print "\nCluster Final: ", centroidesList, "\n"
		
		for c in centroidesList:
			for fi in finais[i]:
				#print "fi: ", fi
				#print "c: ", c 
				
				SSEparcial += pow(calculaEuclidiana(c, fi),2)
				
			i += 1
			#print "SSEparcial", SSEparcial
		SSEi.append(SSEparcial)
		print "SSEi", SSEi

	media = 0
	for sse in SSEi:
		media = sse + media
	media = media / 10

	soma = 0
	for aP in SSEi:
		soma += math.pow((aP - media),2)
	desvioPadrao = math.sqrt(soma / float(len(SSEi)))
	
	with open("Valores/"+dataset+".txt", "w") as acu:
		acu.write('SSEi: '+str(SSEi)+'\
			\n\'Media: '+str(media)+'\
				\n\nDesvio Padrao: '+str(desvioPadrao))

	with open("Dataset/artificial2_novo.data","w") as acu:
		acu.write('A1,A2,cluster\n')
		for x1, y1,c in zip(x,y,clusters):
			acu.write(str(x1)+','+str(y1)+','+str(c)+'\n')

				
			