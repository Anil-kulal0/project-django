# Generated by Django 4.1.5 on 2023-06-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='contact',
            field=models.IntegerField(verbose_name='Contact'),
        ),
    ]
