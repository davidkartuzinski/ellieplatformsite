# Generated by Django 3.2.4 on 2021-06-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profile_twitter_bio_handle'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author_website',
            field=models.CharField(blank=True, default='https://ellieplatform.org', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_bio_handle',
            field=models.CharField(blank=True, default='@open_apprentice', max_length=255),
        ),
    ]
