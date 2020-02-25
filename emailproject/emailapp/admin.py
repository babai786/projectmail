from django.contrib import admin

# Register your models here.
from emailapp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','phone','address','email']

admin.site.register(Student,StudentAdmin)