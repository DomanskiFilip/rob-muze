# Generated by Django 4.1.10 on 2023-07-28 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampel',
            name='cena',
            field=models.IntegerField(default=30),
        ),
    ]
