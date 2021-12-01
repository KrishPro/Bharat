from django.db import models

# Create your models here.


class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=50)
    Content = models.TextField()
    Time = models.DateField(auto_now=True)

    def __str__(self):
        return  self.Title + ' By ' + self.Author 

    