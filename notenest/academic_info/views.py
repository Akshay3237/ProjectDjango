from django.shortcuts import render
from .models import Branch,Branch_subject

def semester_view(request, branch_id):
    # Fetch branch object based on branch_id
    branch = Branch.objects.get(pk=branch_id)
    
    # Calculate the number of semesters based on the duration
    num_semesters = branch.branch_duration * 2  # Assuming each year has 2 semesters
    
    # Create a list of semester numbers
    semesters = [i for i in range(1, num_semesters + 1)]
    
    # Pass the branch_id, num_semesters, and semesters to the template
    return render(request, 'sem.html', {'bid': branch_id, 'num_semesters': num_semesters, 'semesters': semesters})

# views.py
from .models import Subject, Branch_subject

def semester_subjects_view(request, semester_id, branch_id):
    # Find the subjects related to the given semester and branch
    branch_subjects = Branch_subject.objects.filter(branch_id=branch_id, semester=semester_id)
    
    # Extract the subject IDs from the branch_subjects queryset
    subject_ids = branch_subjects.values_list('subject_id', flat=True)
    
    # Retrieve the subjects based on the IDs
    subjects = Subject.objects.filter(subject_id__in=subject_ids)
    
    return render(request, 'semester_subjects.html', {'subjects': subjects,'semester':semester_id,'bid':branch_id})

from django.shortcuts import render

def semester_subjects_branch_view(request, semester_id, branch_id, subject_id):
    # Your view logic here
    context={
        'semid':semester_id,
        'bid':branch_id,
        'subid':subject_id
    }
    return render(request, 'subject.html', context)
