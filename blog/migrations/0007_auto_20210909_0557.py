# Generated by Django 3.2.5 on 2021-09-09 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210909_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.categorymodel'),
        ),
    ]
