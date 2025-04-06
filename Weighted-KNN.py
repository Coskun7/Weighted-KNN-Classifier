#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 23:46:49 2025

@author: mali
"""
def kokal(x):
    return x**(1/2)
   
def usal(x,level):
    return x**level

def eucledianDistance(A,B):
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] - A[i],2)
        distance = kokal(total)
        return distance

def most_frequnt(dizi):
        counter = 0
        num = dizi[0]
        for i in dizi:
            curr_frequnt = dizi.count(i)
            if (curr_frequnt > counter):
                counter = curr_frequnt
                num = i
            
        return num

def kumeleme(liste):
    mavi = []
    kırmızı = []
    for eleman in liste:
        if eleman[2] == 'mavi':
            mavi.append(eleman)
        else:
            kırmızı.append(eleman)
        
    return mavi,kırmızı

def agirilikMerkezi(liste):
    G_y = 0
    G_x = 0
    G = []
    for eleman in liste:
        G_x += eleman[0]
        G_y += eleman[1]
    
    G[0][1] = G_x / len(liste), G_y / len(liste)
    return G
    
A = [5,5,'mavi']
B = [10,10,'mavi']
C = [25,25,'kırmızı']
D = [50,50,'mavi']
E = [100,100,'kırmızı']
F = [255,255,'kırmızı']

ornekUzay = [A,B,C,D,E,F]

mavi,kırmızı = kumeleme(ornekUzay)

mavi_G,kırmızı_G = agirilikMerkezi(mavi),agirilikMerkezi(kırmızı)

print('Verinin X değerini girin')
x = int(input())
print('Verinin Y değerini girin')
y = int(input())

ornekNokta = [x,y,""]

def KNNhesapla(uzay,ornek,n):
    tmp_ornekUzay = uzay.copy()
    tmp_ornekNokta = ornek.copy()
    tmp_ornekNokta.pop()
    
    komsular = []
    print("En yakın '"  +  str(n) + "' komşu : ")
    
    for i in range(n):

        minimumMesafe = 1000
        enYakinEleman = []
            
        for eleman in tmp_ornekUzay:
                            
            tmp_eleman = eleman.copy()
            tmp_eleman.pop()
                
            mesafe = eucledianDistance(tmp_eleman,tmp_ornekNokta)
                
            if mesafe <= minimumMesafe:
                minimumMesafe = mesafe 
                enYakinEleman = eleman.copy()
            
        print(enYakinEleman)
            
        renk = enYakinEleman[-1]
        komsular.append(renk)
            
        tmp_ornekUzay.remove(enYakinEleman)
    print("Komşuların renkleri:")
    print(komsular)
            
    return most_frequnt(komsular)

sonuc = KNNhesapla(ornekUzay, ornekNokta, 3)
print("Tahmin edilen renk:", sonuc)