# Generated by Django 3.0 on 2021-05-08 07:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_services_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
