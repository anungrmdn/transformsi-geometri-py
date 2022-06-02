# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:03:03 2022

@author: ANUNG
"""

#Rotasi

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
rotasi=int(input('Masukan derajat rotasi:'))
print("===============================================================")


print("===============================================================")
print("-----------Masukan titik pusat---------------------------------")
print("===============================================================")
tpx=int(input('Masukan titik pusat x:'))
tpy=int(input('Masukan titik pusat y:'))


if rotasi > 0:
    cosr = round(np.cos(np.deg2rad(rotasi)))
    minsinr = round(-np.sin(np.deg2rad(rotasi)))
    sinr = round(np.sin(np.deg2rad(rotasi)))
else :
    cosr = round(np.cos(np.deg2rad(abs(rotasi))))
    minsinr = round(np.sin(np.deg2rad(abs(rotasi))))
    sinr = round(-np.sin(np.deg2rad(abs(rotasi))))

matrixr = np.array(([cosr,minsinr],
                    [sinr,cosr]))

if tpx == 0 and tpy == 0:
    matrixa = np.array(([ax,ay]))
    matrixb = np.array(([bx,by]))
    matrixc = np.array(([cx,cy]))
    
    matrixaresult = np.dot(matrixr, matrixa)
    matrixbresult = np.dot(matrixr, matrixb)
    matrixcresult = np.dot(matrixr, matrixc)
else :
    matrixa = np.array(([ax - tpx,ay - tpy]))
    matrixb = np.array(([bx - tpx,by - tpy]))
    matrixc = np.array(([cx - tpx,cy - tpy]))

    matrixaresult = np.dot(matrixr, matrixa) + np.array((tpx, tpy))
    matrixbresult = np.dot(matrixr, matrixb) + np.array((tpx, tpy))
    matrixcresult = np.dot(matrixr, matrixc) + np.array((tpx, tpy))

print("===============================================================")
print("--------Hasil titik koordinat setelah di rotasi rotasi---------")     
print("===============================================================")
print("A'",matrixaresult)
print("B'",matrixbresult)
print("C'",matrixcresult)

tampx1 = np.array([ax, bx, cx, ax])
tampy1 = np.array([ay, by, cy, ay])

tampx2 = np.array([matrixaresult[0],
                   matrixbresult[0], 
                   matrixcresult[0],
                   matrixaresult[0]])
tampy2 = np.array([matrixaresult[1],
                   matrixbresult[1], 
                   matrixcresult[1],
                   matrixaresult[1]])


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











