from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('solver/', views.solver, name='solver'),
    path('solve/', views.solve_expression, name='solve_expression'),
    path('exam/setup/', views.exam_setup, name='exam_setup'),
    path('exam/start/', views.exam_start, name='exam_start'),
]
