# Generated by Django 3.0.3 on 2020-02-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ui', '0004_auto_20200223_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='./web_ui/media/uploads', verbose_name='img'),
        ),
    ]