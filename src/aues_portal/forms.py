from modeltranslation.forms import TranslationModelForm
from django.forms import ModelForm
from django import forms
from .models import *

class TeacherForm(TranslationModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'
		exclude = ['user','department']

class DocumentForm(TranslationModelForm):
	class Meta:
		model = Document
		fields = '__all__'