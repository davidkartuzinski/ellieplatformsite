# Generated by Django 3.2.4 on 2021-06-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_header_image_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='twitter_bio_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]