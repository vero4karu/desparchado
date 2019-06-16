# Generated by Django 2.0.13 on 2019-06-16 15:20

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190616_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressarticle',
            name='publication_date',
            field=models.DateTimeField(default=timezone.now, verbose_name='Fecha de publicación'),
            preserve_default=False,
        ),
    ]
