from django.db import models

# Create your models here.
#paradigm
class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Language
class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Programmer
class Programmer(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name