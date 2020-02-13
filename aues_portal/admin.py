from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Institute)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Document)