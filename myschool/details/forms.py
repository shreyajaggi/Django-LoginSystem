from django import forms
from django.db import models
from .models import(Teacher,Student,Class,Homework)




class TeacherForm(forms.ModelForm):
	class Meta:
		model=Teacher
		fields=('name_T','emails_T','branch')

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=('name_S','emails_S','branch','rollnumber')

class HomeworkForm(forms.ModelForm):
	class Meta:
		model= Homework
		fields=('topic','questions','due_date')
		

	














