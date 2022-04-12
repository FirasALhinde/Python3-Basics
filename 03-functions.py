#functions
'''
def mysum(x,y): #argument , parameters
    print(x+y)
mysum(5,5)
'''
#parametres
''' 
  requierd
  keyword =positional
  default
  variba  le length
'''
'''
def mysum(x,y=0): 
    print(x+y)
mysum(x=5,y=3)
'''
'''
def mysum(y,x):
    result = x+y
    return result
print(mysum(11,11))
'''
#local vs global
'''
f = 0
print(f)
def do():
    global f
    f =5
    print(f)
do()
print(f)
'''
'''
mysum = lambda x,y :print(x+y)
mysum(12,12)
'''
for index, latter in enumerate ("firas alhinde"):
    print(f"{index} => {latter}")

