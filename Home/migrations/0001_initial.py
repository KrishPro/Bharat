# Generated by Django 3.0 on 2019-12-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Sno', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=13)),
                ('Email', models.CharField(max_length=100)),
                ('Content', models.TextField()),
            ],
        ),
    ]
