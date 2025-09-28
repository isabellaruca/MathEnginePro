"""
URL configuration for mathengine_project project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('arithmetic/', include('topics.arithmetic.urls')),
    path('algebra/', include('topics.algebra.urls')),
]
