from rest_framework import serializers
from accounts.models import Peracik, User

class PeracikSerializer(serializers.ModelSerializer):
    nama = serializers.SerializerMethodField()
    
    def get_nama(self, obj):
        return obj.user.username
    
    class Meta:
        model = Peracik
        fields = ('nama','alamat', 'no_hp', 'sertifikat', 'gambar_pendukung')

class PeracikSignUpSerializer(serializers.Serializer):
    data_peracik = PeracikSerializer(required=True)
    
    email = serializers.EmailField(max_length=100)
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True, max_length=100)
    password_2 = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        peracik_data = validated_data.pop('data_peracik')
        data = User.objects.create_peracik(**validated_data)
        Peracik.objects.create(
            user=data,
            alamat=peracik_data['alamat'],
            no_hp=peracik_data['no_hp'],
            sertifikat=peracik_data['sertifikat'],
            gambar_pendukung=peracik_data['gambar_pendukung']
        ) 
        return data
    
    def validate(self, data):
        
        email = data.get('email')
        password = data.get('password')
        
        if email is None:
            raise serializers.ValidationError({"pesan":"Email tidak boleh kosong"})
        if password is None:
            raise serializers.ValidationError({"pesan":"Password tidak boleh kosong"})
        if password != data['password_2']:
            raise serializers.ValidationError({"pesan":"Password tidak cocok"})
        return data
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_2', 'peracik_data')
        
class PeracikLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True, max_length=100)
    
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email is None:
            raise serializers.ValidationError({"pesan":"Email tidak boleh kosong"})
        if password is None:
            raise serializers.ValidationError({"pesan":"Password tidak boleh kosong"})
        
        return data
    
    class Meta:
        model = User
        fields = ('email', 'password')

class HomePeracikSerializer(serializers.ModelSerializer):
    
    nama = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    
    def get_nama(self, obj):
        return obj.user.username
    
    def get_email(self, obj):
        return obj.user.email
    
    class Meta:
        model = Peracik
        fields = ('nama', 'email')