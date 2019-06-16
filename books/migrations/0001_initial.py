# Generated by Django 2.0.13 on 2019-06-16 17:33

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0003_pressarticle_publication_date'),
        ('events', '0016_auto_20190616_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='books/book', verbose_name='Background Image')),
                ('isbn', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator('\\d{13}')])),
                ('is_published', models.BooleanField(default=True, help_text='Indica si el libro va a aparecer en la página', verbose_name='Está publicado')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('press_articles', models.ManyToManyField(blank=True, related_name='books', to='news.PressArticle', verbose_name='Artículos de prensa')),
                ('related_events', models.ManyToManyField(blank=True, related_name='books', to='events.Event')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
