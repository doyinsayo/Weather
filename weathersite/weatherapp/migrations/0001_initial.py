# Generated by Django 3.0.8 on 2020-08-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('postcode', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
    ]
