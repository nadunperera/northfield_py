# Generated by Django 2.2 on 2019-04-29 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stay',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stay',
            name='checkout',
            field=models.DateField(blank=True, null=True),
        ),
    ]
