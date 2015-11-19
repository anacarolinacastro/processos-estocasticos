from PIL import Image
from math import sqrt, pi
import scipy
# import matplotlib.pyplot as plt

raios = []


def getBlack(arq):
	im = Image.open(arq)

	pixels = im.getdata()          # pega os pixels
	pretoAceitavel = (50,50,50)
	n = 0 # nmero de pixels pretos
	for pixel in pixels:
	    if pixel < pretoAceitavel:
	        n += 1

	r = sqrt(n/pi)
	return r

for i in range(18):
	string = "imgs/1/out{}.png".format(i+1)
	raio = getBlack(string)
	if i == 0:
		raioO = raio
	raios.append(raio-raioO)


print(raios)