# Generated by Django 3.2.4 on 2021-06-06 21:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro',
            field=tinymce.models.HTMLField(default=True),
        ),
    ]
