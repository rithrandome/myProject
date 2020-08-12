# Generated by Django 2.1.7 on 2020-08-07 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentRegistration', '0007_auto_20200807_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='Course_applied',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('MECH', 'MECH'), ('EEE', 'EEE'), ('ICE', 'ICE'), ('CHEM', 'CHEM'), ('META', 'META'), ('PROD', 'PROD'), ('CIVIL', 'CIVIL')], max_length=30),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='Hobbies',
            field=models.TextField(max_length=200),
        ),
    ]
