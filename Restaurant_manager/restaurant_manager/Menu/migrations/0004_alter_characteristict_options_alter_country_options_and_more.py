# Generated by Django 4.1.2 on 2023-01-12 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_rename_caracteristict_characteristict'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristict',
            options={'verbose_name': 'Characteristic', 'verbose_name_plural': 'Characteristics'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='ingredients',
            options={'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.AlterModelOptions(
            name='menu_items',
            options={'verbose_name': 'Menu item', 'verbose_name_plural': 'Menu items'},
        ),
    ]
