from django.db import models

# Create your models here.
class FacModel(models.Model):
  skillchoices = (
      ('Beginner', 'Beginner'),
      ('Intermediate', 'Intermediate'),
      ('Expert', 'Expert'),
    )
  facchoices = (
      ('PD', '👮 Police Department 👮'),
      ('EMS', '🏥 Medical Department 🏥'),
      ('FBI','🕵️ Federal Bureau Of Investigation 🕵️'),
      (' Mech' , '🛠️ Mechanic 🛠️'),
      ('News', '📰Department of News📰'),
    )
  user = models.TextField()
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  faction = models.CharField(max_length=160, choices=facchoices)
  qualification = models.CharField(max_length=200)
  """dskill = models.CharField(max_length=50, choices=skillchoices)
  sskill = models.CharField(max_length=50, choices= 
  skillchoices)"""
  wtime = models.CharField(max_length=200)
  exjob = models.CharField(max_length=300)
  date_created = models.DateTimeField(auto_now_add=True)

