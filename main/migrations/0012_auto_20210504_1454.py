# Generated by Django 3.0 on 2021-05-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210430_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatweoffer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]