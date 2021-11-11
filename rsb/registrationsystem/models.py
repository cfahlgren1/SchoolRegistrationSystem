from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    crn = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
