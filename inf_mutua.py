#!/usr/bin/python
#coding:utf-8

from collections     import Counter
import math, random, numpy as np

def genera_conjuntos(seq, k, M=None):
    """
    genera los conjuntos para evaluar la información mutua
    seq: iterable con símbolos
    k: corrimiento
    M: tamaño de la ventana. Si es None entonces se toma una tercera parte de seq
    """
    if(M is None):
        M = int(len(seq)/3)
        
    C = []
    X, Y = [], []
    v = seq[:M]
    for x, y in zip(v, seq[k:k+M]):
        C.append((x,y))
        X.append(x)
        Y.append(y)
    return C, X, Y

def entropia(X, base=2):
    """
    Calcula la entropia en lista X
    X: iterable con símbolos
    """
    conteo = Counter(X)
    T = np.sum(list(conteo.values()))
    P = {}
    for simbolo in conteo:
        P[simbolo] = conteo[simbolo] / T

    H = 0.0
    for val in P:
        H += np.log(P[val]) * P[val]
    return -H/np.log(base)
 
def conjunta(C, X, Y, base=2):
    """
    Calcula la entropía conjunta de C tomando
    los símbolos en X e Y
    C es un iterable con tuplas
    X: set con lista de simbolos
    Y: set con lista de símbolos
    """
    Xsimb, Ysimb = X, Y
    l = list([(x,y) for x in Xsimb for y in Ysimb])
    z = [0]*len(l)
    conteos = dict(zip(l,z))
    cc = Counter(C)
    for c in cc:
        conteos[c] = cc[c]
    #print(np.sum(list(conteos.values())))

    T = np.sum(list(conteos.values()))
    P = {}
    for simbolo in conteos:
        P[simbolo] = conteos[simbolo] / T

    H = 0.
    for val in P:
        H += 0 if P[val] == 0 else np.log(P[val])*P[val]
    return -H/np.log(base)
 
def mi(S,k, base, M=None):
    """
    Calcula la información mutua de la secuencia S con un 
    corrimiento k.
    params:
    
    Parameters:
        S (iterable): List o iterable para sacar información mutua
        k (int):      Entero que determina el corrimiento de prueba
        base (int):   Base en la que se encuentra el resultado
        M (int):      Tamaño de ventana 

    Returns:
        IM(X,Y,k ) = H(X) + H(Y) - H(X,Y)
        Información mutua de S con corrimiento k durante M posiciones

    """
    C, X, Y = genera_conjuntos(S,k, M=M)
    Hx      = entropia(X, base=base)
    Hy      = entropia(Y, base=base)
    Hxy     = conjunta(C,set(X), set(Y), base=base)
    return Hx + Hy - Hxy

