# Generated by Django 5.0.6 on 2024-06-22 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='payment',
            name='is_successful',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='orders.order'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('CC', 'Credit Card'), ('COD', 'Cash on Delivery')], max_length=3),
        ),
    ]