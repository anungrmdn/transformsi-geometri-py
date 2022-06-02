# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:08:53 2022

@author: ANUNG
"""
#Pensekalaan
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
print("-----------Masukan titik skala---------------------------------")
print("===============================================================")
tsx=int(input('Masukan titik skala x:'))
tsy=int(input('Masukan titik skala y:'))

ax2 = ax * tsx
ay2 = ay * tsy

bx2 = bx * tsx
by2 = by * tsy

cx2 = cx * tsx
cy2 = cy * tsy

tampx1 = np.array([ax, bx, cx, ax])
tampy1 = np.array([ay, by, cy, ay])

tampx2 = np.array([ax2,bx2, cx2, ax2])
tampy2 = np.array([ay2,by2, cy2, ay2])

print("===============================================================")
print("-----------------------Hasil Skala-----------------------------")
print("===============================================================")
print("A'",[ax2, ay2])
print("B'",[bx2, by2])
print("C'",[cx2, cy2])
   
fig, ax = plt.subplots()


limx = np.min([tampx1,tampx2])

limy = np.min([tampy1,tampy2])

if limx > 0:
    limx = 0

if limy > 0:
    limy = 0
    
ax.set_xlim(limx - 1, np.max([tampx1, tampx2]) + 1)
ax.set_ylim(limy - 1, np.max([tampy1, tampy2]) + 1)

plt.plot(tampx1, tampy1, tampx2, tampy2)
plt.show()


