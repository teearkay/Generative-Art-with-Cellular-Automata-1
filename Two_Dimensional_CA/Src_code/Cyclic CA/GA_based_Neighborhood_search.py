import matplotlib.pyplot as plt
import cv2
import numpy as np

import random
population_size = 5
elitism = 1       # best member only

Target = np.zeros((3,3))

class Individual(object):
    def __init__(self,chromosome):
        self.chromosome = chromosome
        self.fitness = 0
    @classmethod
    def mutated_gene(self):
        return random.randint(0,1) 
    @classmethod
    def create_genome(self):
        global Target
        genome_shape = Target.shape
        x = np.zeros(genome_shape)
        for i in range(genome_shape[0]):
            for j in range(genome_shape[1]):
                x[i][j] = self.mutated_gene()
        return x 
    
    def mate(self,par2):
        global Target
        genome_shape = Target.shape
        child_chromosome = np.zeros(genome_shape)
        for i in range(genome_shape[0]):
            for j in range(genome_shape[1]):
                x = random.random()
                if (x<=0.40):
                    child_chromosome[i][j] = self.chromosome[i][j]
                elif x<=(0.80):
                    child_chromosome[i][j] = par2.chromosome[i][j]
                else:
                    child_chromosome[i][j] = self.mutated_gene()
        
        x = Individual(child_chromosome)

        return Individual(child_chromosome)

# Number of Colors in color palette
N = 14

def map2img(canvas, colors):
  image =  np.zeros((canvas.shape[0],canvas.shape[1],3))
  for i in range(0,canvas.shape[0]):
    for j in range(0,canvas.shape[1]):
      image[i,j,:] = colors[int(canvas[i,j]),:]
      
  return image.astype(int)

def setup(size=(256,256)):
  colors = np.zeros((N,3))
  for i in range(0,N):
    colors[i,:] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
  
  canvas = np.zeros(size)
  for i in range(0,size[0]):
    for j in range(0,size[1]):
      canvas[i,j] = int(random.randint(0,N-1))

  return canvas, colors

def generate_pattern():
    global population_size,elitism
    canvas, colors = setup()
    population = []
    for i in range(0,population_size):
        x = Individual.create_genome()
        population.append(Individual(x))
    
    generation = 0
    gen_hold = []
    while generation<10:
        fig, ax = plt.subplots(1,population_size,figsize =(30,10*population_size))
        j=0
        for gnome in population:
          canv_copy = canvas.copy()
          for i in range(0,100):
            canv_copy = automate_cyclic(canv_copy,N,gnome.chromosome)
          ax[j].imshow(map2img(canv_copy, colors).astype(int))
          j+=1
        plt.show()
        for i in range(0,population_size):
          print(population[i].chromosome)
        x = int(input("Enter the best pattern here: "))
        population[x-1].fitness = -1
        population = sorted(population,key= lambda x:x.fitness)
        gen_hold.append(population)
        new_population = []
        new_population.extend(population[:elitism])
        
        s = population_size-elitism
        for i in range(0,s):
            par1= random.choice(population[:5])
            par2= random.choice(population[:5])
            child = par1.mate(par2)
            new_population.append(child)
        
        population = new_population
        generation+=1
        
    return gen_hold

## Application

gen_arr  = generate_pattern()
