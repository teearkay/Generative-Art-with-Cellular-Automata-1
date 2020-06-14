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

def automate_cyclic(canvas, N, gnome):
  new_can = np.zeros(canvas.shape)
  height, width = canvas.shape
  for i in range(0,height):
    for j in range(0,width):
      new_can[i,j] = canvas[i,j]
      nextValue = int(canvas[i,j]+1)%N
      flag=0
      for i1 in [-1,0,1]:
        for j1 in [-1,0,1]:
            if (gnome[i1+1,j1+1] == 1) and canvas[(i+i1)%height,(j+j1)%width] == nextValue:
                flag=1
                break
        if (flag==1):
          break
      if flag==1:
        new_can[i,j] = nextValue
  return new_can

# Neighborhood expressed as 1's and 0's as whether include the neighbor or not respectively 
chromosome = np.array([[0., 0., 1.], [1., 0., 0.], [1., 0., 0.]])                       ## Replace the chrmosome as per choice to check results

canvas,colors = setup()

for i in range(0,1000):
  canvas = automate_cyclic(canvas,N, chromosome)
  img = map2img(canvas, colors)
  if (i%50==0):
    plt.figure(figsize = (5,5))
    plt.imshow(img.astype(int))
    plt.show(block=False)
    plt.pause(0.01)
    plt.close()  





