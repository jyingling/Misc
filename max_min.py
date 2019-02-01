def max_min(x, y, z):

  x = x
  y = y
  z = z
  
  highest = 0
  lowest = 0
  
    # determine highest number 
  if x > y:
    if x > z:
      highest = x
    elif z > x:
      highest = z
  else: # y > x
    if y > z:
      highest = y
    elif z > y:
      highest = z
  
  # determine lowest number
  if x < y:
    if x < z:
      lowest = x
    elif z > x:
      lowest = z
  else: # y < x
    if y < z:
      lowest = y
    elif y > z:
      lowest = z
  
  print("Highest: {} \tLowest: {}".format(highest, lowest))

x = int(input("First number: "))
y = int(input("Second number: "))
z = int(input("Third number: "))

max_min(x,y,z)
