from django.urls import path
from . import views

app_name = 'arithmetic'

urlpatterns = [
    path('theory/', views.theory, name='theory'),
    path('practice/', views.practice, name='practice'),
    path('get-exercise/', views.get_exercise, name='get_exercise'),
    path('check-answer/', views.check_answer, name='check_answer'),
    path('exam-question/', views.exam_question, name='exam_question'),
]
