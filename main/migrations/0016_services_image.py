# Generated by Django 3.0 on 2021-05-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210508_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
