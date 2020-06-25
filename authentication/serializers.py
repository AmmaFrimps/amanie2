from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'other_name',
                  'last_name',
                  'email',
                  'can_access_dashboard',
                  'phone_number',
                  'work_id',
                  'rank',
                  'location',
                  'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}, 'email': {'required': True},
                        'username': {'required': True}, }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
