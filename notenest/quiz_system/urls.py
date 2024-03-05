from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<slug:subject_id>/', views.quiz_view, name='quiz'),
    path('quizdetail/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz_result/<int:result_id>/', views.quiz_result, name='quiz_result'),
    path('submit_quiz/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
]
