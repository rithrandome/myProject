# Generated by Django 2.1.7 on 2020-08-06 11:41

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('StudentRegistration', '0005_auto_20200806_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='Hobbies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Drawing', 'Drawing'), ('Singing', 'Singing'), ('Dancing', 'Dancing'), ('Cooking', 'Cooking'), ('Others', 'Others')], max_length=38),
        ),
    ]
