# Generated by Django 4.2.7 on 2023-11-10 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='post'),
            preserve_default=False,
        ),
    ]