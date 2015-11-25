import random

largura = 5
altura = 5
t = 2

spins = [[2*random.randint(0,1)-1 for i in range(altura)] for j in range(largura)] # cria a matriz de spins com -1 ou 1

def hamiltonianaLocal(i,j):
	resultado = 0
	self = spins[i][j]

	if (j == 0):
		vizinhoEsqu = spins[i][-1]
		vizinhoDir = spins[i][j+1]
	elif (j == largura-1):
		vizinhoEsqu = spins[i][j-1]
		vizinhoDir = spins[i][0]
	else:
		vizinhoEsqu = spins[i][j-1]
		vizinhoDir = spins[i][j+1]

	if (i == 0):
		vizinhoCima = spins[-1][j]
		vizinhoBaixo = spins[i+1][j]
	elif (i == altura-1):
		vizinhoCima = spins[i-1][j]
		vizinhoBaixo = spins[0][j]
	else:
		vizinhoCima = spins[i-1][j]
		vizinhoBaixo = spins[i+1][j]

	resultado += -1*self*vizinhoEsqu
	resultado += -1*self*vizinhoDir
	resultado += -1*self*vizinhoCima
	resultado += -1*self*vizinhoBaixo

	# resultado2 = 0
	# resultado2 += self*vizinhoEsqu
	# resultado2 += self*vizinhoDir
	# resultado2 += self*vizinhoCima
	# resultado2 += self*vizinhoBaixo

	# print(resultado)
	# print(resultado2) # se alterar o valor do spin é como se tivesse a hamiltoniana com o valor invertido

	return resultado

def hamiltoniana():
	res = 0
	for i in range(largura):
		for j in range(altura):
			res += hamiltonianaLocal(i,j)

	return res


def magnetizacao():
	pass

def troca():
	for n in range(10):
		i = random.randint(0,altura-1)
		j = random.randint(0,largura-1)
		h = hamiltonianaLocal(i,j)

		if h > 0:
			spins[i][j] = -1*spins[i][j]
		else:
			# se mudar o valor do spin nao melhorar a energia, usamos a probabilidade para aceitar ou não a mudanca
			pass


		print(hamiltoniana())

def main():
	print(spins)
	troca()
	
		


main()