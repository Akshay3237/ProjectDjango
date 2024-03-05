from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('branch-<int:branch_id>/', views.semester_view, name='semester_view'),
    path('semester/sem-<int:semester_id>/branch-<int:branch_id>/', views.semester_subjects_view, name='semester_subjects'), 
    path('subject/sem-<int:semester_id>/branch-<int:branch_id>/subject-<int:subject_id>', views.semester_subjects_branch_view, name='subjects'),        
]
