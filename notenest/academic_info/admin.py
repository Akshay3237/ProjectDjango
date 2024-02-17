# academic_info/admin.py

from django.contrib import admin
from .models import Branch, Subject, Branch_subject, PrerequisiteSubject

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_id', 'branch_name', 'branch_duration')
    search_fields = ('branch_name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_id', 'subject_name', 'subject_duration')
    search_fields = ('subject_name',)

@admin.register(Branch_subject)
class BranchSubjectAdmin(admin.ModelAdmin):
    list_display = ('branch', 'subject')
    list_filter = ('branch', 'subject')
    search_fields = ('branch__branch_name', 'subject__subject_name')

@admin.register(PrerequisiteSubject)
class PrerequisiteSubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'prerequisite_subject')
    list_filter = ('subject', 'prerequisite_subject')
    search_fields = ('subject__subject_name', 'prerequisite_subject__subject_name')
