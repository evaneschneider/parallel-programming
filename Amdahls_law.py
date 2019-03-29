import numpy as np
import matplotlib
import matplotlib.pyplot as plt

P = np.linspace(0,0.9,100)
N = np.arange(10000)+1

def amdahls_law(P):
  return 1 / (1 - P)

def amdahl_two(P, N):
  S = 1.0 - P
  return 1 / ( (P/N) + S)

parallel_simple = amdahls_law(P)
parallel_25 = amdahl_two(0.25, N)
parallel_50 = amdahl_two(0.5, N)
parallel_75 = amdahl_two(0.75, N)
parallel_95 = amdahl_two(0.95, N)

plt.plot(P, parallel_simple)
plt.xlabel("Parallel Fraction")
plt.ylabel("Speedup")
plt.savefig("Amdahl_simple.png")
plt.close()

plt.plot(N, parallel_25)
plt.plot(N, parallel_50)
plt.plot(N, parallel_75)
plt.plot(N, parallel_95)
plt.xscale('log')
plt.xlabel("Number of Processors")
plt.ylabel("Speedup")
plt.legend(labels=["25% Parallel", "50% Parallel", "75% Parallel", "95% Parallel"])
plt.savefig("Amdahl_processors.png")
plt.close()
