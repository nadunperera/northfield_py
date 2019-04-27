# Generated by Django 2.2 on 2019-04-27 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bill_from', models.DateField()),
                ('bill_to', models.DateField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_end', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
            ],
        ),
    ]