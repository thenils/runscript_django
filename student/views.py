from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
from django.views.generic import ListView, DetailView


class StudentListView(ListView):
	model = Student
	template_name='student/student_list.html'
	context_object_name= 'students'

class StudentDetailView(DetailView):
	model = Student
	template_name='student/student_detail.html'