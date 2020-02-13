from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Institute(models.Model):
	name = models.CharField("Полное название института", max_length = 100)
	short_name = models.CharField("Аббревиатура института", max_length = 10)
	url_name = models.CharField("Ссылка", max_length = 10)
	info = models.TextField("Информация об институте", blank = True)
	
	class Meta:
		verbose_name = "Институт"
		verbose_name_plural = "Институты"

	def __str__(self):
		return self.short_name

class Department(models.Model):
	institute = models.ForeignKey(Institute, verbose_name = "Институт", on_delete = models.CASCADE, related_query_name = "institute")
	name = models.CharField("Полное название кафедры", max_length = 100)
	short_name = models.CharField("Аббревиатура кафедры", max_length = 10)
	url_name = models.CharField("Ссылка", max_length = 10)
	info = models.TextField("Информация о кафедре", blank = True)

	class Meta:
		verbose_name = "Кафедра"
		verbose_name_plural = "Кафедры"

	def __str__(self):
		return self.short_name

class Teacher(models.Model):
	user = models.OneToOneField(User, verbose_name = "Пользовательская страница", null = True, blank = True, on_delete = models.SET_NULL, related_query_name = "user")
	department = models.ForeignKey(Department, verbose_name = "Кафедра", on_delete = models.CASCADE, related_query_name = "department")
	name = models.CharField("Имя", max_length = 20)
	surname = models.CharField("Фамилия", max_length = 20)
	patronymic = models.CharField("Отчество", max_length = 20)
	image = models.ImageField("Фотография", default = "Prof.png", blank = True, upload_to = "Teachers/")
	rezume = models.TextField("Резюме", blank = True)
	phone = models.CharField("Телефон", max_length = 12, blank = True)
	email = models.EmailField("Почта", max_length=254, blank = True)
	post = models.CharField("Занимаемая должность", max_length = 100, blank = True)
	education = models.TextField("Образование", blank = True)
	qualification_up = models.TextField("Повышение квалификации", blank = True)
	science_articles = models.TextField("Научные статьи", blank = True)
	аwards = models.TextField("Награды", blank = True)
	
	class Meta:
		verbose_name = "Преподаватель"
		verbose_name_plural = "Преподаватели"

	def __str__(self):
		Full_name = self.surname +' '+ self.name +' '+ self.patronymic
		return Full_name

class Document(models.Model):
	CATEGORY = (
		('document' ,'Документ(Дипломы)'),
		('sertificat' ,'Скан сертификатов(повышение квалификации)'),
		('article' ,'Оттиск из статьи'),
		('award' ,'Награды'),
		)
	name = models.TextField("Описание документа")
	doc_name = models.ForeignKey(Teacher, verbose_name = "Кому принадлежит докумет", on_delete = models.CASCADE, related_query_name = "document_name")
	category = models.CharField("Категория", max_length = 10, choices = CATEGORY)
	file = models.FileField("Документ", upload_to = "Teachers/Documents/", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	
	class Meta:
		verbose_name = "Документ"
		verbose_name_plural = "Документы"

	def __str__(self):
		category = None
		if self.category == 'document':
			category = 'Документ(Дипломы)'
		elif self.category == 'sertificat':
			category = 'Скан сертификатов(повышение квалификации)'
		elif self.category == 'article':
			category = 'Оттиск из статьи'
		elif self.category == 'award':
			category = 'Награды'
		str_name = self.doc_name.surname +" "+self.doc_name.name +" "+self.doc_name.patronymic+ " ("+ self.file.name +") " + category
		return str_name

class Group(models.Model):
	department = models.ForeignKey(Department, verbose_name = "Кафедра", on_delete = models.CASCADE, related_query_name = "department")
	name = models.CharField("Название группы", max_length = 10)
	group_adviser = models.ForeignKey(Teacher, verbose_name = "Эдвайзер группы", on_delete = models.CASCADE, related_query_name = "group_adviser")

	class Meta:
		verbose_name = "Группа"
		verbose_name_plural = "Группы"

	def __str__(self):
		return self.name

class Student(models.Model):
	YEARS = (
		('1' ,'1'),
		('2' ,'2'),
		('3' ,'3'),
		('4' ,'4'),
		)

	name = models.CharField("Имя", max_length = 20)
	surname = models.CharField("Фамилия", max_length = 20)
	patronymic = models.CharField("Отчество", max_length = 20)
	group = models.ForeignKey(Group, verbose_name = "Группа", on_delete = models.CASCADE, related_query_name = "group")
	age = models.PositiveSmallIntegerField("Возраст", default = 0)
	study_year = models.CharField("Год обучения", max_length = 1, choices = YEARS)

	
	class Meta:
		verbose_name = "Студент"
		verbose_name_plural = "Студенты"

	def __str__(self):
		Full_name = self.surname +' '+ self.name +' '+ self.patronymic
		return Full_name