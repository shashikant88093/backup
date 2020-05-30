# Generated by Django 3.0.5 on 2020-05-02 03:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20200502_0252'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'movie')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'movie')},
        ),
    ]
