# Generated by Django 3.0.6 on 2020-05-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='lecture_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
