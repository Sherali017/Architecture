# Generated by Django 3.2.5 on 2021-09-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210909_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(default=None, max_length=100),
        ),
    ]