x = 0
while x <10:
    print(x)
    x+=1
#infnit loop
    
x=0
while x<10:
    print(x)


#single while

x=0
while x<10:print(x);x+=1

#nested loop

x=0
while x<10:
    print(x)
    y=0
    while y<4:
        print(y)
        y+=1
    x+=1


x =0
while x<5:
    y=0
    while y<=10:
        print(f"{x} * {y} = {x*y}")
        y+=1
    x+=1


#for

name = "firas"
for x in name:
    print(x)

for x in range(1,11):
    print(x)


# Multiplication table with for

for n in range(1,6):
    for k in range(1,11):
        print(f"{n} * {k} = {n*k}")
   '''
'''
x =int(input("enter the number: \n"))
for n in range(1,x):
         print(n)

#control system
#break
#continue

for x in range(1,11):
    if x ==6:
        if x>0:
            continue
        print(x*2)
    print(x)
    
