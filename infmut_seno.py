#coding:utf8
import numpy as np
import matplotlib as mpl

from matplotlib      import pyplot as plt
from sklearn.metrics import mutual_info_score 

def discretiza(X, n, eps=0.001):
  """
  Discretiza un vector (numpy) en n estados
  ---
  parameters:
    X: numpy array
    n: numero de estados
  returns:
    Xt discretizado
  """
  Xt = X + np.abs(X.min()) + eps
  R = Xt.max() - Xt.min()
  rr = R/n
  f = lambda x, xmn: int((x-xmn) / rr) 
  Xd = np.array([f(x, Xt.min()) for x in Xt])
  return Xd


def main():
  T = np.linspace(0,6*np.pi,6000)
  X = np.sin(T)
  Xd = discretiza(X, 10)
  IM = []
  v = Xd[:int(len(Xd)/3)]
  print(f"Calculando información mutua")
  for j in range(len(Xd) - len(v)):
    IM.append(mutual_info_score(v, Xd[j:j+len(v)]))
  return (T[:len(IM)], IM)
  

if __name__=='__main__':
  T, IM = main()
  plt.plot(T, IM); plt.show()


