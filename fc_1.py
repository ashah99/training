# te Modified April 23, 2023
# Modified 
# Date April 28, 2023
def measure(a,b,t):
  """a integer, b integer, Parm A for area or V for volume"""
  

  if (a < 1) or (b <1):
        return  -1
  elif       t == "a" or t == "A":
       return a * b
  elif       t == "v" or t == "V" :
       return a ** b
  else :
       return -1

# Calling function
letter = "R"
if letter < "S":
  print (letter)
letter = "T"
if letter < "S":
  print (letter)
  
for i in range(0, 5):
  print(i)

x, y = 5, 4
type_s = "A"

obj_area = measure(x, y, type_s)
print ("The object area is", obj_area)

type_s = "V"
obj_vol = measure(x, y, type_s)

print ("The object volume is", obj_vol) # comments

x,y = 0, 5
obj_vol = measure(x, y, type_s)
print ("The object volume is", obj_vol)

x,y = 3, 4
type_s = "x"
obj_vol = measure(x, y, type_s)
print ("The object volume is", obj_vol)
d = 10
while d ==10:
  print(d)
  d = d + 1
  
  
# This is end of program

