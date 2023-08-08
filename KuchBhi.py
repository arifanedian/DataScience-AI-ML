class Student:
    def __init__(self,rollno="",name="",batch="",university_name=""):
        self.rollno = rollno
        self.name = name
        self.batch = batch
        self.university_name = university_name
    
    def studentInfo(self):
        print(f"""
            Student Information Cell
            ________________________
            Student Rollno : {self.rollno}
            Student Name   : {self.name}
            Student Batch  : {self.batch}
            Student Uni    : {self.university_name}
        """)
    def get_rollno(self):
        return self.rollno
    
    def get_name(self):
        return self.name
    
    def get_batch(self):
        return self.batch
    
    def get_uni(self):
        return self.university_name
    
    def set_rollno(self,rollno):
        self.rollno = rollno
        
    def set_name(self,name):
        self.name = name
        
    def set_batch(self,batch):
        self.batch = batch
        
    def set_uni(self,university_name):
        self.university_name = university_name