# Generated by Django 2.1.5 on 2019-09-23 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0006_auto_20190923_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('sell_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sell_stock', to='inventory.Stock')),
            ],
        ),
    ]