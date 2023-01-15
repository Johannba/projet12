from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "role",
        ]

    def create(self, validated_data):
        return User.objects.create_user(
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            role=validated_data["role"],
        )
