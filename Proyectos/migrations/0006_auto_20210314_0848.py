# Generated by Django 3.1.7 on 2021-03-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0005_auto_20210313_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='imagen_5',
            field=models.ImageField(blank=True, help_text='360x360', null=True, upload_to='proyectos'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='imagen_6',
            field=models.ImageField(blank=True, help_text='360x360', null=True, upload_to='proyectos'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='imagen_centro',
            field=models.ImageField(blank=True, help_text='500x360', null=True, upload_to='proyectos'),
        ),
    ]