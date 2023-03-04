# Generated by Django 4.1.7 on 2023-03-04 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_bahan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bahan',
            name='status',
            field=models.CharField(choices=[('DITOLAK', 'Ditolak'), ('MENUNGGU', 'Menunggu'), ('DITERIMA', 'Diterima')], default='DITERIMA', max_length=10),
        ),
    ]