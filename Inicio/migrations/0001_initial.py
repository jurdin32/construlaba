# Generated by Django 3.1.7 on 2021-03-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_redes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('behance', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '8. Contácto Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, help_text='imagenes 500*900', null=True, upload_to='media')),
                ('titulo', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': '2. Slider',
            },
        ),
        migrations.CreateModel(
            name='Vortice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon_amarillo', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('favicon_negro', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo_horizontal', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='favicon')),
                ('logo_amarillo', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('logo_negro', models.ImageField(help_text='imagenes 20*20', upload_to='favicon')),
                ('representante', models.CharField(blank=True, max_length=100, null=True)),
                ('celular', models.CharField(blank=True, max_length=11, null=True)),
                ('celular2', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('nosotros', models.TextField(blank=True, max_length=500, null=True)),
                ('imagen', models.ImageField(blank=True, help_text='imagenes 20*20', null=True, upload_to='vortice')),
            ],
            options={
                'verbose_name_plural': '1. Vortice',
            },
        ),
    ]
