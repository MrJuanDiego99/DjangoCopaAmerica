# Generated by Django 5.0.6 on 2024-07-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
