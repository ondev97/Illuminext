# Generated by Django 3.0 on 2021-04-28 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhatWeOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WhatWeOfferObjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Client_section',
            new_name='ClientSection',
        ),
        migrations.RenameModel(
            old_name='Specialization_item',
            new_name='SpecializationItem',
        ),
    ]
