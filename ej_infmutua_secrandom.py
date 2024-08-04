# coding: utf-8
from sklearn.metrics import normalized_mutual_info_score
import inf_mutua as im
import random as rnd
import matplotlib.pyplot as plt

def muta(secuencia, proc):
    sec = [0]*len(secuencia)
    for i in range(len(secuencia)):
        v = rnd.random()
        sec[i] = rnd.choice([1,2,3,4]) if v<=proc else secuencia[i]
    return sec

secuencia = [rnd.choice([1,2,3,4]) for i in range(20)]
Lp = [muta(secuencia, 1) for i in range(100)]

larga = []
for l in Lp:
    larga += l
larga += secuencia
for l in Lp:
    larga += l

I = []
N = len(secuencia)
for i in range(len(larga)-N):
    ventana = larga[i:i+N]
    I.append(im.im(ventana,secuencia))

plt.plot(I)
plt.show()
