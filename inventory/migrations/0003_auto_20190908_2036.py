# Generated by Django 2.1.5 on 2019-09-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190907_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(default='imagenes/no-image.png', upload_to='imagenes'),
        ),
    ]