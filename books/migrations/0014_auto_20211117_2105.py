# Generated by Django 3.0.6 on 2021-11-17 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_review_rev_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rev_image',
            new_name='image',
        ),
    ]
