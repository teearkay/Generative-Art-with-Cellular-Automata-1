import random
import matplotlib.pyplot as plt
import cv2

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


# Cyclic Cellular Automata with threshold as 1 and Neumann Neighborhood
def automate_cyclic(canvas, N):
  new_can = np.zeros(canvas.shape)
  height, width = canvas.shape
  for i in range(0,height):
    for j in range(0,width):
      new_can[i,j] = canvas[i,j]
      nextValue = int(canvas[i,j]+1)%N
      if(nextValue == canvas[i, (j+1)%width] or nextValue == canvas[(i+1)%height, j] or nextValue == canvas[(i-1+height)%height, j] or nextValue == canvas[i, (j-1+width)%width]):
          new_can[i,j] = nextValue
  return new_can

canvas, colors = setup()

for i in range(0,1000):
  canvas = automate_cyclic(canvas,N)
  img = map2img(canvas, colors)
  if (i%50==0):
    plt.figure(figsize = (5,5))
    plt.imshow(img.astype(int))
    plt.show(block=False)
    plt.pause(0.1)
    plt.close()  



