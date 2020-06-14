import numpy as np
import keras 
import cv2
import matplotlib.pyplot as plt
import IPython
import random

# An Experimental extension of Stepping Stone rule (not discussed in the report as it was primarily a part of experimentation, not the result)
def automate_extended(image):
    row = image.shape[0]
    col = image.shape[1]
    for i in range(row):
      for j in range(col):
        r = random.random()
        if r<=0.8:
          x = random.randint(0,3)
          if x ==0:
            image[(i-3)%row,(j+1)%col,:] = image[i,j,:]
            image[(i-3)%row,j,:] = image[i,j,:]
          elif x==1:
            image[(i+1)%row,(j-3)%col,:] = image[i,j,:]
            image[i,(j-2)%col,:] = image[i,j,:]
            image[i,(j-3)%col,:] = image[i,j,:]
          elif x==2:
            image[(i-1)%row,(j+3)%col,:] = image[i,j,:]
            image[i,(j+3)%col,:] = image[i,j,:]
            image[(i+3)%row,(j+3)%col,:] = image[i,j,:]
          else:
            image[(i+2)%row,j,:] = image[i,j,:]
            image[(i+3)%row,(j+3)%col,:] = image[i,j,:]
            image[(i+3)%row,j,:] = image[i,j,:]
    return image


Img = cv2.imread("./Image.jpg")    ## Replace the image path and filename as per your downloaded image 
img = cv2.resize(Img,(256,256))

image = img

for i in range(0,10000):  
  image = automate_extended(image)
  if (i%100==0):
    plt.figure(figsize = (3,3))
    plt.imshow(image.astype(int))
    plt.show(block=False)
    plt.pause(0.1)
    plt.close()
