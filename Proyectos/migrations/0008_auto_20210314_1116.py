# Generated by Django 3.1.7 on 2021-03-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0007_proyectos_video_youtube'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectos',
            name='anio',
        ),
        migrations.AddField(
            model_name='proyectos',
            name='nombre_proyecto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
