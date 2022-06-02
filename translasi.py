# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:27:42 2022

@author: ANUNG
"""

#Translasi
import matplotlib.pyplot as plt
import numpy as np


print("===============================================================")
print("-----------Masukan titik-titik koordinat Segitiga--------------")
print("===============================================================")

ax=int(input('Masukan titik untuk nilai A x:'))
ay=int(input('Masukan titik untuk nilai A y:'))
bx=int(input('Masukan titik untuk nilai B x:'))
by=int(input('Masukan titik untuk nilai B y:'))
cx=int(input('Masukan titik untuk nilai C x:'))
cy=int(input('Masukan titik untuk nilai C y:'))

print("===============================================================")
print("---------Masukan nilai titik koordinat Translasi---------------")
print("===============================================================")

ta=int(input('Masukan titik untuk nilai T a:'))
tb=int(input('Masukan titik untuk nilai T b:'))

ax2 = ax + ta
bx2 = bx + ta
cx2 = cx + ta

ay2 = ay + tb
by2 = by + tb
cy2 = cy + tb

tampx1 = np.array([ax, bx, cx, ax])
tampy1 = np.array([ay, by, cy, ay])

tampx2 = np.array([ax2, bx2, cx2, ax2])
tampy2 = np.array([ay2, by2, cy2, ay2])

print("===============================================================")
print("-----------------------Hasil translasi-------------------------")
print("===============================================================")
print("A'",[ax2, ay2])
print("B'",[bx2, by2])
print("C'",[cx2, cy2])

# create a figure and axes
fig, ax = plt.subplots()

limx = np.min([tampx1,tampx2])

limy = np.min([tampy1,tampy2])

if limx > 0:
    limx = 0

if limy > 0:
    limy = 0

# set x, y-axis limits 
ax.set_xlim(limx - 1, np.max([tampx1, tampx2]) + 1)
ax.set_ylim(limy - 1, np.max([tampy1, tampy2]) + 1)


plt.plot(tampx1, tampy1, tampx2, tampy2)

plt.show()

