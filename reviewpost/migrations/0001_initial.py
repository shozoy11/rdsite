# Generated by Django 3.2.6 on 2021-10-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name='ユーザー名')),
                ('bet', models.IntegerField(default=5000, verbose_name='ベット上限金額')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='最終更新日')),
            ],
            options={
                'verbose_name': 'ユーザー管理',
                'verbose_name_plural': 'ユーザー管理',
            },
        ),
    ]
