class Calculator:
    def __init__(self,name):
        print(f"hello {name}")
        print(self.sum(12,12))
    def sum (self,x,y):
        return x+y
    def mul (self,x,y):
        return x*y
m = Calculator("firas")
print(m.sum(3,4))
f = Calculator ("jad")
print(f.sum(10,10)  )

print(m.mul(4,4))
