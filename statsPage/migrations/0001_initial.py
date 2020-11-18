# Generated by Django 3.1.2 on 2020-11-18 03:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=50)),
                ('lName', models.CharField(max_length=50)),
                ('homeTown', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('locationStreet', models.CharField(blank=True, max_length=50)),
                ('locationCity', models.CharField(max_length=50)),
                ('speedMPH', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='statsPage.driver')),
            ],
        ),
    ]