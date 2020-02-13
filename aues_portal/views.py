from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import *

# Create your views here.
def logoutuser(request):
	logout(request)
	return redirect('login')

def main(request):
	return render(request, 'html/dashboard.html')

def instituts(request):
	instituts = Institute.objects.all()
	context = {'instituts':instituts,
	}
	return render(request, 'html/instituts.html', context)

def institut(request, inst_url):
	institut = Institute.objects.get(url_name = inst_url)
	departments = Department.objects.filter(institute__url_name = inst_url)
	context = {'institut':institut,
	'departments':departments,
	}
	return render(request, 'html/institut.html', context)

def institut_list(request, inst_url):
	institut = Institute.objects.all()
	context = {'institut_list':institut,
	}
	return render(request, 'html/navbar.html', context)

def departments(request):
	instituts = Institute.objects.all()
	departments = Department.objects.all()
	context = {'departments':departments,
	'instituts':instituts,
	}
	return render(request, 'html/departments.html', context)

def department(request, dep_url):
	department = Department.objects.get(url_name = dep_url)
	teachers = Teacher.objects.filter(department__url_name = dep_url)
	groups = Group.objects.filter(department__url_name = dep_url)
	context = {'department':department,
	'teachers':teachers,
	'groups':groups,
	}
	return render(request, 'html/department.html', context)

def pps(request):
	instituts = Institute.objects.all()
	departments = Department.objects.all()
	teachers = Teacher.objects.all()
	context = {'teachers':teachers,
	'departments':departments,
	'instituts':instituts,
	}
	return render(request, 'html/pps.html', context)

def teacher(request, teach):
	teacher = Teacher.objects.get(id = teach)
	doc = Document.objects.filter(doc_name_id = teach)
	context = {'teacher':teacher,
	"doc":doc,
	}
	return render(request, 'html/teacher.html', context)

@unauthenticated_user
def loginpage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Неправильный логин или пароль')
	return render(request, 'html/login.html')

@authenticated_user
def groups(request):
	groups = Group.objects.all()
	instituts = Institute.objects.all()
	departments = Department.objects.all()
	context = {'groups':groups,
	'departments':departments,
	'instituts':instituts,
	}
	return render(request, 'html/groups.html', context)

@authenticated_user
def group(request, group_id):
	group = Group.objects.get(id = group_id)
	adviser_id = Teacher.objects.get(id = group_id)
	students = Student.objects.filter(group_id = group_id)
	context = {'group':group,
	'students':students,
	'adviser_id':adviser_id,
	}
	return render(request, 'html/group.html', context)

@authenticated_user
def student(request, pk):
	student = Student.objects.get(id = pk)
	context = {'student':student,
	}
	return render(request, 'html/student.html', context)

@authenticated_user
def user(request):
	teacher = request.user.teacher
	form = TeacherForm(instance = teacher)
	if request.method == 'POST':
		form = TeacherForm(request.POST, request.FILES, instance = teacher)
		if form.is_valid():
			form.save()
	context = {'form':form,
	}
	return render(request, 'html/user.html', context)

@authenticated_user
def documents(request):
	document = Document.objects.all()
	context = {'document':document,
	}
	return render(request, 'html/documents.html', context)

@authenticated_user
def doc_add(request):
	form = DocumentForm()
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('documents')
	context = {'form':form,
	}
	return render(request, 'html/doc_add.html', context)

@authenticated_user
def doc_upd(request, doc_id):
	doc = Document.objects.get(id = doc_id)
	form = DocumentForm(instance = doc)
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES, instance = doc)
		if form.is_valid():
			form.save()
			return redirect('documents')
	context = {'form':form,
	'doc':doc
	}
	return render(request, 'html/doc_upd.html', context)

@authenticated_user
def doc_del(request, doc_id):
	doc = Document.objects.get(id = doc_id)
	if request.method == 'POST':
		doc.delete()
	return redirect('documents')
#@allowed_users(allowed_roles = ['группа']) Доступ по группе