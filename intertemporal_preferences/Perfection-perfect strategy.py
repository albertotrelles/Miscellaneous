# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:22:18 2023

@author: ALBERTO TRELLES
"""

import numpy as np

#Def Utility function U^t(tau)
def Utility(t, tau, rewards, costs, beta, inmediate_costs: bool):
    
    v = np.array(rewards)                               
    c = np.array(costs)
    
    if inmediate_costs:                                 
        if tau == t:
            U = beta*v[tau-1]-c[tau-1]
        elif tau > t:
            U = beta*(v[tau-1]-c[tau-1])
    
    else:                                               
        if tau == t:
            U = v[tau-1]-beta*c[tau-1]
        elif tau > t:
            U = beta*(v[tau-1]-c[tau-1])

    return(U)


#Según el perfil, obtener la estrategia  
def strategy(rewards, costs, beta, inmediate_costs: bool, profile):
    
    if profile == "tc":                                                         #Para time-consistent
        
        strat = list()
        for i in range(1, len(rewards) + 1):
            d = list()
            for j in range(i+1, len(rewards) + 1):
                
                now = Utility(i, i, rewards, costs, 1, inmediate_costs)
                later = Utility(i, j, rewards, costs, 1, inmediate_costs)
                
                if now >= later:
                    d.append("Y")
                else:
                    d.append("N")
            
            if "N" in d:
                strat.append("N")
            else:
                strat.append("Y")
        
        return(strat)
        
        
    elif profile == "n":                                                        #Para naivos
        
        strat = list()
        for i in range(1, len(rewards) + 1):
            d = list()
            for j in range(i+1, len(rewards) + 1):
                
                now = Utility(i, i, rewards, costs, beta, inmediate_costs)
                later = Utility(i, j, rewards, costs, beta, inmediate_costs)
                
                if now >= later:
                    d.append("Y")
                else:
                    d.append("N")
            
            if "N" in d:
                strat.append("N")
            else:
                strat.append("Y")
        
        return(strat)
        
    
    elif profile == "s":                                                        #Para sofisticados 
        
        strat = list()                                                          #Make the respective list (N, N, ..., N, Y)
        for i in range(1, len(rewards) + 1):
            strat.append("N")
        strat[len(rewards)-1] = "Y"
        
        
        for i in range (len(rewards) - 1, 0, -1):
            
            index = strat.index("Y")
            tau_prime = index + 1
            
            if Utility(i, i, rewards, costs, beta, inmediate_costs) >= Utility(i, tau_prime, rewards, costs, beta, inmediate_costs):
                strat[i-1] = "Y"
                
            else:
                strat[i-1] = "N"   
         
        return(strat)
        
    
    else:
        return(print("invalid profile"))
    
    
    
#EJEMPLOS DEL PAPER
strategy([2,2,2,2], [3,5,8,13], 1/2, True, "tc")   
strategy([2,2,2,2], [3,5,8,13], 1/2, True, "n")   
strategy([2,2,2,2], [3,5,8,13], 1/2, True, "s")   
    
strategy([3,5,8,13], [0,0,0,0], 1/2, False, "tc")
strategy([3,5,8,13], [0,0,0,0], 1/2, False, "n")
strategy([3,5,8,13], [0,0,0,0], 1/2, False, "s")

# (.).index("Y") + 1  es el momento en el que el individuo realiza la actividad. 



#####Hacer otra funcion que permita el delta. Para eso transformar v y c antes de los condicionales del perfil 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    