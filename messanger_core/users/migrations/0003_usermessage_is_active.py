# Generated by Django 5.1.3 on 2024-11-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermessage_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
