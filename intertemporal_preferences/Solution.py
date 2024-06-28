# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:06:58 2023

@author: ALBERTO TRELLES
"""

import numpy as np

#Utility function from perspective t, of doing activity at time tau, given cost, rewards, beta and whether costs are inmediate or not
def Utility(t, tau, rewards, costs, beta, inmediate_costs: bool):
    
    v = np.array(rewards)                               #Set rewards and costs as vectors 
    c = np.array(costs)
    
    if inmediate_costs:                                 #Function if costs are inmediate
        if tau == t:
            U = beta*v[tau-1]-c[tau-1]
        elif tau > t:
            U = beta*(v[tau-1]-c[tau-1])
    
    else:                                               #Function if rewards are inmediate
        if tau == t:
            U = v[tau-1]-beta*c[tau-1]
        elif tau > t:
            U = beta*(v[tau-1]-c[tau-1])

    return(U)


#Example with Inmediate costs
rewards = [2,2,2,2]
costs = [3,5,8,13]   

strat = list()
for i in range(1, 5):
    d = list()
    for j in range(i+1, 5):
        
        now = Utility(i, i, rewards, costs, 1/2, True)
        later = Utility(i, j, rewards, costs, 1/2, True)
        
        if now >= later:
            d.append("Y")
        else:
            d.append("N")
    
    if "N" in d:
        strat.append("N")
    else:
        strat.append("Y")
         
        
#Estrategia para TC (beta=1)
rewards = [2,2,2,2]
costs = [3,5,8,13]   

strat = list()
for i in range(1, 5):
    d = list()
    for j in range(i+1, 5):
        
        now = Utility(i, i, rewards, costs, 1, True)
        later = Utility(i, j, rewards, costs, 1, True)
        
        if now >= later:
            d.append("Y")
        else:
            d.append("N")
    
    if "N" in d:
        strat.append("N")
    else:
        strat.append("Y")
        
for i in range(1,5):
    print(i)
    
#Example with Inmediate rewards 
strat = list()
for i in range(1, 5):
    d = list()
    for j in range(i+1, 5):
        
        now = Utility(i, i, [3,5,8,13], [0,0,0,0], 1/2, False)
        later = Utility(i, j, [3,5,8,13], [0,0,0,0], 1/2, True)
        
        if now >= later:
            d.append("Y")
        else:
            d.append("N")
    
    if "N" in d:
        strat.append("N")
    else:
        strat.append("Y")
        
    

    

# u11 = Utility(1,1, rewards, costs, 1/2, True)
# u12 = Utility(1,2, rewards, costs, 1/2, True)
# u13 = Utility(1,3, rewards, costs, 1/2, True)
# u14 = Utility(1,4, rewards, costs, 1/2, True)
# u22 = Utility(2,2, rewards, costs, 1/2, True)
# u23 = Utility(2,3, rewards, costs, 1/2, True)
# u24 = Utility(2,4, rewards, costs, 1/2, True)
# u33 = Utility(3,3, rewards, costs, 1/2, True)
# u34 = Utility(3,4, rewards, costs, 1/2, True)
# u44 = Utility(4,4, rewards, costs, 1/2, True)

#Strategy for Sophisticates 
rewards = [2,2,2,2]
costs = [3,5,8,13]

strat = list(("N","N","N","Y")) 
for i in range (4-1, 0, -1):
    
    index = strat.index("Y")
    tau_prime = index + 1
    
    if Utility(i, i, rewards, costs, 1/2, True) >= Utility(i, tau_prime, rewards, costs, 1/2, True):
        strat[i-1] = "Y"
        
    else:
        strat[i-1] = "N"
        
 
#Instant rewards, sophisticates
rewards = [3,5,8,13]
costs = [0,0,0,0]

strat = list(("N","N","N","Y")) 
for i in range (4-1, 0, -1):
    
    index = strat.index("Y")
    tau_prime = index + 1
    #print("index", index, "tau'", tau_prime)
    
    if Utility(i, i, rewards, costs, 1/2, False) >= Utility(i, tau_prime, rewards, costs, 1/2, False):
        strat[i-1] = "Y"
        
    else:
        strat[i-1] = "N"   
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
