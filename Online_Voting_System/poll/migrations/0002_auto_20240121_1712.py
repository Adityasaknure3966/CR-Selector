# Generated by Django 2.2.7 on 2024-01-21 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
