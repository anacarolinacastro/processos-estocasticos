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
	amostras = 1000
	tempo = 100

	desvio_do_caminhante =[]
	tp = []

	for j in range(tempo):
		tp.append(math.sqrt(j))

	matrixX = []
	matrixY = []
	matrix = []

	for n in range(amostras):
		positionX = []
		positionX.append(0)
		positionY = []
		positionY.append(0)	
		for t in range(tempo):	#numbers of interations
			caso = random.randint(0,1)
			if caso == 0:
				# anda em uma dimensao
				dimensao = random.randint(0,1)
				if dimensao == 0:
					# caminhante move em x
					x = random.randint(0,1)
					if x == 0:
						x = -1.0
					else:
						x = 1.0
					positionX.append(positionX[-1] + x)	#increment position
					positionY.append(positionY[-1]) # keep last result

				else:
					# caminhante move em y
					y = random.randint(0,1)
					if y == 0:
						y = -1.0
					else:
						y = 1.0
					positionY.append(positionY[-1] + y)	#increment position
					positionX.append(positionX[-1]) # keep last result
			else:
				# anda nas duas dimensoes
				x = random.randint(0,1)
				if x == 0:
					x = -1.0
				else:
					x = 1.0
				positionX.append(positionX[-1] + x)	#increment position

				y = random.randint(0,1)
				if y == 0:
					y = -1.0
				else:
					y = 1.0
				positionY.append(positionY[-1] + y)	#increment position
		matrixX.append(positionX)
		matrixY.append(positionY)

	minX = 0
	minY = 0
	maxX = 0
	maxY = 0
	for i in range(len(matrixX)):
		if (minX>min(matrixX[i])):
			minX = min(matrixX[i])
		if (minY>min(matrixY[i])):
			minY = min(matrixY[i])
		if (maxX<max(matrixX[i])):
			maxX = max(matrixX[i])
		if (maxY<max(matrixY[i])):
			maxY = max(matrixY[i])

	matrix = [[0 for x in range(int(abs(maxX))+int(abs(minX))+1)] for y in range(int(abs(maxY))+int(abs(minY))+1)]
	for i in range(amostras):
		for t in range(tempo):
			matrix[int(int(abs(minY))+matrixY[i][t])][int(int(abs(minX))+matrixX[i][t])] += 1

	for j in range(len(matrix[0])):
		amostra = []
		amostra2 = []
		for z in range(len(matrixX)):
			amostra.append(matrixX[z][j])	
			amostra2.append(matrixY[z][j])	
			# amostra.append(math.sqrt(pow(matrixX[z][j],2)+pow(matrixY[z][j],2)))	
		desvio_do_caminhante.append(math.sqrt(pow(desvio_padrao(amostra),2)+pow(desvio_padrao(amostra2),2)))	
		# desvio_do_caminhante.append(math.sqrt(pow(desvio_padrao(amostra),2)+pow(desvio_padrao(amostra2),2)))	
		# desvio_do_caminhante.append(desvio_padrao(amostra))	

	plt.plot(desvio_do_caminhante)	#prepare plot
	plt.plot(tp)
	plt.show()	#show plot

	# colormap
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

def caminhate1D_ciro():
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

def main():
	# umaDimensao()
	duasDimensoes()
	

main()
