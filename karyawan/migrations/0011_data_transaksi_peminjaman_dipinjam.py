# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0010_auto_20160910_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_transaksi_peminjaman',
            name='dipinjam',
            field=models.BooleanField(default=False),
        ),
    ]
