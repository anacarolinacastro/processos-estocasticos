import random
import matplotlib.pyplot as plt

position = []
position.append(0)	#position start from 0
for i in range(1000):	#numbers of interations
	x = random.randint(0,1)
	if x==0:
		x=-1
	position.append(position[-1] + x)	#increment position

plt.plot(position)	#prepare plot
plt.show()	#show plot
