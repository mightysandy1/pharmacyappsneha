# Generated by Django 4.1.2 on 2025-02-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo_site', '0003_remove_billdetails_med_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='pack_quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
