from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()

    def str(self):
        return "Project Page"