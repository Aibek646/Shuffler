# Generated by Django 3.0.5 on 2020-04-10 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200410_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='link_grubhub',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='person',
            name='link_linkedin',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='person',
            name='link_twitter',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='person',
            name='pic',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('ST', 'Staff'), ('CR', 'Crew'), ('PA', 'Passenger'), ('AD', 'Admin')], max_length=2),
        ),
    ]
