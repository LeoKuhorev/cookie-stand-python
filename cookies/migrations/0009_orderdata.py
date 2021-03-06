# Generated by Django 3.1.2 on 2020-10-22 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0008_order_date_placed'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('number_of_customers', models.IntegerField(help_text='Enter number of customers for the day')),
                ('avg_sale', models.DecimalField(decimal_places=2, help_text='Enter the average number of cookies per sale for the day', max_digits=5)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cookies.location')),
            ],
        ),
    ]
