# Generated by Django 3.0 on 2021-05-12 08:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_contactinfo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsection',
            name='client_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='clientsection',
            name='client_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='clientsection',
            name='client_post',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='clientsection',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]