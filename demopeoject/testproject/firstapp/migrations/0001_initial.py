# Generated by Django 4.1.5 on 2023-01-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='username')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
            ],
        ),
    ]
