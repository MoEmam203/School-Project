# Generated by Django 2.2.7 on 2020-02-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0003_auto_20200212_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]