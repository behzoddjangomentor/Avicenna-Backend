# Generated by Django 4.1.1 on 2022-10-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_bloktestlar_fantest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloktestlar',
            options={'verbose_name': 'Blok Testlar', 'verbose_name_plural': 'Blok Testlar'},
        ),
        migrations.AlterModelOptions(
            name='fantest',
            options={'verbose_name': 'Fan Testlar', 'verbose_name_plural': 'Fan Testlar'},
        ),
        migrations.RenameField(
            model_name='fantest',
            old_name='fan',
            new_name='togri_javoblar',
        ),
        migrations.AlterField(
            model_name='bloktestlar',
            name='fan_nomi',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='bloktestlar',
            name='test_kodi',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='fantest',
            name='fan_nomi',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='fantest',
            name='test_kodi',
            field=models.CharField(max_length=600),
        ),
    ]
