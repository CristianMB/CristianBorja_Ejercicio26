import numpy as np
import matplotlib.pyplot as plt

splits = np.array(range(10,110, 10))

plt.figure()
T = np.loadtxt('tiempos')
plt.scatter(splits,T)
plt.title("Data Splits")
plt.xlabel('Number of Splits')
plt.ylabel('Time of Execution')
plt.savefig('NvsT.pdf')
