# Generated by Django 2.0.13 on 2019-04-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='special',
            name='subtitle',
            field=models.CharField(default='', max_length=500, verbose_name='Título'),
        ),
    ]