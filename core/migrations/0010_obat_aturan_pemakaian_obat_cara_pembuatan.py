# Generated by Django 4.1.7 on 2023-02-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_gejala_delete_penyakit'),
    ]

    operations = [
        migrations.AddField(
            model_name='obat',
            name='aturan_pemakaian',
            field=models.TextField(default='_'),
        ),
        migrations.AddField(
            model_name='obat',
            name='cara_pembuatan',
            field=models.TextField(default='_'),
        ),
    ]
