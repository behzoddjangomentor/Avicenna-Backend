# Generated by Django 4.1.1 on 2022-09-28 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_options_alter_student_table'),
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter class name', max_length=100, verbose_name='Class name')),
                ('lesson_time', models.TextField(help_text='Enter lesson time', verbose_name='Lesson time')),
                ('student', models.ManyToManyField(to='students.student')),
                ('tuitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.tuitor')),
            ],
            options={
                'verbose_name': 'Classroom ',
                'verbose_name_plural': 'Classroom ',
                'db_table': 'ClassRoom',
            },
        ),
    ]
