from django.db import models


# Create your models here.

class Cources(models.Model):
    courseServer_id = models.CharField(max_length=10)
    date = models.CharField(max_length=50)

    modified = models.CharField(max_length=50)

    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000, blank=True)
    contentProtected = models.BooleanField(max_length=10)


class Author(models.Model):
    AuthorData = models.ForeignKey(Cources, on_delete=models.CASCADE, related_name='AuthorData', blank=True)
    AuthorServer_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=10000)
    url = models.CharField(max_length=500)
