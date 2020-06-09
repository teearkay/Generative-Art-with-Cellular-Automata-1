## Multi Rule Set

import numpy as np
import matplotlib.pyplot as plt
import random 

def create_canvas(length=257, prob=0.5, method='default', n_rules=None): #Probability of 0
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
    elif method =='custom':
      for i in range(0, length):
        canvas+= str(random.randint(0,n_rules-1))
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

def rule_r(r):
  rule = ''
  while(r!=0):
    rule+= str(r%2)
    r = int(r/2)
  rule = '0'*(8-len(rule)) + rule[::-1]
  return rule

def generate_image_multi(rule_list, size=(257, 257), rule_base='seq'):
  canvas = create_canvas(size[1], method='center_black')
  if rule_base=='seq':
    seq = create_canvas(size[0], method='custom', n_rules=len(rule_list))
    list_canvas = [canvas]
    for i in range(1, size[0]):
      canvas = automate(canvas, rule_r(rule_list[int(seq[i])]))
      list_canvas.append(canvas)
    
    image = map2img(list_canvas)
    plt.imshow(image.astype(int), cmap='gray')

  elif rule_base=='uniform':
    list_canvas = [canvas]
    n_rules= len(rule_list)
    for i in range(1, size[0]):
      canvas = automate(canvas, rule_r(rule_list[i%n_rules]]))
      list_canvas.append(canvas)
    
    image = map2img(list_canvas)
    plt.imshow(image.astype(int), cmap='gray')
    
## Generate Image

rules_list = [73, 60, 129, 99]
generate_image_multi(rules_list)

## Image from randomly selected rules

def generate_rules_list(N):
   rules_list = []
   for i in range(0, N):
     rules_list.append(random.randint(0,255))
   return rules_list

rule_list_2 = generate_rules_list(6) 
generate_image_multi(rule_list_2)
