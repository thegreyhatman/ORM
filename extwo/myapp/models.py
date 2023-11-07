from django.db import models
from django.contrib import admin
class Football (models.Model):
    Place=models.CharField(max_length=20,help_text="Employee ID")
    name=models.CharField(max_length=100)
    Pskill=models.IntegerField()
    age=models.IntegerField()
    Jersynumber=models.IntegerField()

class FootballAdmin(admin.ModelAdmin):
    list_display=('Place','name','Pskill','age','Jersynumber')
