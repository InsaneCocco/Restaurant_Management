# Generated by Django 4.1.2 on 2022-12-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_sellM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dish', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField()),
                ('Table', models.IntegerField()),
            ],
        ),
    ]
