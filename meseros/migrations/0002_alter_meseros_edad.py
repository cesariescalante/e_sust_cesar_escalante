# Generated by Django 4.1.3 on 2022-12-16 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meseros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meseros',
            name='edad',
            field=models.IntegerField(max_length=2),
        ),
    ]
