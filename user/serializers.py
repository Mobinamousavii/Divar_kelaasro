from rest_framework.serializers import ModelSerializer
from user.models import User
from django.contrib.auth.hashers import make_password

class UserSerializers(ModelSerializer):
    class Meta():
        model = User
        fields = '__all__'
        write_only_fields = ['password']

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["password"] = make_password(validated_data["password"])
        return validated_data
        
        