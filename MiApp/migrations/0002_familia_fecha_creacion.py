# Generated by Django 4.1 on 2022-08-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='fecha_creacion',
            field=models.DateField(auto_now=True),
        ),
    ]