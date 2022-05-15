## project one
'''
num = int(input("enter the number list : "))
l_even=[]
l_odd=[]
for i in range(num):
    number = int(input("enter the number  : "))
    if number % 2 ==0:
        l_even.append(number)
    else:
        l_odd.append(number)

print("even list ",l_even)
print("odd list ",l_odd)


'''


## project two
'''
word = input("enter the word : ")
chars = []
for char in word:
    if char not in chars:
        chars.append(char)
        print(char,end = "")
print("       length list = ",len(chars))

'''

#project three
'''
number = int(input("enter the number please : "))
for i in range(number+1):
    print(i)
'''

# project four
'''
num1= int(input("enter the one number"))
num2= int(input("enter the two number"))
for i in range(num1):
    if i%num2 == 0:
        print(i)
'''
#project five
'''
num1= int(input("enter the one number"))
num2= int(input("enter the two number"))
for i in range(100):
    if i%num1 == 0:
        print(f"{i} / {num1} = {i/num1}")
    if i%num2==0:
        print(f"{i} / {num2} = {i/num2}")
    else:
        continue
'''

#project six
class Game:
    def start(self):
        op = input("please select game : one or two or three or four or five or x(exit)").strip().lower()
        if op =="x":
            print("Good bay")
            exit
        elif op=="one":
            self.one()
        elif op=="two":
            self.two()
        elif op =="three":
            self.three()
        elif op =="four":
            self.four()
        elif op=="five":
            self.five()
        else:
            print("please chose in select ")
            self.start()
    def one(self):
        num = int(input("enter the number list : "))
        l_even=[]
        l_odd=[]
        for i in range(num):
            number = int(input("enter the number  : "))
            if number % 2 ==0:
                l_even.append(number)
            else:
                l_odd.append(number)

        print("even list ",l_even)
        print("odd list ",l_odd)
        self.start()

    def two(self):
        word = input("enter the word : ")
        chars = []
        for char in word:
            if char not in chars:
                chars.append(char)
                print(char,end = "")
        print("       length list = ",len(chars))
        self.start()

    def three(self):
        number = int(input("enter the number please : "))
        for i in range(number+1):
            print(i)
        self.start()

    def four(self):
        num1= int(input("enter the one number"))
        num2= int(input("enter the two number"))
        for i in range(num1):
            if i%num2 == 0:
                print(i)
        self.start()

    def five(self):
        num1= int(input("enter the one number"))
        num2= int(input("enter the two number"))
        for i in range(100):
            if i%num1 == 0:
                print(f"{i} / {num1} = {i/num1}")
            if i%num2==0:
                print(f"{i} / {num2} = {i/num2}")
            else:
                continue
g1 = Game()
g1.start()        


