# Generated by Django 4.2.15 on 2024-11-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordsearch',
            name='found_words',
            field=models.TextField(default=''),
        ),
    ]
