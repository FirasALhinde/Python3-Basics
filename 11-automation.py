'''
import pyautogui as pyg

pyg.moveTo(800, 150)
pyg.password('Enter password (text will be hidden)')
pyg.alert("Error")

'''
'''
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
'''    '''

numbers = [1,2,3,4,5,6]
#res = []
#for i in numbers:
#    res.append(i*i)

#print(res)


res =[i*i for i in numbers]
print(res)
'''

#for x in range(1,5):
 #  for y in range(1,10):
  #      print(x*y)


#res = [x*y for x in range(1,5) for y in range(1,10) ]
#print(res)
'''
even = [x for x in range (0,20) if x%2==0]
print(even)
'''
numbers = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
x = numbers[0]
y = numbers[1:-1]
z = numbers[-1]
print(x)
print(y)
h,*m,n = numbers
print(h)
print(m)
print(n)
