from django.urls import path
from . import views

app_name = 'algebra'

urlpatterns = [
    path('theory/', views.theory, name='theory'),
    path('practice/', views.practice, name='practice'),
    path('api/get-exercise/', views.get_exercise, name='get_exercise'),
    path('api/check-answer/', views.check_answer, name='check_answer'),
]
