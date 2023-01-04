# Generated by Django 4.1.2 on 2023-01-03 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Caracteristict', to='Menu.menu_items')),
            ],
        ),
    ]