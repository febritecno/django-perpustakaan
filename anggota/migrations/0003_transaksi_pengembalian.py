# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-14 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0002_auto_20160813_0930'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaksi_pengembalian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_buku', models.CharField(max_length=100)),
                ('tgl_buku_dikembalikan', models.DateField()),
                ('denda_hari', models.IntegerField(null=True)),
                ('nama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anggota.transaksi_peminjaman')),
            ],
        ),
    ]
