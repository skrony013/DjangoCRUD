from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('StudentForm', views.StudentFormView, name='student_form'),
]
