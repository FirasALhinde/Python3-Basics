class Student:
    def __init__(self,name):
        print(f"welcome {name}")
        self.marks = []
        
        
    def add_mark(self,mark):
        self.marks.append(mark)

    def get_marks(self):
        print(self.marks)

    def get_avg(self):
        print(sum(self.marks)/len(self.marks))
s1 = Student("firas")

s1.add_mark(30)
s1.add_mark(90)
s1.add_mark(50)
s1.add_mark(80)
s1.add_mark(20)
s1.get_marks()
s1.get_avg()
s2 = Student("ali")

s2.add_mark(20)
s2.add_mark(60)
s2.add_mark(70)
s2.add_mark(30)
s2.add_mark(50)

s2.get_marks()
s2.get_avg()
