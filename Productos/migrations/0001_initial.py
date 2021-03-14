# Generated by Django 3.1.7 on 2021-03-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField(default=0)),
                ('resistencia', models.CharField(blank=True, max_length=50, null=True)),
                ('detalle', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Productos',
            },
        ),
    ]
