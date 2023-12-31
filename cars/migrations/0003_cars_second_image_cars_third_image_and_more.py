# Generated by Django 4.2 on 2023-06-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_delete_carsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='second_image',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.fields.CharField>---عکس دوم', verbose_name='عکس دوم'),
        ),
        migrations.AddField(
            model_name='cars',
            name='third_image',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.fields.CharField>---عکس سوم', verbose_name='عکس سوم'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='<django.db.models.fields.CharField>---عکس اصلی', verbose_name='عکس ماشین'),
        ),
    ]
