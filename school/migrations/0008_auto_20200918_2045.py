# Generated by Django 3.1.1 on 2020-09-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20200918_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(default=2, max_length=10, verbose_name='Предмет'),
            preserve_default=False,
        ),
    ]
