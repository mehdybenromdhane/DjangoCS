# Generated by Django 4.2 on 2024-11-18 19:23

import Person.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person'},
        ),
        migrations.AlterField(
            model_name='person',
            name='cin',
            field=models.CharField(max_length=8, primary_key=True, serialize=False, validators=[Person.models.validate_cin]),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=100, validators=[Person.models.validate_email]),
        ),
    ]