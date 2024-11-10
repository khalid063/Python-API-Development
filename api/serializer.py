from rest_framework import serializers # type: ignore
from rest_framework.response import Response # type: ignore
from.models import CustomUser, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


## Registration of New User with Password "Serializer"
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'phone_number', 'name']
        extra_kwargs = {
            'password': {'write_only': True}  # Password should not be returned
        }

    def validate_username(self, value):
        # This check will only validate if the username is being changed
        if self.instance and self.instance.username != value and CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],  # This will be hashed by create_user
            phone_number=validated_data.get('phone_number'),
            name=validated_data.get('name')
        )
        return user