# Generated by Django 3.0.1 on 2021-09-01 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('masivo', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=70)),
                ('horas_total', models.IntegerField()),
                ('porc_establecido', models.IntegerField()),
            ],
        ),
    ]
