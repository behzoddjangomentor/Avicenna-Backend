# Generated by Django 4.1.1 on 2022-10-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_options_alter_student_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='one_id',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
