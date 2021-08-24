# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:45:00 2021

@author: Leopoldo
"""

'''
Simples 1D random  
para demonstrar qual acurácia necessária
para se obter ganhos nas opções binárias
'''

import numpy as np
import random
from matplotlib import pyplot as plt


#Número de trades.
N_steps = 100

# Acurácia do sinal
prob = 0.5



'''
Definir a função para o random walk.  
N número de steps and
p probabilidade de corte   
'line' tipo da linha
'''
def SimpleRandomWalk(N, p, line):
    position = np.empty(N)
    position[0] = 0
    pos_counter = 0

    steps = np.arange(N)

    #Start the random walk.
    for i in range(1,N):
        #gerar variavel aleatória entre 0 e 1.
        test = random.random()
        '''
        Se test menor que a acurácia ganho 
        se não perda
        '''
        if test <= p:
            pos_counter += 0.85
        else:
            pos_counter -= 1
        #acrescentar retorno no array
        position[i] = pos_counter



    #Gerar gráficos
    plt.plot(steps, position, line)
    plt.title(f'Random Walk - Acurácia {prob}')
    plt.xlabel('Trades')
    plt.ylabel('Ganhos')


    return None

plt.figure()
#N linhas de Random walk para comparar
for i in range(0,10):
    SimpleRandomWalk(N_steps, prob, line = '-')
plt.show()