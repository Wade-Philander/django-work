# Generated by Django 3.2.4 on 2021-07-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_auto_20210706_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-04-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
