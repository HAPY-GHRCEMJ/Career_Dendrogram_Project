# Generated by Django 5.0.8 on 2024-09-17 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
