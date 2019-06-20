from django.db import models
# Cre
# from __future__ import unicode_literalsate your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    sex = models.CharField(max_length=32)
    school = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)