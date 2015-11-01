import random
import math
import matplotlib.pyplot as plt

def media(x):
	return sum(x)/len(x)

def desvio_padrao(x):
	soma = 0
	media_x = media(x)
	for i in range(len(x)):
		soma += (x[i] - media_x)**2
	return math.sqrt(soma/(len(x)))

def main():
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
	return 0

main()
