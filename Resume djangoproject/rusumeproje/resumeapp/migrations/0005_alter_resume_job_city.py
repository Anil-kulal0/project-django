# Generated by Django 4.1.5 on 2023-08-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_alter_resume_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='job_city',
            field=models.CharField(choices=[('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Kolkatta', 'Kolkatta'), ('Ranchi', 'Ranchi')], max_length=100, verbose_name='Job City'),
        ),
    ]
