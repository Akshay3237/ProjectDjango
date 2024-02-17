# authentication/admin.py

from django.contrib import admin
from .models import User, Student, Tutor, Parent

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login')
    search_fields = ('username', 'email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user', 'branch_id', 'year', 'sem')
    list_filter = ('branch_id',)
    search_fields = ('student_id', 'user__username', 'user__email')

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor_id', 'user', 'subject_id')
    list_filter = ('subject_id',)
    search_fields = ('tutor_id', 'user__username', 'user__email')

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('parent_id', 'user', 'student_id')
    search_fields = ('parent_id', 'user__username', 'user__email')
