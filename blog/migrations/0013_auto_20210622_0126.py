# Generated by Django 3.2.4 on 2021-06-21 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_twitter_bio_handle_profile_twitter_bio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='github_url',
            new_name='github',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='instagram_handle',
            new_name='instagram',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='linkedin_profile_url',
            new_name='linkedin',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='youtube_handle',
            new_name='youtube',
        ),
    ]
