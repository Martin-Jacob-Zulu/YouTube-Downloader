from django.db import models


class Jumbotron(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    footer = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Guide(models.Model):
    stet_count = models.CharField(max_length=100)
    header = models.CharField(max_length=50)
    stet_description = models.TextField()
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
