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

num1= int(input("enter the one number"))
num2= int(input("enter the two number"))
for i in range(num1):
    if num1%num2 == 0:
        print(i)
