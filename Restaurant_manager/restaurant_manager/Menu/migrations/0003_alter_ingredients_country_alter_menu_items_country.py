# Generated by Django 4.1.2 on 2022-12-30 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_country_ingredients_menu_items_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='Menu.country'),
        ),
        migrations.AlterField(
            model_name='menu_items',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='Menu.country'),
        ),
    ]
