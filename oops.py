class cit:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def welcome(self):
        print("welcome "+self.name)
student=cit("pooja","cse")
print(student.name)
student=cit("poojitha","ece")
print(student.dept)
student.welcome()
        
        

