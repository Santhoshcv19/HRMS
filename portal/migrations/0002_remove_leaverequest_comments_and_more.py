# Generated by Django 5.0.1 on 2024-04-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='comments',
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='manager_comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
