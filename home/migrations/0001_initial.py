# Generated by Django 4.2 on 2023-06-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='لوگو')),
            ],
            options={
                'verbose_name_plural': 'لوگو',
            },
        ),
    ]