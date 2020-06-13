import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib inline
import random
import time
from copy import deepcopy
import random
import pandas as pd

bestfitness = [] #keep track of fitness of every gene in all generations
fit = {} #used later to select top 20 genes from every generation
t_genes = list() #keeps track of all genes in each generation 
plots = [] #stores plots for each IC's 2D Space-Time evolution  


#generate initial genes

genes = []
for i in range(100):
    g = []
    for k in range(128):
        g.append(random.randint(0,1))
    genes.append(g)
t_genes+=[genes]


# genetic algorithm
for generation in range(51): # runnning for 51 generations
    
    #generate ICs
    ic = []
    for i in range(100): # for each generation a new set of 100 ICs is generated
        ic0 = []
        l = []
        k = 0
        density=(i+1) # to maintain a uniform distribution with values of rho belonging to [0,100]
        n0 = int(density*1.48)
        n1 = 149 - n0
        while(k<149):
            if(k<n0):
                l.append(0)
                k = k+1
            else:
                l.append(1)
                k = k+1
        ic.append(random.sample(l,149))
    
    for i in range(100): # padding each IC from both sides
        ic[i] = ic[i] + ic[i][0:3]
        ic[i] = ic[i][146:149] + ic[i]
    
    #number of runs(timesteps) per gene that the IC is computed 
    runs = 150
    fit = {} 
    
    #fitness test 
    
    for g in range(len(genes)):
        icloc = deepcopy(ic)
        plotting = []
        score = 0
        gene = genes[g]
        for i in range(len(icloc)): #iterating for each IC
            
            for k in range(runs): #computing each IC timesteps = runs times for each gene(rule)
                
                plotting.append(icloc[i][3:152]) #track of current 2D matrix of IC (space-time)
                
                for j in range(149): #updation for each cell of the lattice (IC)
                    nbd = icloc[i][j:j+7] ##neighborhood of the current cell
                    nbdstr = "".join([str(elems) for elems in nbd])
                    icloc[i][j+3] = gene[int(nbdstr,2)] #using rule to set the value of current cell wrt neighborhood
                    
            plotting.append(icloc[i][3:152])
            
            if((i>=50)and(sum(icloc[i][3:152])==0)): #finally checking if condition is satisfied for task
                score+=1
                plots.append(plotting)
                
            if((i<50)and(sum(icloc[i][3:152])==149)): #finally checking if condition is satisfied for task
                score+=1
                plots.append(plotting)
                
            plotting = []
            
        f = float(score)/100 #final score for the gene, fitness function ends.
        
        fit[rule] = f #saving fitness for each gene for future selection of elites
        
    dct = {k: v for k, v in sorted(fit.items(), key=lambda item: item[1],reverse=True)} #sorting top 20 values of fitness
    elite_index = [k for k in dct.keys()] 
    
    elites = list()
    for j in range(20): #top 20 genes selected
        elites.append(genes[elite_index[j]])

    bestfitness.append([(k,v) for k,v in dct.items()])
        
    #crossover and mutation
    
    newpop = [] #the container for rest of the 80 genes for the next generation
    for i in range(40): #40 iterations of randomly chosing a pair out of the elites for
                        #a single point crossover to produce 80 new children
        c1 = random.randint(0,19) 
        c2 = random.randint(0,19)
        c_point = random.randint(1,127)
        g1 = deepcopy(genes[c1])
        g2 = deepcopy(genes[c2])
        temp = g2[c_point:128]
        g2[c_point:128] = g1[c_point:128]
        g1[c_point:128] = temp
        
        #mutation: mutating each gene at 2 random positions
        for i in range(2):
            c1 = random.randint(0,127)
            c2 = random.randint(0,127)
            g1[c1]= int(not(g1[c1]))
            g2[c2]=int(not(g2[c2]))
        newpop += [g1,g2]
    plots = []
    genes = elites+newpop #preparing next generation genes
    t_genes+=[genes]