# Generated by Django 4.1.3 on 2022-11-07 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='new_field',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
    ]