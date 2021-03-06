# Generated by Django 3.2.4 on 2021-06-20 22:27

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=60, unique=True)),
                ('beg_page_content', ckeditor_uploader.fields.RichTextUploadingField(default='This is the beginning or top part of your content.')),
                ('variation_id', models.AutoField(primary_key=True, serialize=False)),
                ('variation_page_content', ckeditor_uploader.fields.RichTextUploadingField(default='This is the variation content. Make a version here and another in a different page.')),
                ('end_page_content', ckeditor_uploader.fields.RichTextUploadingField(default='This is the end or bottom part of your content.')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('meta_description', models.TextField(default='meta description', max_length=160)),
            ],
        ),
    ]
