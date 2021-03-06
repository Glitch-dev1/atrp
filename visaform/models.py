from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class VisaModel(models.Model):
  genderchoices = (
      ('male','male'),
      ('female', 'female')
    )
  rpexpchoices = (
      ('new', 'New to Roleplay'),
      ('1m', '1 Month'),
      ('5m', '5 months'),
      ('1y', '1 year'),
      ('a1y', 'Above 1 year')
    )
  user = models.TextField(null=True, blank=True)
  realname = models.CharField(max_length=25, null=True)
  gender = models.CharField(choices=genderchoices, max_length=10, default='male')
  realage = models.IntegerField(null=True)
  rprules = models.BooleanField(null=True)
  igname = models.CharField(max_length=25, null=True)
  igage = models.IntegerField(null=True)
  iggender = models.CharField(choices=genderchoices, max_length=10, default='male')
  rpexp = models.CharField(choices=rpexpchoices, max_length=20, null=True)
  discordname = models.CharField(max_length=50, null=True)
  characterstory = models.TextField(null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
class Profile(models.Model):
  
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to= 'avatar/% Y/% m/% d/', default="https://media.discordapp.net/attachments/569806298120454146/878466555481059398/image_downloader_1629513127513.png", null=True)

