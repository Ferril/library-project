# Generated by Django 2.2.7 on 2019-11-22 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20191122_1923'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reader',
            unique_together={('first_name', 'last_name')},
        ),
    ]
