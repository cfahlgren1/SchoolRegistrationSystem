from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING

# Enrollment Summary
class EnrollmentSummary(models.Model):
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    report = models.TextField() # list of student names in course
    # have student name be added to enrollment when student adds

    def __str__(self):
        
        return str(self.date)

# Grade Report
class GradeReport(models.Model):
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    report = models.TextField() # professors names per grade

    def __str__(self):
        return str(self.date)
    
# Professor Model
class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollmentSummaries = models.ManyToManyField(EnrollmentSummary, blank=True)
    gradeReports = models.ManyToManyField(GradeReport, blank=True)

    def __str__(self):
        return self.name

# Course Model
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    professor = models.ForeignKey(Professor, on_delete=DO_NOTHING) #make this a one to many field
    crn = models.IntegerField()
    description = models.TextField(blank=True)
    enrollmentSummary = models.OneToOneField(EnrollmentSummary, on_delete=DO_NOTHING, blank=True, null=True)
    gradeReport = models.OneToOneField(GradeReport, on_delete=DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # delete this student account, if user deletes account
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name

# Drop Request
class DropRequest(models.Model):
    course = models.OneToOneField(Course, on_delete=DO_NOTHING)
    student = models.OneToOneField(Student, on_delete=DO_NOTHING)
    
    # Drop student from course
    def acceptRequest(self):
        # remove student from course
        self.student.courses.remove(self.course)
        #remove request when done
        super().delete()
    
    # Deny Request
    def denyRequest(self):
        super().delete()
    
    def __str__(self):
        return self.course.name

# Add Request
class AddRequest(models.Model):
    course = models.OneToOneField(Course, on_delete=DO_NOTHING)
    student = models.OneToOneField(Student, on_delete=DO_NOTHING)

    # Add student to course
    def acceptRequest(self):
        # add student to course
        self.student.courses.add(self.course)
        # delete request when done
        super().delete()

    # Delete Request 
    def denyRequest(self):
        super().delete()

    def __str__(self):
        return self.course.name
