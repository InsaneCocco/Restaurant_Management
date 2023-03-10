# Generated by Django 4.1.2 on 2023-01-01 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='Menu.country')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingr_name', models.CharField(max_length=20)),
                ('ingr_type', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='Menu.country')),
            ],
        ),
    ]
