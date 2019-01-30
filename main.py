import matplotlib.pyplot as plt
import tkinter
import numpy as np
from docplex.mp.model import model

rnd = np.random
rnd.seed(1)

n = 10  #numero de mercados

#criando a lista de mercados
mercados = [x for x in range(1, n + 1)]

#criando uma lista de nodes a ser passados(mercados+casa)
nodos = [0] + mercados

#criando a lista de entregadores
entregadores = [x for x in range(1, 8)]

#posições dos nodos(mercados e casa)
loc_x = rnd.rand(len(nodos)) * 200
loc_y = rnd.rand(len(nodos)) * 100

#posição dos entregadores
loc_entregadores_x = rnd.rand(len(entregadores)) * 200
loc_entregadores_y = rnd.rand(len(entregadores)) * 100

#criando arcos entre nodos
arcosNodos = {(i, j) for i in nodos for j in nodos if i != j}
#calculando distancia entre nodos
distanciaNodos = {(i, j): np.hypot(loc_x[i] - loc_x[j], loc_y[i] - loc_y[j])
                  for i in nodos for j in nodos if i != j}

#criando arcos entre entregador e nodos
arcoEntregador = {(i, j) for i in entregadores for j in nodos}
#calculando distancia entre entregador e nodo
distanciaEntregador = {(i + 1, j): np.hypot(loc_entregadores_x[i] - loc_x[j],
                                            loc_entregadores_y[i] - loc_y[j])
                       for i in range(len(entregadores)) for j in nodos}
'''
#criando imagem para plot
plt.figure(figsize=(25,5))

#adicionando os mercados à imagem
for i in range(1,len(nodos)):
    print(i)
    plt.scatter(loc_x[i],loc_y[i],c="green")
    plt.annotate('Mercado %d'%i,(loc_x[i]+1,loc_y[i]-0.5))

#adicionando os entregadores à imagem
for i in range(len(entregadores)):
    plt.scatter(loc_entregadores_x[i],loc_entregadores_y[i],c="blue")
    plt.annotate('Entregador %d'%i,(loc_entregadores_x[i]+1,loc_entregadores_y[i]-0.5))

#adicionando a casa à imagem
plt.scatter(loc_x[0],loc_y[0],c="red",marker='s')
plt.annotate('Casa',(loc_x[0]+1,loc_y[0]-0.5))
plt.show()'''

mdl = Model('problem')

x = mdl.binary_var_dict(arcos, )
