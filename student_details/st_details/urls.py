# ormquery/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from st_details.views import StudentView, TeacherView

router = DefaultRouter()
router.register("student", StudentView, basename="student")
router.register("teacher", TeacherView, basename="teacher")

urlpatterns = [
    path("", include(router.urls)),
]
