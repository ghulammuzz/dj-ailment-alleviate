from django.db import models

class Bahan(models.Model):
    nama_bahan = models.CharField(max_length=100)
    keterangan = models.TextField(default='_')
    gambar = models.ImageField(upload_to='bahan/', null=True, blank=True, default='bahan/default.jpeg')
    cara_pakai = models.TextField(default='_')
    class Status(models.TextChoices):
        DITOLAK = 'DITOLAK'
        MENUNGGU = 'MENUNGGU'
        DITERIMA = 'DITERIMA'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DITERIMA)
    def __str__(self):
        return self.nama_bahan

class Category(models.Model):
    name_category = models.CharField(max_length=100)
    keterangan = models.TextField(default='_')
    
    def __str__(self):
        return self.name_category

class Obat(models.Model):
    nama_obat = models.CharField(max_length=100, default='Obat ')
    keterangan = models.TextField(default='_')
    
    gambar = models.ImageField(upload_to='obat/', null=True, blank=True, default='obat/default.jpeg')
    bahan_1 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_1', null=True, blank=True)
    bahan_2 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_2', null=True, blank=True)
    bahan_3 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_3', null=True, blank=True)
    bahan_4 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_4', null=True, blank=True)
    bahan_5 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_5', null=True, blank=True)
    bahan_6 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_6', null=True, blank=True)
    bahan_7 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_7', null=True, blank=True)
    peracik = models.ForeignKey('accounts.Peracik', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Status(models.TextChoices):
        DITOLAK = 'DITOLAK'
        MENUNGGU = 'MENUNGGU'
        DITERIMA = 'DITERIMA'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.MENUNGGU)
    cara_pembuatan = models.TextField(default='_')
    aturan_pemakaian = models.TextField(default='_')
    
    def __str__(self):
        return self.nama_obat
    
class Gejala(models.Model):
    nama_gejala = models.CharField(max_length=100)
    keterangan = models.TextField(default='_')
    gambar = models.ImageField(upload_to='gejala/', null=True, blank=True)
    
    def __str__(self):
        return self.nama_gejala
