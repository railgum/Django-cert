# Generated by Django 5.0.3 on 2024-03-12 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_eats', '0004_alter_recipe_cooking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]