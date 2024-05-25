from st_details.models import Student, Teacher
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"

class TeacherStudentAllocationSerializer(serializers.Serializer):
    teacher_name = serializers.CharField()
    student_name = serializers.CharField()
