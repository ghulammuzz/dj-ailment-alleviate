from rest_framework import serializers
from accounts.models import Peracik, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')

class PeracikSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    def get_name(self, obj):
        return obj.user.username
    
    class Meta:
        model = Peracik
        fields = ('name','address', 'phone_number','type', 'certificate', 'supporting_image')

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
            address=peracik_data['address'],
            type=peracik_data['type'],
            phone_number=peracik_data['phone_number'],
            certificate=peracik_data['certificate'],
            supporting_image=peracik_data['supporting_image']
        ) 
        return data
    
    def validate(self, data):
        
        email = data.get('email')
        password = data.get('password')
        # exisisting email
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"pesan":"Email sudah terdaftar"})
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
