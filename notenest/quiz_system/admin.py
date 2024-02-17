# quiz_system/admin.py

from django.contrib import admin
from .models import Quiz, Question, Result

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'subject', 'number_of_questions')
    search_fields = ('subject__subject_name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'quiz', 'question_definition', 'answer')
    list_filter = ('quiz',)
    search_fields = ('question_definition', 'quiz__subject__subject_name')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('result_id', 'student', 'quiz', 'score')
    list_filter = ('quiz',)
    search_fields = ('student__username', 'quiz__subject__subject_name')
