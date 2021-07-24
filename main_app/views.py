from django.shortcuts import render
from . import forms

from .models import Student


# Create your views here.

def HomeView(request):
    context = {'title': "Home"}
    return render(request, 'index.html', context)


def StudentFormView(request):
    form = forms.StudentForm()
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HomeView(request)

    context = {'title': "Student Reg Form", "student_form": form}
    return render(request, 'student_form.html', context)
