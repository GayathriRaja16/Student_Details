from django.contrib import admin
from st_details.models import Student,Teacher

admin.site.register([Student, Teacher])
