from django.db import models

# How are these GPT generated models LMAO
class User(models.Model):
    email = models.EmailField(max_length=50, primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=32)

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=50)
    task_desc = models.CharField(max_length=255)
    deadline = models.DateField()
    importance = models.IntegerField()
    is_complete = models.BooleanField()
    completion_date = models.DateField()

    class Meta:
        unique_together = (('task_id', 'user'),)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=0)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = (('task', 'user'),)

class Work_Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    technique = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('session_id', 'user', 'task'),)

class Admin(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

