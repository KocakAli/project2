# Generated by Django 3.2.5 on 2021-08-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210803_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.CharField(max_length=256),
        ),
    ]