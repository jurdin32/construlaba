# Generated by Django 3.1.7 on 2021-03-14 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0004_proyectos_tipo_proyecto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyectos',
            options={'verbose_name_plural': '2. Proyectos'},
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]