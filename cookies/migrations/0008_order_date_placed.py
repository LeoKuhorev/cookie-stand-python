# Generated by Django 3.1.2 on 2020-10-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0007_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True, default='2020-10-01'),
            preserve_default=False,
        ),
    ]
