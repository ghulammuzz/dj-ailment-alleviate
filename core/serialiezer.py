from rest_framework import serializers
from .models import Bahan, Obat

def build_url(url):
    return f'http://127.0.0.1:8000{url}'

class BahanSerializer(serializers.ModelSerializer):
    
    gambar = serializers.SerializerMethodField()
    
    def get_gambar(self, obj):
        return build_url(obj.gambar)
    
    class Meta:
        model = Bahan
        fields = ('nama_bahan','gambar', 'keterangan')
        
class ObatSerializer(serializers.ModelSerializer):
    gambar = serializers.SerializerMethodField()
    bahan_1 = BahanSerializer()
    bahan_2 = BahanSerializer()
    bahan_3 = BahanSerializer()
    bahan_4 = BahanSerializer()
    bahan_5 = BahanSerializer()
    
    def get_gambar(self, obj):
        return build_url(obj.gambar)
    
    class Meta:
        model = Obat
        fields = ('id','nama_obat', 'keterangan', 'gambar', 'bahan_1', 'bahan_2', 'bahan_3', 'bahan_4', 'bahan_5')