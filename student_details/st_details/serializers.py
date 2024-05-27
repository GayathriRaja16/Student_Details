from rest_framework import serializers
from .models import Student, Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'subject', 'gender', 'students'] 
