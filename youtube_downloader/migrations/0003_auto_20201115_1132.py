# Generated by Django 2.2 on 2020-11-15 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_downloader', '0002_auto_20201115_1001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guide',
            old_name='stet_count',
            new_name='step_count',
        ),
        migrations.RenameField(
            model_name='guide',
            old_name='stet_description',
            new_name='step_description',
        ),
    ]