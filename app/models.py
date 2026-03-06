from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ph_no = models.CharField(max_length=10)
    skills = models.TextField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name
