import numpy as np
from matplotlib import pyplot as plt
x=np.random.randint(10, size=10)
y=np.random.randint(10, size=10)
print(x,y)
plt.scatter(x,y)
plt.show()