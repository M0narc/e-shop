# Generated by Django 5.1.2 on 2024-12-18 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=200)),
                ('shipping_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.order')),
            ],
            options={
                'verbose_name': 'Shipping Address',
                'verbose_name_plural': 'Shipping Addresses',
                'ordering': ['-created_at'],
            },
        ),
    ]
