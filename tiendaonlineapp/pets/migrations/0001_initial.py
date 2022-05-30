# Generated by Django 4.0.4 on 2022-05-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('value', models.FloatField(default=0)),
                ('image', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
