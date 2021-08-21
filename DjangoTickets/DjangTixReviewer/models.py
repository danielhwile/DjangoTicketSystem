from django.db import models

# Create your models here.
class UserNames(models.Model):
    UserName = models.CharField(max_length=30)
class Tickets(models.Model):
    Owner = models.ForeignKey(UserNames, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=2000)
    CreateDate = models.DateField()
    DueDate = models.DateField()
    Status = models.CharField(max_length=30)
    IsClosed = models.BooleanField()
    RelevantUsers = models.CommaSeparatedIntegerField(max_length=1000)