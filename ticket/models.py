from django.db import models

PRIORITY_LIST={
        "UR": "Urgent",
        "ME": "Medium",
        "LO": "Low"
    }

STORY = {
        "Tec": "Technical Task",
        "Use": "User Story"
    }


class User(models.Model):
    name = models.CharField( max_length=20)
    phone = models.IntegerField()
    mail = models.EmailField()
    

# Create your models here.


class Ticket(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    deadline = models.DateField()
    assignees = models.ManyToManyField(
        User,  related_name="Users")
    subtasks = models.SlugField(null=True, blank=True)
    priority = models.CharField(max_length=50,choices=PRIORITY_LIST)
    category = models.CharField(max_length=50,choices=STORY)
