# Generated by Django 3.0.6 on 2020-05-26 08:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.TextField()),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.Task')),
            ],
        ),
    ]
