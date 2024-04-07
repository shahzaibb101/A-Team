from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TaskList(models.Model):
	manage = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=None, null= True)

	task = models.CharField(max_length=300)
	done = models.BooleanField(default=False)
	taskDescription = models.TextField(null = True)
	task_Assign_Date = models.DateField(default = date.today)
	deadline = models.DateField(null = True)
	importance = models.IntegerField(default = 0)

	def __str__(self):
		return self.task + "-" + str(self.done)