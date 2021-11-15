from django.contrib import admin
from registrationsystem.models import Course, DropRequest, AddRequest, Professor, Student, GradeReport, EnrollmentSummary

# Mass accept requests
@admin.action(description="Accept Request")
def accept_request(modeladmin, request, queryset):
    for request in queryset:
        request.acceptRequest()  

# Mass deny requests
@admin.action(description="Deny Request")
def deny_request(modeladmin, request, queryset):
    for request in queryset:
        request.denyRequest()

# Set actions and fields to display in action
class RequestAdmin(admin.ModelAdmin):
    list_display = ['course', 'student']
    actions = [deny_request, accept_request]

# Set Fields for Admin Display for Course
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'crn', 'professor')
    search_fields = ['name', 'crn']

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(Course, CourseAdmin)
admin.site.register(DropRequest, RequestAdmin)
admin.site.register(AddRequest, RequestAdmin)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(GradeReport)
admin.site.register(EnrollmentSummary)