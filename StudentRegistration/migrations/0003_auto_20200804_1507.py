# Generated by Django 2.1.7 on 2020-08-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentRegistration', '0002_auto_20200804_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='Course_applied',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='Course_applied',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='Gender',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='Gender',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]
