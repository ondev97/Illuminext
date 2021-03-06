# Generated by Django 3.0 on 2021-05-08 06:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_whatweofferobjects_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=300, null=True)),
                ('project_name', models.CharField(blank=True, max_length=300, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services_heading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='whatweofferobjects',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
