from django.db import models

# Create your models here.
class UserNames(models.Model):
    UserName = models.CharField(max_length=30)
    def __str__(self):
        return self.UserName
class Tickets(models.Model):

    Owner = models.ForeignKey(UserNames, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=2000)
    CreateDate = models.DateField()
    DueDate = models.DateField()
    IsClosed = models.BooleanField()
    RelevantUsers = models.CharField(max_length=1000)
    class Meta:
        ordering = ["Owner"]