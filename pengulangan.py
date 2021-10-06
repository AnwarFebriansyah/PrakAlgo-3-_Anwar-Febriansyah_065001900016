# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:25:54 2021

@author: HP
"""
kecil = int(input("Masukkan angka awal : "))
besar = int(input("Masukkan angka akhir : "))
#hasil = besar > kecil
while kecil and kecil <= besar:
    print(kecil, besar)
    kecil += 1
    besar -= 1