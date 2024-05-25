# ormquery/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from st_details.views import StudentView, TeacherView, teacher_student_allocation

router = DefaultRouter()
router.register("student", StudentView, basename="student")
router.register("teacher", TeacherView, basename="teacher")

urlpatterns = [
    path("", include(router.urls)),
    path('teacher-student-allocation/', teacher_student_allocation, name='teacher_student_allocation'),
]
