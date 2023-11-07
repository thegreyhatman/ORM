# Ex02 Django ORM Web Application
## Date: 7/11/2023

## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM

```
Model.py

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

admin.py

from django.contrib import admin
from .models import Football,FootballAdmin
admin.site.register(Football,FootballAdmin)
```

## OUTPUT
![Alt text](<Screenshot (21).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
