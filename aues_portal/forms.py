from django.forms import ModelForm
from django import forms

from .models import *

class TeacherForm(ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'
		exclude = ['user','department']

class DocumentForm(ModelForm):
	class Meta:
		model = Document
		fields = '__all__'