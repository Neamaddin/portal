from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Institute)
class InstituteTranslationOptions(TranslationOptions):
	fields = ('name', 'short_name', 'info')

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
	fields = ('name', 'short_name', 'info')

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
	fields = ('name', 'surname', 'patronymic', 'rezume', 'post', 'education', 'qualification_up', 'science_articles', 'аwards')

@register(Group)
class GroupTranslationOptions(TranslationOptions):
	fields = ('name',)

@register(Student)
class StudentTranslationOptions(TranslationOptions):
	fields = ('name', 'surname', 'patronymic')

@register(Document)
class DocumentTranslationOptions(TranslationOptions):
	fields = ('name',)