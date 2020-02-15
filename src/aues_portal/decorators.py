from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def authenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_anonymous:
			return HttpResponse('Ошибка доступа')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def allowed_users(allowed_roles):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			groups = None
			if request.user.groups.exists():
				groups = request.user.groups.all()
				groups_name = []
				for group in groups:
					groups_name.append(group.name)
			if allowed_roles in groups_name:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('Ошибка доступа')
		return wrapper_func
	return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		'''if group == 'customer':
			return redirect('user-page')'''
		if group == 'admin':
			return view_func(request, *args, **kwargs)
	return wrapper_function