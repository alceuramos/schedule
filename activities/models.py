from django.db import models
from datetime import datetime

# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,null=True)
    author = models.CharField(max_length=50,null=True)
    create_date = models.DateField(default=datetime.now,null=True)
    last_edit_date = models.DateField(null=True)
    # class Meta:
    #     abstract = True

class Event(Activity):
    activity_id = models.OneToOneField(Activity, on_delete=models.CASCADE, primary_key=True)
    event_details = models.CharField(max_length = 100,null=True)
class Task(Activity):
    activity_id = models.OneToOneField(Activity, on_delete=models.CASCADE, primary_key=True)
    task_details = models.CharField(max_length = 100,null=True)
class Routine(Activity):
    activity_id = models.OneToOneField(Activity, on_delete=models.CASCADE, primary_key=True)
    routine_details = models.CharField(max_length = 100,null=True)