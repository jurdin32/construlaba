# Generated by Django 3.1.7 on 2021-03-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0006_auto_20210314_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='video_youtube',
            field=models.CharField(blank=True, help_text='link de video youtube', max_length=120, null=True),
        ),
    ]
