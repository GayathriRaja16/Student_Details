# ormquery/views.py

from django.http import JsonResponse
from st_details.models import Student, Teacher
from st_details.serializers import StudentSerializer, TeacherSerializer, TeacherStudentAllocationSerializer
from rest_framework import viewsets

def teacher_student_allocation(request):
    teachers_with_students = Teacher.objects.select_related('students').all()

    data = []
    for teacher in teachers_with_students:
        data.append({
            'teacher_name': teacher.name,
            'student_name': teacher.students.name if teacher.students else None
        })

    serializer = TeacherStudentAllocationSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

# Class-based view for Student model
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ["get", "post", "put", "delete"]

# Class-based view for Teacher model
class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    http_method_names = ["get", "post", "put", "delete"]

