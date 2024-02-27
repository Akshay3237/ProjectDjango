from django.shortcuts import render,redirect
from .models import Quiz,Result
# Create your views here.

def quiz_view(request, subject_id):
    # Your view logic here
    quizzes = Quiz.objects.filter(subject_id=subject_id)
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

from django.shortcuts import render
from .models import Quiz, Question
from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question

def quiz_detail(request, quiz_id):
    # Retrieve the quiz object or return a 404 error if not found
    quiz = get_object_or_404(Quiz, quiz_id=quiz_id)
    # Get all questions related to the quiz
    questions = Question.objects.filter(quiz=quiz)
    
    # Construct a list of dictionaries containing question details
    question_details = []
    for question in questions:
        question_details.append({
            'question': question.question_definition,
            'options': [question.option1, question.option2, question.option3, question.option4],
            'answer': question.answer,
        })

    context = {
        'quiz': quiz,
        'questions': question_details,
    }
    return render(request, 'quiz_detail.html', context)

def submit_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    score = 0
    count = 1
    for question in questions:
        selected_option = request.POST.get(f'question{count}')
        count=count+1
        print(selected_option)
        print(question.answer)
        if str(selected_option) == str(question.answer):
            score += 1
    total_questions = len(questions)
    percentage_score = (score / total_questions) * 100
    result = Result.objects.create(user=request.user, quiz=quiz, score=percentage_score)
    return redirect('quiz_result', result_id=result.pk)

def quiz_result(request, result_id):
    result = Result.objects.get(pk=result_id)
    return render(request, 'quiz_result.html', {'result': result})