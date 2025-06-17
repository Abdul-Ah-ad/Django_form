from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_view, name='feedback-form'),
    path('success/', views.feedback_success, name='feedback-success'),
]
