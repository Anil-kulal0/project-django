# Generated by Django 4.1.6 on 2023-08-17 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0002_alter_resume_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='mobail',
            new_name='mobile',
        ),
    ]
