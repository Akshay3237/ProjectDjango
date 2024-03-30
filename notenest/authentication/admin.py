# authentication/admin.py

from django.contrib import admin
from .models import User, Student, Tutor, Parent

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login')
    search_fields = ('username', 'email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'branch_id', 'year', 'sem']

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject_id']

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_id']