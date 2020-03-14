class management():
    def auth(self,username,password):
        
        if username =="anand" and password =="bita": 
            print("LOGIN SUCCESS")
            return True
        else:
            print("LOGIN FAILED")
            return False
            
class Student(management):
    count=0
    def __init__(self,name,ID,mark,username,password):
        Student.count=Student.count+1
        self.count=Student.count
        self.N=name
        self.I=ID
        self.M=mark
        login_status = super(Student,self).auth(username,password)
        if login_status:
            print(self.avg())
            print(self.grade())
    def avg(self):
        totalsum = sum(self.M)
        return totalsum //len(self.M)
    def grade(self): 
        avg=self.avg()
        if avg<=50:
            return "F"
        if 50<avg<=60:
            return "E"
        if 60<avg<=70:
            return "D"
        if 70<avg<=80:
            return "C"
        if 80<avg<=90:
            return "B"
        if 90<avg<=95:
            return "A"
        if 95<avg<=100:
            return "S"
stud1=Student("anand","786",[45,55,65,75],"anand","bita")
stud2=Student("arun","123",[48,56,89,98],"anand","bita")
stud3=Student("arjun","456",[40,80,67,55],"anand","bita")
stud4=Student("alex","789",[15,25,35,45],"anand","bita")
stud5=Student("akash","101",[45,55,15,66],"anand","bita")
stud6=Student("amir","112",[11,22,33,44],"anand","bita")
print(Student.count)




