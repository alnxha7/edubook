# Generated by Django 5.0.6 on 2024-06-14 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_page_remove_pagelock_page_name_pagelock_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagelock',
            old_name='user',
            new_name='username',
        ),
    ]
