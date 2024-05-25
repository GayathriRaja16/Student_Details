from django.db import models


class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.course}"


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=25)
    students = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}.{self.students}"
