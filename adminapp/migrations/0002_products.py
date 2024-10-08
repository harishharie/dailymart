# Generated by Django 5.1 on 2024-08-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(default='null.jpg', upload_to='image')),
                ('price', models.IntegerField()),
                ('category', models.TextField()),
                ('features', models.TextField()),
            ],
        ),
    ]
