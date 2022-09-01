from django.urls import path

from core import views


urlpatterns = [
    path('api/endpoint/', views.endpoint),
]
