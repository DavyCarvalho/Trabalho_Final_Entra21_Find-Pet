# Generated by Django 3.1.5 on 2021-02-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_historiasfelizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='eu_vi',
            name='house_number',
            field=models.CharField(default='', max_length=15),
        ),
    ]