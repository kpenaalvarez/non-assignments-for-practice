142# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

L = np.linspace(1, 3, num=3)

print(f"L = {L}")
print( type(L[0]))

for i in range(3):
    V = L[i]**3
    print(f"L = L[i], V = {V}")

V =[]
for i in range(3):
    V.append(L[i]**3)
    print(f"L = {L[i]}, V = {V[i]}")

plt.plot(L, V, 'bo')
plt.title('Volume of cube by side length')
plt.xlabel('Length of a sdide')
plt.ylabel('Volume of cube')
plt.grid()
plt.show()