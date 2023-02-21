# Generated by Django 4.1.7 on 2023-02-21 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_bahan', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='media/bahan/')),
            ],
        ),
        migrations.CreateModel(
            name='Penyakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_penyakit', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='media/penyakit/')),
                ('bahan_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_1', to='core.bahan')),
                ('bahan_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_2', to='core.bahan')),
                ('bahan_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_3', to='core.bahan')),
                ('bahan_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_4', to='core.bahan')),
                ('bahan_5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bahan_5', to='core.bahan')),
            ],
        ),
    ]