from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _
from django.utils import timezone
import datetime

# Create your models here.
class Institute(models.Model):
	name = models.CharField(_("Полное название института"), max_length = 100)
	short_name = models.CharField(_("Аббревиатура института"), max_length = 10)
	url_name = models.CharField(_("Ссылка"), max_length = 10)
	info = models.TextField(_("Информация об институте"), blank = True)
	
	class Meta:
		verbose_name = _("Институт")
		verbose_name_plural = _("Институты")

	def __str__(self):
		return self.short_name

class Department(models.Model):
	institute = models.ForeignKey(Institute, verbose_name = _("Институт"), on_delete = models.CASCADE, related_query_name = "institute")
	name = models.CharField(_("Полное название кафедры"), max_length = 100)
	short_name = models.CharField(_("Аббревиатура кафедры"), max_length = 10)
	url_name = models.CharField(_("Ссылка"), max_length = 10)
	info = models.TextField(_("Информация о кафедре"), blank = True)
	release = models.BooleanField(_("Выпуск групп"))

	class Meta:
		verbose_name = _("Кафедра")
		verbose_name_plural = _("Кафедры")

	def __str__(self):
		return self.short_name

class Teacher(models.Model):
	user = models.OneToOneField(User, verbose_name = _("Пользовательская страница"), null = True, blank = True, on_delete = models.SET_NULL, related_query_name = "user")
	department = models.ForeignKey(Department, verbose_name = _("Кафедра"), on_delete = models.CASCADE, related_query_name = "department")
	name = models.CharField(_("Имя"), max_length = 20)
	surname = models.CharField(_("Фамилия"), max_length = 20)
	patronymic = models.CharField(_("Отчество"), max_length = 20)
	image = models.ImageField(_("Фотография"), default = "Prof.png", blank = True, upload_to = "images/")
	rezume = models.TextField(_("Резюме"), blank = True)
	phone = models.CharField(_("Телефон"), max_length = 12, blank = True)
	email = models.EmailField(_("Почта"), max_length=254, blank = True)
	post = models.CharField(_("Занимаемая должность"), max_length = 100, blank = True)
	education = models.TextField(_("Образование"), blank = True)
	qualification_up = models.TextField(_("Повышение квалификации"), blank = True)
	science_articles = models.TextField(_("Научные статьи"), blank = True)
	аwards = models.TextField(_("Награды"), blank = True)
	
	class Meta:
		verbose_name = _("Преподаватель")
		verbose_name_plural = _("Преподаватели")

	def __str__(self):
		Full_name = self.surname +' '+ self.name +' '+ self.patronymic
		return Full_name

class Document(models.Model):
	CATEGORY = (
		('document', _('Документ(Дипломы)')),
		('sertificat', _('Скан сертификатов(повышение квалификации)')),
		('article', _('Оттиск из статьи')),
		('award', _('Награды')),
		)
	name = models.TextField(_("Описание документа"))
	doc_name = models.ForeignKey(Teacher, verbose_name = _("Кому принадлежит докумет"), on_delete = models.CASCADE, related_query_name = "document_name")
	category = models.CharField(_("Категория"), max_length = 10, choices = CATEGORY)
	file = models.FileField(_("Документ"), upload_to = 'Documents/' , validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	
	class Meta:
		verbose_name = _("Документ")
		verbose_name_plural = _("Документы")

	def __str__(self):
		category = None
		if self.category == 'document':
			category = _('Документ(Дипломы)')
		elif self.category == 'sertificat':
			category = _('Скан сертификатов(повышение квалификации)')
		elif self.category == 'article':
			category = _('Оттиск из статьи')
		elif self.category == 'award':
			category = _('Награды')
		str_name = self.doc_name.surname +" "+self.doc_name.name +" "+self.doc_name.patronymic+ " ("+ self.file.name +") " + category
		return str_name

class Group(models.Model):
	department = models.ForeignKey(Department, verbose_name = _("Кафедра"), on_delete = models.CASCADE, related_query_name = "department")
	name = models.CharField(_("Название группы"), max_length = 10)
	group_adviser = models.ForeignKey(Teacher, verbose_name = _("Эдвайзер группы"), on_delete = models.CASCADE, related_query_name = "group_adviser")
	study_start = models.DateField(_("Дата начала обучения группы"))

	class Meta:
		verbose_name = _("Группа")
		verbose_name_plural = _("Группы")

	def __str__(self):
		return self.name

	def studyYear(self):
		if self.study_start <= (datetime.date.today() - datetime.timedelta(days = 365*4)):
			return False
		elif self.study_start <= (datetime.date.today() - datetime.timedelta(days = 365*3)):
			return 4
		elif self.study_start <= (datetime.date.today() - datetime.timedelta(days = 365*2)):
			return 3
		elif self.study_start <= (datetime.date.today() - datetime.timedelta(days = 365)):
			return 2
		else:
			return 1

class Student(models.Model):
	name = models.CharField(_("Имя"), max_length = 20)
	surname = models.CharField(_("Фамилия"), max_length = 20)
	patronymic = models.CharField(_("Отчество"), max_length = 20)
	group = models.ForeignKey(Group, verbose_name = _("Группа"), on_delete = models.CASCADE, related_query_name = "group")

	class Meta:
		verbose_name = _("Студент")
		verbose_name_plural = _("Студенты")

	def __str__(self):
		Full_name = self.surname +' '+ self.name +' '+ self.patronymic
		return Full_name