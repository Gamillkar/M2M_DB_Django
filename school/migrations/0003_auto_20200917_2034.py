# Generated by Django 3.1.1 on 2020-09-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200917_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.CharField(default=2, max_length=10, verbose_name='Класс'),
            preserve_default=False,
        ),
    ]