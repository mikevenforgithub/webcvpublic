# Generated by Django 3.1.2 on 2021-05-06 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0005_auto_20210506_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycv',
            name='mycv',
            field=models.FileField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]