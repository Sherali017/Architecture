# Generated by Django 3.2.5 on 2021-09-09 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_categorymodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.categorymodel'),
        ),
    ]
