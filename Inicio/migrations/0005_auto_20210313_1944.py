# Generated by Django 3.1.7 on 2021-03-14 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0004_auto_20210313_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anios_experiencia', models.IntegerField(default=0)),
                ('trabajadores', models.IntegerField(default=0)),
                ('clientes', models.IntegerField(default=0)),
                ('proyectos', models.IntegerField(default=0)),
                ('arquitectura', models.IntegerField(default=0)),
                ('construccion', models.IntegerField(default=0)),
                ('edificios', models.IntegerField(default=0)),
                ('interior', models.IntegerField(default=0)),
                ('comercial', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': '4. Dirección',
            },
        ),
        migrations.AddField(
            model_name='construlaba',
            name='valor',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]