# Generated by Django 5.0.3 on 2024-03-11 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_eats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='categories',
        ),
        migrations.AddField(
            model_name='recipe',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='good_eats.category'),
        ),
    ]
