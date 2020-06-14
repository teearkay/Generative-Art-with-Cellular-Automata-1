import matplotlib.pyplot as plt
import cv2
import numpy as np

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

# Alternate Neighborhood Scheme: Using Two different Neighborhoods
def automate_cyclic_alter_neighborhood(canvas, N, gnome1, gnome2, x):
  new_can = np.zeros(canvas.shape)
  height, width = canvas.shape
  for i in range(0,height):
    for j in range(0,width):
      new_can[i,j] = canvas[i,j]
      nextValue = int(canvas[i,j]+1)%N
      if x%2==0:
        flag=0
        for i1 in [-1,0,1]:
          for j1 in [-1,0,1]:
              if (gnome1[i1+1,j1+1] == 1) and canvas[(i+i1)%height,(j+j1)%width] == nextValue:
                  flag=1
                  break
          if (flag==1):
            break
        if flag==1:
          new_can[i,j] = nextValue
      else:
        flag=0
        for i1 in [-1,0,1]:
          for j1 in [-1,0,1]:
              if (gnome2[i1+1,j1+1] == 1) and canvas[(i+i1)%height,(j+j1)%width] == nextValue:
                  flag=1
                  break
          if (flag==1):
            break
        if flag==1:
          new_can[i,j] = nextValue
  return new_can

# Alternate Neighborhood: Using 3 different Neighborhoods
def automate_cyclic_alter_neighborhood_(canvas, N, gnome1, gnome2, gnome3, x):
  new_can = np.zeros(canvas.shape)
  height, width = canvas.shape
  for i in range(0,height):
    for j in range(0,width):
      new_can[i,j] = canvas[i,j]
      nextValue = int(canvas[i,j]+1)%N
      if x%3==0:
        flag=0
        for i1 in [-1,0,1]:
          for j1 in [-1,0,1]:
              if (gnome1[i1+1,j1+1] == 1) and canvas[(i+i1)%height,(j+j1)%width] == nextValue:
                  flag=1
                  break
          if (flag==1):
            break
        if flag==1:
          new_can[i,j] = nextValue
      elif x%3==1:
        flag=0
        for i1 in [-1,0,1]:
          for j1 in [-1,0,1]:
              if (gnome2[i1+1,j1+1] == 1) and canvas[(i+i1)%height,(j+j1)%width] == nextValue:
                  flag=1
                  break
          if (flag==1):
            break
        if flag==1:
          new_can[i,j] = nextValue
      else:
        flag=0
        for i1 in [-1,0,1]:
          for j1 in [-1,0,1]:
              if (gnome3[i1+1,j1+1] == 1) and canvas[(i+i1)%height,(j+j1)%width] == nextValue:
                  flag=1
                  break
          if (flag==1):
            break
        if flag==1:
          new_can[i,j] = nextValue
  return new_can

# Neighborhoods

chromosome1 = np.array([[0., 0., 0.],
 [1., 0., 1.],
 [1., 0., 1.]])

chromosome2 = np.array([[0., 1., 1.],
 [0. ,0. ,0.],
 [1., 1., 0.]])

chromosome3 = np.array([[0., 1., 0.],
 [0. ,0. ,1.],
 [1., 1., 0.]])


# Result for 2 Neighborhoods

canvas,colors = setup()

for i in range(0,1000):
  canvas = automate_cyclic_alter_neighborhood(canvas,N,chromosome1, chromosome2, i)
  img = map2img(canvas, colors)
  if (i%50==0):
    plt.figure(figsize = (5,5))
    plt.imshow(img.astype(int))
    plt.show(block=False)
    plt.close()  


# Result for 3 Neighborhoods

canvas,colors = setup()

for i in range(0,1000):
  canvas = automate_cyclic_alter_neighborhood_(canvas,N,chromosome1, chromosome2, chromosome3,i)
  img = map2img(canvas, colors)
  if (i%50==0):
    plt.figure(figsize = (5,5))
    plt.imshow(img.astype(int))
    plt.show(block=False)
    plt.close()  
