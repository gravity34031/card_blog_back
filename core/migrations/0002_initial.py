# Generated by Django 4.1.3 on 2023-03-04 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photologue', '0019_remove_photo_img_path'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postnews',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postblog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postblog',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL, verbose_name='Избранное'),
        ),
        migrations.AddField(
            model_name='postblog',
            name='images',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='photologue.gallery', verbose_name='Галерея'),
        ),
        migrations.AddField(
            model_name='postblog',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='core.RuTaggedItem', to='taggit.Tag', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='post_blog',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_blog', to='core.postblog'),
        ),
        migrations.AddField(
            model_name='comments',
            name='post_news',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_news', to='core.postnews'),
        ),
    ]