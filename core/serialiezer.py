from rest_framework import serializers
from .models import *
from accounts.serializer import PeracikSerializer

local = 'http://127.0.0.1:8000'
deployment = 'https://deployailment.pythonanywhere.com'

def build_url(url):
    return f'{deployment}/media/{url}'

class BahanSerializer(serializers.ModelSerializer):
    
    gambar = serializers.SerializerMethodField()
    
    def get_gambar(self, obj):
        return build_url(obj.gambar)
    
    class Meta:
        model = Bahan
        fields = ('id','nama_bahan','gambar', 'keterangan')
        
class ObatSerializer(serializers.ModelSerializer):
    gambar = serializers.SerializerMethodField()
    bahan = serializers.SerializerMethodField()
    peracik = serializers.SerializerMethodField()
    peracik = PeracikSerializer()
      
    # def get_peracik(self, obj):
    #     return obj.peracik.user.username
        
    def get_bahan(self, obj):
        bahan = []
        
        bahan_1 = BahanSerializer(obj.bahan_1).data
        bahan_2 = BahanSerializer(obj.bahan_2).data
        bahan_3 = BahanSerializer(obj.bahan_3).data
        bahan_4 = BahanSerializer(obj.bahan_4).data
        bahan_5 = BahanSerializer(obj.bahan_5).data
        bahan_6 = BahanSerializer(obj.bahan_6).data
        bahan_7 = BahanSerializer(obj.bahan_7).data
        
        for i in [bahan_1, bahan_2, bahan_3, bahan_4, bahan_5, bahan_6, bahan_7]:
            if i['nama_bahan'] and i['gambar'] and i['keterangan'] == None:
                pass
            elif i['nama_bahan'] and i['gambar'] and i['keterangan'] != None:
                bahan.append(i)

        return bahan
            
        
    def get_gambar(self, obj):
        return build_url(obj.gambar)
    
    class Meta:
        model = Obat
        fields = (
            'id',
            'nama_obat',
            'peracik',
            'keterangan',
            'gambar',
            'cara_pembuatan',
            'aturan_pemakaian',
            'bahan'
            )
        
class CategorySerializer(serializers.ModelSerializer):
    
    bahan = serializers.SerializerMethodField()
    
    def get_bahan(self, obj):
        bahan = BahanSerializer(obj.bahan, many=True).data
        return bahan
    
    class Meta:
        model = Category
        fields  = ["name_category", "keterangan", "bahan"]