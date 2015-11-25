import random
import math
import matplotlib.pyplot as plt
from pylab import cm, imshow, colorbar, show
import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
from scipy import interpolate
import scipy.interpolate as inter
import numpy as np
import pylab as plt
from numpy.random import normal
from scipy.optimize import curve_fit



def umaDimensao():
	caminhante = []
	desvio_do_caminhante =[]
	t = []
	temp = 100
	last_walk = []

	for j in range(temp):
		t.append(math.sqrt(j))

	for j in range(200):
		position = []
		position.append(0)	#position start from 0

		for i in range(temp):	#numbers of interations
			x = random.randint(0,1)
			if x==0:
				x=-1.0
			else:
				x=1.0
			position.append(position[-1] + x)	#increment position

		caminhante.append(position)
		last_walk.append(position[-1])

	for j in range(len(caminhante[0])):
		amostra = []
		for z in range(len(caminhante)):
			amostra.append(caminhante[z][j])	
		desvio_do_caminhante.append(desvio_padrao(amostra))	


	
	gaussian_numbers = normal(size=1000)
	plt.hist(last_walk)
	plt.title("Caminhante Aleatrio")
	plt.xlabel("Posicao")
	plt.ylabel("Quantidade de caminhantes")
	plt.show()	

	plt.title("Desvio Padrao dos caminhantes")
	plt.xlabel("tempo")
	plt.ylabel("Desvio padrao")
	plt.plot(desvio_do_caminhante)	#prepare plot
	plt.plot(t)
	plt.show()	#show plot


def duasDimensoes():
	num_caminhantes = 1000
	tempo = 100
	last_walk_distance = []


	tp = []
	for j in range(tempo):
		tp.append(math.sqrt(j))

	caminhante_x = []
	caminhante_y = []

	for n in range(num_caminhantes):
		positionX = []
		positionY = []
		positionX.append(0)
		positionY.append(0)	
		for t in range(tempo):	#numbers of interations
			x = random.randint(0,2)
			y = random.randint(0,2)
			while(x == 0 and y == 0):
				x = random.randint(0,2)
				y = random.randint(0,2)
			if x == 2:
				x = -1.0
			if y == 2:		
				y = -1.0
			y = float(y)
			x = float(x)	
			positionX.append(positionX[-1] + x)
			positionY.append(positionY[-1] + y)	

		caminhante_x.append(positionX)
		caminhante_y.append(positionY)	
		last_walk_distance.append( math.sqrt(positionX[-1]**2 + positionY[-1]**2) )

	plt.hist(last_walk_distance)
	plt.title("Caminhante Aleatrio")
	plt.xlabel("Distancia")
	plt.ylabel("Quantidade de caminhantes")
	plt.show()		

	desvio_do_caminhante = []
	for j in range(tempo):
		amostra_x = []
		amostra_y = []
		for z in range(num_caminhantes):
			amostra_x.append(caminhante_x[z][j]) 
			amostra_y.append(caminhante_y[z][j]) 
		desvio_do_caminhante.append(desvio_padrao(amostra_x)) # APENAS CALCULANDO PARA X  ( NEED TO CHANGE ) !!!!!!!!!!!!!!!!!!!!!!!!

	#GRAFICO DA LOUCURA---------------------------------------------------
	minX = 0
	minY = 0
	maxX = 0
	maxY = 0
	for i in range(num_caminhantes):
		if (minX>min(caminhante_x[i])):
			minX = min(caminhante_x[i])
		if (minY>min(caminhante_y[i])):
			minY = min(caminhante_y[i])
		if (maxX<max(caminhante_x[i])):
			maxX = max(caminhante_x[i])
		if (maxY<max(caminhante_y[i])):
			maxY = max(caminhante_y[i])

	matrix = [[0 for x in range(int(abs(maxX))+int(abs(minX))+1)] for y in range(int(abs(maxY))+int(abs(minY))+1)]
	for i in range(num_caminhantes):
		for t in range(tempo):

			matrix[int(int(abs(minY))+caminhante_y[i][t])][int(int(abs(minX))+caminhante_x[i][t])] += 1	
	#---------------------------------------------------------------------------------------------
	
	plt.title("Desvio Padrao dos caminhantes")
	plt.xlabel("tempo")
	plt.ylabel("Desvio padrao")
	plt.plot(desvio_do_caminhante)	#prepare plot
	plt.plot(tp)
	plt.show()	#show plot

	#COLOR MAP
	cmap = cm.jet
	cmap.set_bad('w')
	im = imshow(matrix, cmap=cmap, interpolation='nearest')
	colorbar()
	show()	

def variancia(x):
	return pow(desvio_padrao(x),2)

def media(x):
	return sum(x)/len(x)

def desvio_padrao(x):
	soma = 0
	media_x = media(x)
	for i in range(len(x)):
		soma += (x[i] - media_x)**2
	return math.sqrt(soma/(len(x)))


def raio_gota():
	x1 = []
	y1 = [0.0, 4.86145310969863, 7.9622103949172285, 10.318877638434742, 12.279599156048462, 14.004704563355219, 15.30134774432635, 16.881628115741066, 17.742845371250354, 18.157515625751387, 19.149235447234418, 19.943364081042446, 20.673835708371385, 21.485613609689835, 22.109636622936847, 22.658230422829476, 23.135058014571882, 23.13827966117315]

	x1.append(0)
	for i in range(17):
		x1.append(x1[-1] + 3.722222)

	y = np.array(y1)	
	x = np.array(x1)
	z = np.polyfit(x, y, 3)
	p = np.poly1d(z)
	xp = np.linspace(-1, x1[-1], 1000)
	plt.yscale('linear')
	_ = plt.plot(x, y, '.', xp, p(xp), '-')
	plt.title("Experimento da gota")
	plt.xlabel("tempo")
	plt.ylabel("Raio da gota")

	plt.show()



def main():
	#umaDimensao()
	duasDimensoes()
	#raio_gota()
	#caminhate1D_ciro()
	

main()
