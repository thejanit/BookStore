# Generated by Django 3.0.6 on 2021-11-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rev_image',
            field=models.ImageField(null=True, upload_to='images/review'),
        ),
    ]