# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0012_remove_transaksi_peminjaman_jenis_buku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi_peminjaman',
            name='nama_peminjam',
            field=models.CharField(max_length=100),
        ),
    ]
