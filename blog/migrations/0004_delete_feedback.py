# Generated by Django 4.2.2 on 2023-06-21 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
