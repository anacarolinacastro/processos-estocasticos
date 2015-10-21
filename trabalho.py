import matplotlib.pyplot as plt
# (t,x)

p1 = [2,4]
p2 = [3,9]
p3 = [6,36]
p4 = [9,81]
p = [p1,p2,p3,p4]

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
	plt.plot(p1[0],p1[1],'bo')
	plt.plot(p2[0],p2[1],'bo')
	plt.plot(p3[0],p3[1],'bo')
	plt.plot(p4[0],p4[1],'bo')

	data = []
	t = []
	for i in range(100):
		t.append(i*0.1)
		data.append(f(i*0.1))

	plt.plot(t,data,'r')
	plt.show()

main()