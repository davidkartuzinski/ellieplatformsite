# Generated by Django 3.2.4 on 2021-06-11 18:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=ckeditor.fields.RichTextField(max_length=160),
        ),
    ]