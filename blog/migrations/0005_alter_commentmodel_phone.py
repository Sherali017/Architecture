# Generated by Django 3.2.5 on 2021-09-08 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210714_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
