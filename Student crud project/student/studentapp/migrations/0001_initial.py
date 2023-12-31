# Generated by Django 4.1.5 on 2023-07-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=15, verbose_name='Student Name')),
                ('emailid', models.EmailField(max_length=20, verbose_name='Email_id')),
                ('rollno', models.TextField(max_length=5, verbose_name='Roll No')),
                ('contact', models.TextField(max_length=10, verbose_name='Contact')),
                ('course', models.CharField(max_length=20, verbose_name='Course')),
                ('bloodgroup', models.CharField(max_length=5, verbose_name='Blood Group')),
            ],
        ),
    ]
