import numpy as np
import matplotlib.pyplot as plt
import random
import time
from copy import deepcopy

def Binary(n): #function to get binary representation
    binary = "" 
    i = 0
    while n > 0 and i<=8: 
        s1 = str(int(n%2)) 
        binary = binary + s1 
        n /= 2
        i = i+1
    return binary[::-1]  

lattice_size = 259 #lattice size for CA
## using 259 as padding of one cell is required for first and last element

ic = list(np.zeros(lattice_size).astype(int)) # initializing IC
ic[(lattice_size+1)>>2] = 1 # using the center-black rule 

runs = 150 #runs (timesteps) to keep applying rule to the IC

rules = [] #array which stores all the rules to enumerate ICs

rules.append([0,0,0,0,0,0,0,0])
for rule in range(1,256):  #storing all rules
    d = Binary(rule)
    d=d[1:]
    rules.append([int(n) for n in d])

n = 2  #number of rules to add in the ruleset

for iterations in range(100): #Generating plots for 100 randomly generated triplets of rules
    
    ruleset = [] #set of rules to use
    for iterations in range(n): #Selecting combinations of different triplets to use
        rnum = random.randint(0,len(rules)-1)
        ruleset.append(rules[rnum])

    icloc = deepcopy(ic) #Copying the IC for the current iteration
    
    plotting = [] #to track changes (all the timesteps) to the IC
    
    for k in range(runs): #Applying rule to the IC for timesteps = runs
        plotting.append(icloc[1:259]) #tracking changes to IC
        
        for j in range(257): #iterating for all cells in the lattice of 257 cells
            
            nbd = icloc[j:j+3] ##neighborhood of the current cell (j+1)
            nbdstr = "".join([str(elems) for elems in nbd])
            nbd_val = int(nbdstr,2) #value of the current cell's neighborhood
            
            icloc[j+1] = ruleset[k%n][nbd_val] ## Uniform Rule Application to determine cell state for (j+1)
    
    plotting.append(icloc[1:259]) #tracking changes to IC
    
    plt.imshow(np.array(plotting),cmap="binary", vmax=1, vmin=0) #plotting the 2-D representation of the CA  
    plt.show()