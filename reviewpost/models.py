from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class ReviewModel(models.Model):
    user_name = models.CharField(
        max_length=30 , verbose_name="ユーザー名",
        blank=True,
        null=True,        
        )
    user = models.CharField(max_length=50, verbose_name="MACアドレス")
    
    bet = models.IntegerField(default=5000, verbose_name="ベット上限金額")

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False,
        verbose_name="作成日")
    
    updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
        verbose_name="最終更新日")

    class Meta:
        verbose_name = 'ユーザー管理'
        verbose_name_plural = 'ユーザー管理'
