from django.db import models

# Create your models here.


class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=13)
    Email = models.CharField(max_length=100)
    Content = models.TextField()
    Time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Message From ' + self.Name + ' - ' + self.Email 

    