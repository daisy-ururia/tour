from django.db import models

# Create your models here.
class contact2(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class searches(models.Model):
    select = models.CharField(max_length=20)
    daterange = models.DateField()
    people = models.IntegerField()

