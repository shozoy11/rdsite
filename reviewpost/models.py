from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ReviewModel(models.Model):
    user = models.CharField(max_length=50)
    bet = models.IntegerField(default=0)
