# Generated by Django 3.1.2 on 2021-04-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
        ),
    ]
