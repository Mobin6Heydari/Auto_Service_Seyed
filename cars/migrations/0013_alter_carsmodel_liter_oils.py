# Generated by Django 4.2 on 2023-06-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_remove_carsmodel_img_one_carsmodel_main_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsmodel',
            name='liter_oils',
            field=models.IntegerField(blank=True, null=True, verbose_name='ظرفیت روغن'),
        ),
    ]
