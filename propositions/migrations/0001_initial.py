# Generated by Django 3.1.1 on 2021-02-06 14:47

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, verbose_name='Название тэга')),
                ('tag_eng_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Название тэга')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Заголовок')),
                ('title_eng', models.CharField(blank=True, max_length=80, null=True, verbose_name='Заголовок eng')),
                ('date_added', models.DateField(auto_now=True)),
                ('proposition_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', tinymce.models.HTMLField()),
                ('description_eng', tinymce.models.HTMLField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('tag', models.ManyToManyField(to='propositions.Tag')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
                'ordering': ['-date_added'],
            },
        ),
    ]