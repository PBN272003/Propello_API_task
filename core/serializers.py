from .models import User, Firm
from rest_framework import serializers

class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = '__all__'
        read_only_fields = ['user']
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    firms = FirmSerializer(many=True, read_only=True)  # nested firms

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'firms']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        