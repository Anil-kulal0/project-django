# Generated by Django 4.1.6 on 2023-02-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('withinapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelname', models.CharField(max_length=100, verbose_name=' Model Name')),
                ('makeyear', models.CharField(max_length=10, verbose_name='Make Year')),
            ],
        ),
    ]
