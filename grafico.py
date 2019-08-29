import pandas as pd
import matplotlib.pyplot as plt
import sys

def leArquivo(dataset):
	data = []
	data = pd.read_csv("Dataset/"+dataset+".data")
	return data["A1"].values, data["A2"].values, data["cluster"].values

if __name__ == '__main__':
	

	dataset = sys.argv[1]
	x,y,clusters = leArquivo(dataset)

	tamanho = len(x)

	print tamanho
	x1 = []
	y1 = []
	x2 = []
	y2 = []
	x3 = []
	y3 = []
	x4 = []
	y4 = []
	x5 = []
	y5 = []
	x6 = []
	y6 = []
	x7 = []
	y7 = []
	x8 = []
	y8 = []
	x9 = []
	y9 = []
	x10 = []
	y10 = []

	for i in range(tamanho):
		if clusters[i] == 1:
			x1.append(x[i])
			y1.append(y[i])
		if clusters[i] == 2:
			x2.append(x[i])
			y2.append(y[i])
		if clusters[i] == 3:
			x3.append(x[i])
			y3.append(y[i])
		if clusters[i] == 4:
			x4.append(x[i])
			y4.append(y[i])
		if clusters[i] == 5:
			x5.append(x[i])
			y5.append(y[i])
		if clusters[i] == 6:
			x6.append(x[i])
			y6.append(y[i])
		if clusters[i] == 7:
			x7.append(x[i])
			y7.append(y[i])
		if clusters[i] == 8:
			x8.append(x[i])
			y8.append(y[i])
		if clusters[i] == 9:
			x9.append(x[i])
			y9.append(y[i])
		if clusters[i] == 10:
			x10.append(x[i])
			y10.append(y[i])

	plt.scatter(x1,y1,label="Cluster 1",color="red")
	plt.scatter(x2,y2,label="Cluster 2",color="green")
	plt.scatter(x3,y3,label="Cluster 3",color="blue")
	plt.scatter(x4,y4,label="Cluster 4",color="yellow")
	plt.scatter(x5,y5,label="Cluster 5",color="magenta")
	plt.scatter(x6,y6,label="Cluster 6",color="purple")
	plt.scatter(x7,y7,label="Cluster 7",color="cyan")
	plt.scatter(x8,y8,label="Cluster 8",color="orange")
	plt.scatter(x9,y9,label="Cluster 9",color="black")
	plt.scatter(x10,y10,label="Cluster 10",color="gray")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Dataset')
	plt.legend(loc='lower right', prop={'size':8})
	plt.show()