# Generated by Django 4.2.1 on 2023-05-26 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
