# Generated by Django 4.1.3 on 2023-01-16 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_postblog_rename_userprofile_user_review_postnews_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]