# Generated by Django 3.0 on 2019-12-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
