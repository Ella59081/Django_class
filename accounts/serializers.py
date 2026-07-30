from rest_framework import serializers
from rest_framework_simplejwt import TokenObtainPairSerializer
from .models import User
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']
        
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fieids.pop('username')
        self.fields['email'] = serializers.EmailField(write_only=True)
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        try:
            user = User.object.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed (
                'No active accounts found for this email'
            )
        
        return super().validate({'username': user.username, 'password': user.password})
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'bio']
            