from django.db import models

# Create your models here.
from django.db import models

class Experience(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    position = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    office_name = models.CharField(max_length=100)
    experience_description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.office_name}"


class Education(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    address = models.CharField(max_length=255)
    description = models.TextField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.position} ({self.from_date} - {self.to_date})"


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name