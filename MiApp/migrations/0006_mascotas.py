# Generated by Django 4.1 on 2022-08-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiApp', '0005_alter_familia_genero_alter_familia_relacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('especie', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
        ),
    ]