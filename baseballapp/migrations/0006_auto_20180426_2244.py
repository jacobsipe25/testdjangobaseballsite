# Generated by Django 2.0.3 on 2018-04-27 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseballapp', '0005_auto_20180426_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(choices=[('ARI', 'Diamondbacks')], max_length=600),
        ),
    ]
