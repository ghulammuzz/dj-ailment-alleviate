# Generated by Django 4.1.7 on 2023-03-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_bahan_gambar_alter_obat_gambar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100)),
                ('keterangan', models.TextField(default='_')),
            ],
        ),
    ]
