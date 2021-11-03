from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('questions/',views.all_questions,name='questions'),
    path('questions/ask/',views.ask_question,name='ask'),
    path('questions/<int:pk>/',views.question_detail,name='question_detail'),
]