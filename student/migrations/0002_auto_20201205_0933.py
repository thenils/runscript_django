# Generated by Django 3.1.4 on 2020-12-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Age',
            field=models.CharField(max_length=3),
        ),
    ]
