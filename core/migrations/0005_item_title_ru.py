# Generated by Django 3.1.1 on 2021-02-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210210_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='title_ru',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
