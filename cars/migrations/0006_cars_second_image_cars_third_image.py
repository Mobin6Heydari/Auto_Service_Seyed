# Generated by Django 4.2 on 2023-06-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_remove_cars_second_image_remove_cars_third_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='second_image',
            field=models.ImageField(blank=True, null=True, upload_to='ماشین', verbose_name='عکس دوم'),
        ),
        migrations.AddField(
            model_name='cars',
            name='third_image',
            field=models.ImageField(blank=True, null=True, upload_to='ماشین', verbose_name='عکس سوم'),
        ),
    ]
