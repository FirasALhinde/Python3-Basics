
class Calc:
    def __init__(self,name):
        print(f"Hello {name}")
    def sum(self,x,y):
        return x+y
    def mul(self,x,y):
        return x*y


class SicCalc (Calc) :
    def sum(self,x,y):
        print("gggggg")
        return x+y
    def power (self,x,y):
        return x**y
    





v1 = SicCalc("firas")
print(v1.sum(2,3))
print(v1.mul(3,4))
print(v1.power(2,3))

class A :
    def do (self):
        print('A')

class B (A):
    pass

class C :
    def do():
        print("c")

class D (B,C):
    pass


dv = D()
dv.do()
print(D.mro())
