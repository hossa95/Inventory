# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('phone', models.IntegerField()),
                ('max_discount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('credit_limit', models.IntegerField()),
                ('grace_period', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('max_discount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.TextField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity_sold', models.DecimalField(decimal_places=3, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoice_number', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('invoice_due_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('discount', models.IntegerField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Partial', 'Partial')], max_length=100)),
                ('type', models.CharField(choices=[('Cash', 'Cash'), ('Credit', 'Credit')], max_length=100)),
                ('remaining', models.DecimalField(decimal_places=2, max_digits=9)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Agent')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Invoices')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Agent')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity_in_stock', models.IntegerField()),
                ('quantity_on_hold', models.IntegerField()),
                ('expire_date', models.DateTimeField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('vendor', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Category')),
            ],
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Payments'),
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Invoices'),
        ),
        migrations.AddField(
            model_name='invoicedetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Products'),
        ),
    ]
