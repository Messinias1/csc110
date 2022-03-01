
def computeThis(x,y):
  if (x > y):
    z = x - y
  elif (x == y):
    z = 0
  else:
    z = y - x
  return z

print(computeThis(4, 6))