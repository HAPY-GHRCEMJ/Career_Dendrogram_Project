# Generated by Django 5.0.8 on 2024-09-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0005_alter_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
