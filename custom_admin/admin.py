from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'date',]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']