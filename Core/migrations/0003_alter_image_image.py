# Generated by Django 4.1.3 on 2023-03-09 13:45

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_tier_res_1_tier_res_2_tier_res_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/', location='media/'), upload_to=''),
        ),
    ]