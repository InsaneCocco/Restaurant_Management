# Generated by Django 4.1.2 on 2022-12-22 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_list',
            name='unit_id',
        ),
    ]
