# Generated by Django 3.1.4 on 2020-12-08 14:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0011_auto_20200229_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='can_edit_places', to=settings.AUTH_USER_MODEL),
        ),
    ]