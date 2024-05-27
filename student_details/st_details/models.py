from django.db import models

class Teacher (models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=25)
    gender=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}-{self.subject}-{self.gender}"
    
    class Meta:
        db_table="Teacher"



class Student (models.Model):
    name=models.CharField(max_length=30)
    roll_no=models.CharField(max_length=30)
    section=models.CharField(max_length=10)
    teacher=models.ForeignKey(Teacher ,on_delete=models.CASCADE, related_name="students")        

    def __str__(self):
        return f"{self.name}-{self.roll_no}-{self.section}"
    
    class Meta:
        db_table="student"


