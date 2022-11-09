from django.db import models

# Create your models here.


class Book(models.Model):

    def __str__(self):
        return self.Name

    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')
    Rating = models.FloatField()
    Description = models.CharField(max_length=500)
    Category = models.CharField(max_length=200)
