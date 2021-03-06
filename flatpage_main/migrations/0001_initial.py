# Generated by Django 3.2.4 on 2021-06-22 11:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewFlatpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='content field')),
                ('flatpage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flatpages.flatpage')),
            ],
            options={
                'verbose_name': 'Static Page',
                'verbose_name_plural': 'Static Pages',
            },
        ),
    ]
