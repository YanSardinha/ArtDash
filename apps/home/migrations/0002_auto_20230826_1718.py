# Generated by Django 3.2.13 on 2023-08-26 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dw_artigos',
            name='autores',
        ),
        migrations.AddField(
            model_name='dw_artigos',
            name='autores',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.dw_autor'),
            preserve_default=False,
        ),
    ]
