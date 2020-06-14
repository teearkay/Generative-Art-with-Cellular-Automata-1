import numpy as np
import keras 
import cv2
import matplotlib.pyplot as plt
import IPython
import random

def newdata(size):
  image = np.zeros(size)

  for i in range(size[0]):
    for j in range(size[1]):
      for k in range(0,3):
        image[i,j,k] = int(random.randint(0,255))

  return image

# Stepping Stone Updation Rule
def automate(image):
    row = image.shape[0]
    col = image.shape[1]
    for i in range(row):
      for j in range(col):
        r = random.random()
        if r<=0.5:
          x = random.randint(0,3)
          if x ==0:
            image[(i-1)%row,j,:] = image[i,j,:]
          elif x==1:
            image[i,(j-1)%col,:] = image[i,j,:]
          elif x==2:
            image[i,(j+1)%col,:] = image[i,j,:]
          else:
            image[(i+1)%row,j,:] = image[i,j,:]

    return image


# Random noise generated Image
image = newdata((256,256,3))

for i in range(0,10000):  
  image = automate(image)
  if (i%100==0):
    plt.figure(figsize = (3,3))
    plt.imshow(image.astype(int))
    plt.show(block=False)
    plt.pause(0.1)
    plt.close()

# Load some Image taken from Google as the start image

Img = cv2.imread("./Image.jpg")    ## Replace the image path and filename as per your downloaded image 
img = cv2.resize(Img,(256,256))

image = img

for i in range(0,10000):  
  image = automate(image)
  if (i%100==0):
    plt.figure(figsize = (3,3))
    plt.imshow(image.astype(int))
    plt.show(block=False)
    plt.pause(0.1)
    plt.close()
