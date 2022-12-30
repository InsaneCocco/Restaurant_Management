# Generated by Django 4.1.2 on 2022-12-30 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_alter_ingredients_country_alter_menu_items_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='Menu.country'),
        ),
        migrations.AlterField(
            model_name='menu_items',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='Menu.country'),
        ),
    ]
