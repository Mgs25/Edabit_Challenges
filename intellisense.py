import math

class DB:
    def __init__(self,name,rollNo,grade):
        self.name = name
        self.rollNo = rollNo
        self.grade = grade
    
    def results(self):
        return self.name +" Passed" if self.grade > 6 else self.name +  " Failed"

student1 = DB("Methran",19,2)

print(DB.results(student1))
    