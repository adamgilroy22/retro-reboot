# Generated by Django 3.2.19 on 2023-06-26 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]