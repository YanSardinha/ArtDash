# Generated by Django 3.2.13 on 2023-08-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dw_autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='dw_artigos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('curso', models.CharField(max_length=100)),
                ('orientador', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('autores', models.ManyToManyField(to='home.dw_autor')),
            ],
        ),
    ]
