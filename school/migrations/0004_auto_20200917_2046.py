# Generated by Django 3.1.1 on 2020-09-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200917_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='group',
            field=models.CharField(max_length=10, null=True, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='subject',
            field=models.CharField(max_length=10, null=True, verbose_name='Предмет'),
        ),
    ]
