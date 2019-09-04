# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-04 05:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrepaidAgreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('compressed_files_url', models.TextField(blank=True, null=True)),
                ('bulk_download_path', models.TextField(blank=True, null=True)),
                ('filename', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='PrepaidProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('issuer_name', models.CharField(blank=True, max_length=255)),
                ('prepaid_type', models.CharField(blank=True, max_length=255, null=True)),
                ('program_manager', models.CharField(blank=True, max_length=255, null=True)),
                ('program_manager_exists', models.CharField(blank=True, max_length=255, null=True)),
                ('other_relevant_parties', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('withdrawal_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='prepaidagreement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prepaid_agreements.PrepaidProduct'),
        ),
    ]
