# Generated by Django 5.0.2 on 2024-03-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dancing_places', '0003_spot_address_alter_spot_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='spot',
            name='address',
            field=models.TextField(),
        ),
    ]
