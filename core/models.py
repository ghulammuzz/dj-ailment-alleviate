from django.db import models

class Bahan(models.Model):
    nama_bahan = models.CharField(max_length=100)
    keterangan = models.TextField()
    gambar = models.ImageField(upload_to='media/bahan/', null=True, blank=True)
    # takaran = models.CharField(max_length=100, default='_')
    
    def __str__(self):
        return self.nama_bahan
    
class Obat(models.Model):
    nama_obat = models.CharField(max_length=100)
    keterangan = models.TextField()
    gambar = models.ImageField(upload_to='media/obat/', null=True, blank=True)
    bahan_1 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_1', null=True, blank=True)
    bahan_2 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_2', null=True, blank=True)
    bahan_3 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_3', null=True, blank=True)
    bahan_4 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_4', null=True, blank=True)
    bahan_5 = models.ForeignKey(Bahan, on_delete=models.SET_NULL, related_name='bahan_5', null=True, blank=True)
    
    def __str__(self):
        return self.nama_obat
