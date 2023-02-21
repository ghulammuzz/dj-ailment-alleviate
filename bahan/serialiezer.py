from rest_framework import serializers
from .models import Bahan, Penyakit

class BahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bahan
        fields = ('nama_bahan','gambar')
        
class PenyakitSerializer(serializers.ModelSerializer):
    bahan_1 = BahanSerializer()
    bahan_2 = BahanSerializer()
    bahan_3 = BahanSerializer()
    bahan_4 = BahanSerializer()
    bahan_5 = BahanSerializer()
    
    class Meta:
        model = Penyakit
        fields = ('nama_penyakit', 'keterangan', 'gambar', 'bahan_1', 'bahan_2', 'bahan_3', 'bahan_4', 'bahan_5')