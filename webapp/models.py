from django.db import models

# Create your models here.

class courses(models.Model):
	coursename = models.CharField(max_length=50)
	coursedesc = models.CharField(max_length=50)
	courseid = models.IntegerField()


	def __str__(self):
		return self.coursename


