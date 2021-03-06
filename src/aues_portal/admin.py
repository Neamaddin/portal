from django.contrib import admin
from django.utils.translation import gettext as _
from .models import *


admin.site.site_header = _('Администрирование Портала')
admin.site.index_title = _('Администрирование Портала')
admin.site.site_title = _('АУЭС')

class GroupInline(admin.TabularInline):
	exclude = ['department', 'name']
	model = Group
	extra = 1

class StudentInline(admin.TabularInline):
	exclude = ['name', 'surname', 'patronymic']
	model = Student
	extra = 1

class DocumentInline(admin.TabularInline):
	exclude = ['name']
	model = Document
	extra = 1

class StudyYearFilter(admin.SimpleListFilter):
	title = _('Курс обучения')
	parameter_name = 'study_start'

	def lookups(self, request, model_admin):
		return (
			('1', _('Первый курс')),
			('2', _('Второй курс')),
			('3', _('Третий курс')),
			('4', _('Четвертый курс')),
			('end_study', _('Выпустившиеся группы')),
		)

	def queryset(self, request, queryset):
		today = datetime.date.today()
		if self.value() == '1':
			return queryset.filter(study_start__gte=today - datetime.timedelta(days = 365))
		if self.value() == '2':
			return queryset.filter(study_start__gte=today - datetime.timedelta(days = 365*2), study_start__lte=today - datetime.timedelta(days = 365+1))
		if self.value() == '3':
			return queryset.filter(study_start__gte=today - datetime.timedelta(days = 365*3), study_start__lte=today - datetime.timedelta(days = 365*2+1))
		if self.value() == '4':
			return queryset.filter(study_start__gte=today - datetime.timedelta(days = 365*4), study_start__lte=today - datetime.timedelta(days = 365*3+1))
		if self.value() == 'end_study':
			return queryset.filter(study_start__lte=today - datetime.timedelta(days = 365*4+1))

def depars_by_inst_id(inst_id):
	class DepartmentsFilter(admin.SimpleListFilter):
		inst = Institute.objects.get(id = inst_id)
		title = _("Кафедры " + inst.short_name + "-а")
		parameter_name = "department"

		def lookups(self, request, model_admin):
			list_of_department = []
			department = Department.objects.filter(institute__id = inst_id)
			for depar in department:
				list_of_department.append((str(depar.id), depar.short_name))
			return sorted(list_of_department, key = lambda tp:tp[1])

		def queryset(self, request, queryset):
			if self.value():
				return queryset.filter(department = self.value())
			return queryset
	return DepartmentsFilter

def depars_rel_by_inst_id(inst_id):
	class DepartmentReleaseFilter(admin.SimpleListFilter):
		inst = Institute.objects.get(id = inst_id)
		title = _("Кафедры " + inst.short_name + "-а")
		parameter_name = "department_first"

		def lookups(self, request, model_admin):
			list_of_department = []
			department = Department.objects.filter(institute__id = inst_id)
			for depar in department:
				if depar.release == True:
					list_of_department.append((str(depar.id), depar.short_name))
			return sorted(list_of_department, key = lambda tp:tp[1])

		def queryset(self, request, queryset):
			if self.value():
				return queryset.filter(department = self.value())
			return queryset
	return DepartmentReleaseFilter

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
	exclude = ['name', 'short_name', 'info']
	list_display = ("short_name", "name")

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
	exclude = ['name', 'short_name', 'info']
	list_display = ("short_name", "name")
	search_fields = ("name", "short_name")
	list_filter = ("institute",)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	exclude = ['name', 'surname', 'patronymic', 'rezume', 'post', 'education', 'qualification_up', 'science_articles', 'аwards']
	list_display = ("__str__", "department")
	list_filter = (depars_by_inst_id(3), )
	search_fields = ("name", "surname", "patronymic")
	inlines = [DocumentInline, GroupInline]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
	exclude = ['name']
	list_display = ("name", "department", "group_adviser")
	list_filter = (depars_rel_by_inst_id(3), StudyYearFilter)
	search_fields = ("name",)
	inlines = [StudentInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	exclude = ['name', 'surname', 'patronymic']
	list_display = ("__str__", "group")
	search_fields = ("name", "surname", "patronymic", "group__name")

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
	exclude = ['name', 'short_name', 'info']
	list_display = ("name", "doc_name", "category")
	list_filter = ("category",)
	search_fields = ("name", "doc_name__name", "doc_name__surname", "doc_name__patronymic")