import matplotlib.pyplot as plt
import numpy as np

N = 10

x1 = np.logspace(0.1, 1, N, endpoint=True)

x2 = np.logspace(0.1, 1, N, endpoint=False)

y = np.zeros(N)
print(x1)
print(x2)
plt.plot(x1, y, )


plt.plot(x2, y + 0.5)


plt.ylim([-0.5, 1])


plt.show()
