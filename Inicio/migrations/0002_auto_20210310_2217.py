# Generated by Django 3.1.7 on 2021-03-11 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Construlaba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon_1', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('favicon_2', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo_horizontal_1', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='favicon')),
                ('logo_horizontal_2', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('celular2', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('nosotros', models.TextField(blank=True, max_length=500, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='construlaba')),
            ],
            options={
                'verbose_name_plural': '1. Vortice',
            },
        ),
        migrations.DeleteModel(
            name='Vortice',
        ),
        migrations.RemoveField(
            model_name='contacto_redes',
            name='behance',
        ),
    ]
