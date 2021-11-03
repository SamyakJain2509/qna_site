from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def index(request):
    return render(request, 'qna/home.html',{})

@login_required
def all_questions(request):
    questions = Question.objects.all()
    return render(request, 'qna/questions.html',{'questions':questions})

@login_required
def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    form = AnswerForm()
    answers = question.answers.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        new_answer = form.save(commit=False)
        new_answer.question = question
        new_answer.answerer = request.user
        new_answer.save()
        return redirect('home')
    else:
        form = AnswerForm()

    return render(request, 'qna/detail.html',{'question':question, 'form':form, 'answers':answers})

@login_required
def ask_question(request):
    form = AskForm()
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.asker = request.user
            new_question.save()
            return redirect('questions')

    else:
        form = AskForm()
    return render(request, 'qna/ask.html', {'form':form})