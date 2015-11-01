import matplotlib.pyplot as plt
import math

p1 = [2,4]
p2 = [3,9]
p3 = [6,36]
p4 = [9,90]
# p = [p1,p2,p3,p4]
p = []
for i in range(11):
	p.append([i,math.sqrt(i)])

def f(t): 
	# interpolacao de lagrange
	l = []
	for i in range(len(p)): # numero de pontos
		lAux = 1
		for j in range(len(p)):
			if (i != j):
				lAux = lAux * (t - p[j][0])/(p[i][0] - p[j][0])
		l.append(lAux)

	res = 0
	for i in range(len(p)):
		res += p[i][1]*l[i]

	return res


def main():
	for i in range(len(p)):
		plt.plot(p[i][0],p[i][1],'bo')

	data = []
	t = []
	for i in range(101):
		t.append(i*0.1)
		data.append(f(i*0.1))

	plt.plot(t,data,'r')
	plt.show()

main()