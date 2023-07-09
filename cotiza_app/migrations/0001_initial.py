# Generated by Django 4.2.3 on 2023-07-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('descrip_falla', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'cotizacion_celu_django',
            },
        ),
    ]
