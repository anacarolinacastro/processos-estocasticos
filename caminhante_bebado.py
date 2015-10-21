import random
import matplotlib.pyplot as plt

position = []
media = []
position.append(0)
for i in range(1000):
	x = random.randint(0,1)
	if x==0:
		x=-1
	position.append(position[-1] + x)
plt.plot(position)
plt.show()
