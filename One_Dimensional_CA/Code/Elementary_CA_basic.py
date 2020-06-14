import numpy as np
import matplotlib.pyplot as plt
import random 

def create_canvas(length=257, prob=0.5, method='default'): #Probability of 0
    canvas = ''
    if method == 'default':
      for i in range(0, length):
        x = random.random()
        if x<=prob:
          canvas+='0'
        else:
          canvas+='1'
    elif method =='center_black':
      canvas = '0'*int(length/2) + '1' + '0'*int(length/2)
    return canvas

def map2img(list_canvas):
    n, m = len(list_canvas), len(list_canvas[0])
    image = np.zeros((n, m))
    for i in range(0, n):
      for j in range(0, m):
        image[i,j] = abs(int(list_canvas[i][j])-1)
    return image

def automate(canvas, rule):
  n = len(canvas)
  new_canvas = ''
  for i in range(0, n):
    new_canvas += rule[7 - (4*int(canvas[(i-1)%n]) + 2*int(canvas[(i)%n]) + int(canvas[(i+1)%n]))]
  return new_canvas

def generate_image(rule, size=(257, 257), method='center_black'):
  canvas = create_canvas(size[1], method=method)
  list_canvas = [canvas]
  for i in range(1, size[0]):
    canvas = automate(canvas, rule)
    list_canvas.append(canvas)
  image = map2img(list_canvas)
  plt.imshow(image.astype(int), cmap='gray')

def rule_r(r):
  rule = ''
  while(r!=0):
    rule+= str(r%2)
    r = int(r/2)
  rule = '0'*(8-len(rule)) + rule[::-1]
  return rule

## Generate Image
generate_image(rule_r(60))		# Replace the rule number as per choice, here rule_r(60) = 00111100  


