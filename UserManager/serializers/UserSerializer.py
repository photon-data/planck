from rest_framework import serializers
from UserManager.models.PlanckUser import PlanckUser

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = PlanckUser
        fields = ['username', 'email', 'password', 'password2']

    def create(self, validated_data):
        user = PlanckUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data