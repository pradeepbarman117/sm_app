# Generated by Django 4.1.2 on 2022-10-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0002_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heading',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
