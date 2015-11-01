import random
import math
import matplotlib.pyplot as plt
from pylab import cm, imshow, colorbar, show

def umaDimensao():
	caminhante = []
	desvio_do_caminhante =[]
	t = []

	for j in range(1000):
		t.append(math.sqrt(j))

	for j in range(200):
		position = []
		position.append(0)	#position start from 0

		for i in range(1000):	#numbers of interations
			x = random.randint(0,1)
			if x==0:
				x=-1.0
			else:
				x=1.0
			position.append(position[-1] + x)	#increment position

		caminhante.append(position)

	for j in range(len(caminhante[0])):
		amostra = []
		for z in range(len(caminhante)):
			amostra.append(caminhante[z][j])	
		desvio_do_caminhante.append(desvio_padrao(amostra))	

	plt.plot(desvio_do_caminhante)	#prepare plot
	plt.plot(t)
	plt.show()	#show plot


def duasDimensoes():
	num_caminhantes = 1000
	tempo = 1000

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
			x = random.randint(0,1)
			y = random.randint(0,1)
			while(x == 0 and y == 0):
				x = random.randint(0,1)
				y = random.randint(0,1)
			if x == 0:
				x = -1.0
			else:
				x = 1.0
			if y == 0:
				y = -1.0
			else:
				y = 1.0	
			positionX.append(positionX[-1] + x)
			positionY.append(positionY[-1] + y)		
		caminhante_x.append(positionX)
		caminhante_y.append(positionY)	

	desvio_do_caminhante = []
	for j in range(tempo):
		amostra_x = []
		amostra_y = []
		for z in range(num_caminhantes):
			amostra_x.append(caminhante_x[z][j]) 
			amostra_y.append(caminhante_y[z][j]) 	
		desvio_do_caminhante.append(desvio_padrao(amostra_x)) # APENAS CALCULANDO PARA X

	plt.plot(desvio_do_caminhante)	#prepare plot
	plt.plot(tp)
	plt.show()	#show plot

	# # colormap
	# cmap = cm.jet
	# cmap.set_bad('w')
	# im = imshow(matrix, cmap=cmap, interpolation='nearest')
	# colorbar()
	# show()

def media(x):
	return sum(x)/len(x)

def desvio_padrao(x):
	soma = 0
	media_x = media(x)
	for i in range(len(x)):
		soma += (x[i] - media_x)**2
	return math.sqrt(soma/(len(x)))

def caminhate1D_ciro():
	caminhante = []
	desvio_do_caminhante =[]
	t = []

	for j in range(1000):     #time increment
		t.append(math.sqrt(j))

	for j in range(200):
		position = []
		position.append(0)	#position start from 0

		for i in range(1000):	#numbers of interations
			x = random.randint(0,1)
			if x==0:
				x=-1.0
			else:
				x=1.0
			position.append(position[-1] + x)	#increment position

		caminhante.append(position)	#put positions in caminhante

	for j in range(len(caminhante[0])):
		amostra = []
		for z in range(len(caminhante)):
			amostra.append(caminhante[z][j])	
		desvio_do_caminhante.append(desvio_padrao(amostra))	

	plt.plot(desvio_do_caminhante)	#prepare plot
	plt.plot(t)
	plt.show()	#show plot

def main():
	#umaDimensao()
	duasDimensoes()
	

main()
