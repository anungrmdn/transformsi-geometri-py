# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 20:13:20 2022

@author: ANUNG
"""

#Refleksi
import matplotlib.pyplot as plt
import numpy as np


print("=========================================================")
print("    MASUKAN PILIHAN RELEKSI   ")
print("=========================================================")
print("     1. REFLEKSI sumbu x : P(x,y) -> P'(x,-y)            ")
print("     2. REFLEKSI sumbu y : P(x,y) -> P'(-x,y)            ")
print("     3. REFLEKSI sumbu y = x : P(x,y) -> P'(y,x)         ")
print("     4. REFLEKSI titik 0 : P(x,y) -> P'(-x,-y)           ")
print("     5. REFLEKSI sumbu x = h : P(x,y) -> P'(2h - x,y)    ")
print("     6. REFLEKSI sumbu y = h : P(x,y) -> P'(x,2h - y)    ")
print("     7. REFLEKSI sumbu y = -x : P(x,y) -> P'(-y,-x)      ")
print("=========================================================")
PIL=int(input("Masukan Pilihan Anda: "))

if PIL == 1:
    print("=========================================================")
    print("=  1. ANDA memilih REFLEKSI TERHADAP sumbu x : P(x,y) -> P'(x,-y)   ")
    print("=========================================================")
    
    ax=int(input('Masukan titik untuk nilai A x:'))
    ay=int(input('Masukan titik untuk nilai A y:'))
    bx=int(input('Masukan titik untuk nilai B x:'))
    by=int(input('Masukan titik untuk nilai B y:'))
    cx=int(input('Masukan titik untuk nilai C x:'))
    cy=int(input('Masukan titik untuk nilai C y:'))

    
    ax2 = ax;     bx2 = bx;      cx2 = cx
    ay2 = -ay;    by2 = -by ;    cy2 = -cy
   
    
    tampx1 = np.array([ax, bx, cx, ax])
    tampy1 = np.array([ay, by, cy, ay])

    tampx2 = np.array([ax2, bx2, cx2, ax2])
    tampy2 = np.array([ay2, by2, cy2, ay2])
    
    print("=========================================================")
    print("=   Hasil REFLEKSI TERHADAP sumbu x : P(x,y) -> P'(x,-y)   ")
    print("=========================================================")
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
    ax.set_title("REFLEKSI TERHADAP sumbu x : P(x,y) -> P'(x,-y)")
    
    plt.plot(tampx1, tampy1, tampx2, tampy2)
    plt.show()
    
elif PIL == 2:
    print("=========================================================")
    print("=  2. ANDA memilih REFLEKSI sumbu y : P(x,y) -> P'(-x,y)       ")
    print("=========================================================")
    
    ax=int(input('Masukan titik untuk nilai A x:'))
    ay=int(input('Masukan titik untuk nilai A y:'))
    bx=int(input('Masukan titik untuk nilai B x:'))
    by=int(input('Masukan titik untuk nilai B y:'))
    cx=int(input('Masukan titik untuk nilai C x:'))
    cy=int(input('Masukan titik untuk nilai C y:'))
    
    ax2 = -ax;   bx2 = -bx;    cx2 = -cx
    ay2 = ay;    by2 = by ;    cy2 = cy
   
    
    tampx1 = np.array([ax, bx, cx, ax])
    tampy1 = np.array([ay, by, cy, ay])

    tampx2 = np.array([ax2,bx2, cx2, ax2])
    tampy2 = np.array([ay2,by2, cy2, ay2])
    
    print("=========================================================")
    print("=   Hasil REFLEKSI TERHADAP sumbu y : P(x,y) -> P'(-x,y)     ")
    print("=========================================================")
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
    ax.set_title("REFLEKSI TERHADAP sumbu y : P(x,y) -> P'(-x,y) ")
     
    plt.plot(tampx1, tampy1, tampx2, tampy2)
    plt.show()

elif PIL == 3:
    print("=========================================================")
    print("=  3. ANDA memilih REFLEKSI sumbu y = x : P(x,y) -> P'(y,x)       ")
    print("=========================================================")

    ax=int(input('Masukan titik untuk nilai A x:'))
    ay=int(input('Masukan titik untuk nilai A y:'))
    bx=int(input('Masukan titik untuk nilai B x:'))
    by=int(input('Masukan titik untuk nilai B y:'))
    cx=int(input('Masukan titik untuk nilai C x:'))
    cy=int(input('Masukan titik untuk nilai C y:'))
    
    ax2 = ay;    bx2 = by;      cx2 = cy
    ay2 = ax;    by2 = bx;      cy2 = cx
   
    
    tampx1 = np.array([ax, bx, cx, ax])
    tampy1 = np.array([ay, by, cy, ay])

    tampx2 = np.array([ax2, bx2, cx2, ax2])
    tampy2 = np.array([ay2, by2, cy2, ay2])
    
    print("=========================================================")
    print("=   Hasil REFLEKSI TERHADAP sumbu y = x : P(x,y) -> P'(y,x)      ")
    print("=========================================================")
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
    ax.set_title("REFLEKSI TERHADAP sumbu y = x : P(x,y) -> P'(y,x) ")
    
    plt.plot(tampx1, tampy1, tampx2, tampy2)
    plt.show()
    
elif PIL == 4:
    print("=========================================================")
    print("=====  4. ANDA memilih titik 0,0 : P(x,y) -> P'(-x,-y)       ")
    print("=========================================================")
 
    ax=int(input('Masukan titik untuk nilai A x:'))
    ay=int(input('Masukan titik untuk nilai A y:'))
    bx=int(input('Masukan titik untuk nilai B x:'))
    by=int(input('Masukan titik untuk nilai B y:'))
    cx=int(input('Masukan titik untuk nilai C x:'))
    cy=int(input('Masukan titik untuk nilai C y:'))
    
    ax2 = -ax;   bx2 = -bx;    cx2 = -cx
    ay2 = -ay;   by2 = -by ;   cy2 = -cy
   
    
    tampx1 = np.array([ax, bx, cx, ax])
    tampy1 = np.array([ay, by, cy, ay])

    tampx2 = np.array([ax2, bx2, cx2, ax2])
    tampy2 = np.array([ay2, by2, cy2, ay2])
    
    print("=========================================================")
    print("=   Hasil REFLEKSI TERHADAP titik 0,0 : P(x,y) -> P'(-x,-y)       ")
    print("=========================================================")
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
    ax.set_title("REFLEKSI TERHADAP titik 0,0 : P(x,y) -> P'(-x,-y)")
    
    plt.plot(tampx1, tampy1, tampx2, tampy2)
    plt.show()

elif PIL == 5:
    print("=========================================================")
    print("=      ANDA memilih REFLEKSI sumbu x = h : P(x,y) -> P'(2h - x,y)   ")
    print("=========================================================")
    
    sumbux=int(input("Masukan titik x: "))
    print("=========================================================")
    
    ax=int(input('Masukan titik untuk nilai A x:'))
    ay=int(input('Masukan titik untuk nilai A y:'))
    bx=int(input('Masukan titik untuk nilai B x:'))
    by=int(input('Masukan titik untuk nilai B y:'))
    cx=int(input('Masukan titik untuk nilai C x:'))
    cy=int(input('Masukan titik untuk nilai C y:'))
    
    ax2 = 2*sumbux - ax;    bx2 = 2*sumbux - bx;    cx2 = 2*sumbux - cx
    ay2 = ay;               by2 = by ;              cy2 = cy
   
    
    tampx1 = np.array([ax, bx, cx, ax])
    tampy1 = np.array([ay, by, cy, ay])

    tampx2 = np.array([ax2, bx2, cx2, ax2])
    tampy2 = np.array([ay2, by2, cy2, ay2])
    
    print("=========================================================")
    print("=   Hasil REFLEKSI TERHADAP sumbu x = h : P(x,y) -> P'(2h - x,y)       ")
    print("=========================================================")
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
    ax.set_title("REFLEKSI TERHADAP sumbu x = h : P(x,y) -> P'(2h - x,y) ")
    
    plt.plot(tampx1, tampy1, tampx2, tampy2)
    plt.show()
    
elif PIL == 6:
    print("=========================================================")
    print("=====  6. ANDA memilih REFLEKSI sumbu y = h : P(x,y) -> P'(x,2h - y)       ")
    print("=========================================================")
     
    sumbuy=int(input("Masukan titik y: "))
    print("=========================================================")
     
    ax=int(input('Masukan titik untuk nilai A x:'))
    ay=int(input('Masukan titik untuk nilai A y:'))
    bx=int(input('Masukan titik untuk nilai B x:'))
    by=int(input('Masukan titik untuk nilai B y:'))
    cx=int(input('Masukan titik untuk nilai C x:'))
    cy=int(input('Masukan titik untuk nilai C y:'))
    
    ax2 = ax;               bx2 = bx;               cx2 =  cx
    ay2 = 2*sumbuy -ay;     by2 = 2*sumbuy - by ;   cy2 = 2*sumbuy -cy
   
    
    tampx1 = np.array([ax, bx, cx, ax])
    tampy1 = np.array([ay, by, cy, ay])

    tampx2 = np.array([ax2, bx2, cx2, ax2])
    tampy2 = np.array([ay2, by2, cy2, ay2])
    
    print("=========================================================")
    print("=   Hasil REFLEKSI TERHADAP sumbu y = h : P(x,y) -> P'(x,2h - y)        ")
    print("=========================================================")
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
    ax.set_title("REFLEKSI TERHADAP sumbu y = h : P(x,y) -> P'(x,2h - y)    ")
    
    plt.plot(tampx1, tampy1, tampx2, tampy2)
    plt.show()
    
elif PIL == 7:
    print("=========================================================")
    print("=    7. ANDA memilih REFLEKSI sumbu y = -x : P(x,y) -> P'(-y,-x)       ")
    print("=========================================================")

    ax=int(input('Masukan titik untuk nilai A x:'))
    ay=int(input('Masukan titik untuk nilai A y:'))
    bx=int(input('Masukan titik untuk nilai B x:'))
    by=int(input('Masukan titik untuk nilai B y:'))
    cx=int(input('Masukan titik untuk nilai C x:'))
    cy=int(input('Masukan titik untuk nilai C y:'))
    
    ax2 = -ay;    bx2 = -by;      cx2 = -cy
    ay2 = -ax;    by2 = -bx;      cy2 = -cx
   
    
    tampx1 = np.array([ax, bx, cx, ax])
    tampy1 = np.array([ay, by, cy, ay])

    tampx2 = np.array([ax2, bx2, cx2, ax2])
    tampy2 = np.array([ay2, by2, cy2, ay2])
    
    print("=========================================================")
    print("=   Hasil REFLEKSI TERHADAP sumbu y = -x : P(x,y) -> P'(-y,-x)         ")
    print("=========================================================")
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
    ax.set_title("REFLEKSI TERHADAP sumbu y = -x : P(x,y) -> P'(-y,-x)    ")
    
    plt.plot(tampx1, tampy1, tampx2, tampy2)
    plt.show()
    
else :
    print("Tidak ada pilihan")