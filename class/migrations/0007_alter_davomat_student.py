# Generated by Django 4.1.1 on 2022-10-24 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_one_id'),
        ('class', '0006_alter_davomat_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='davomat',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', to_field='one_id'),
        ),
    ]
