from django.db import models

# Create your models here.
class gallery(models.Model):
  Url = models.URLField(null=True)
  