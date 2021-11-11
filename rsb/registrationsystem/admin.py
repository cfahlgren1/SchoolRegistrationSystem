from django.contrib import admin
from registrationsystem.models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'crn')
    search_fields = ['name', 'crn']

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Course, CourseAdmin)