'''
def m_t(s,e,s1,e1): 
    for i in range(s+1,e+1):
        print("------------------")
        for j in range(s1,e1+1):
            print(f"{i} * {j} = {i*j}")


word = input("enter the word :  ")
chrs = []
for char in word:
    if char not in chrs:
        chrs.append(char)
        print(char,end=" ")
'''

class Game:
    def __init__(self):
        print("welcome in our game")
        print("chose one our games ")
        print("     1 : muliplation table")
        print("     2 : remove duplicate")
        print("     x  : exit")

        user_choise = input("enter Game Number : ")
        
        if user_choise == "x":
            exit
        else:
            if int(user_choise) == 1:
                start = int(input("enter Number : "))
                end = int(input("enter Number : "))
                start2 = int(input("enter Number : "))
                end2 = int(input("enter Number : "))
                self.m_t(start,end,start2,end2)
            elif int(user_choise) ==2:
                self.remove_duplicate()
    def m_t(self,s,e,s1,e1): 
        for i in range(s+1,e+1):
            print("------------------")
            for j in range(s1,e1+1):
                print(f"{i} * {j} = {i*j}")


    def remove_duplicate (self):
        word = input("enter the word :  ")
        chrs = []
        for char in word:
            if char not in chrs:
                chrs.append(char)
                print(char,end=" ")
        
g1 = Game()
