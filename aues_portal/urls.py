from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.loginpage, name = "login"),
	path('logout/', views.logoutuser, name = "logout"),
	path('user/', views.user, name = "user"),
    path('user/documents', views.documents, name = "documents"),
    path('user/documents/add', views.doc_add, name = "doc_add"),
    path('user/document/<int:doc_id>', views.doc_upd, name = "doc_upd"),
    path('user/documents/delete/<int:doc_id>', views.doc_del, name = "doc_del"),

    path('', views.main, name = "home"),
    path('instituts/', views.instituts, name = "instituts"),
    path('institut/<str:inst_url>/', views.institut, name = "institut"),
    path('instituts/departments/', views.departments, name = "departments"),
    path('institut/department/<str:dep_url>', views.department, name = "department"),
    path('instituts/department/pps/', views.pps, name = "teachers"),
    path('instituts/department/pps/<int:teach>', views.teacher, name = "teacher"),
    path('instituts/department/groups/', views.groups, name = "groups"),
    path('instituts/department/group/<int:group_id>', views.group, name = "group"),
    path('instituts/department/student/<int:pk>/', views.student, name = "student"),

]