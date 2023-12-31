from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,),
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
