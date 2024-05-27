from rest_framework import viewsets
from .models import Teacher,Student
from .serializers import TeacherSerializer,StudentSerializer

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    http_method_names = ["get", "post", "put", "delete"]

# Class-based view for Student model
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ["get", "post", "put", "delete"]



