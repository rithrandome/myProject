# Generated by Django 2.1.7 on 2020-08-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentRegistration', '0009_auto_20200807_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='Course_applied',
            field=models.CharField(choices=[('CSE', 'Computer Science Engg'), ('ECE', 'Electronics and Communication Engg'), ('MECH', 'Mechanical Engg'), ('EEE', 'Electrical and Electronics Engg'), ('ICE', 'Instrumentation and Control Engg'), ('CHEM', 'Chemical Engg'), ('META', 'Metalurgy Engg'), ('PROD', 'Production Engg'), ('CIVIL', 'Civil Engg')], max_length=30),
        ),
    ]
