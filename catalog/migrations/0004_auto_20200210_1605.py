# Generated by Django 2.2.6 on 2020-02-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200210_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
