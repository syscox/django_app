from django.contrib.auth.models import User, Group
from rest_framework import serializers
from profiles.models import Address, Media, User as UserP


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# class ProfileUserSerializer(serializers.HyperlinkedModelSerializer):
#     address = serializers.PrimaryKeyRelatedField(many=False, read_only=True)  # devuelve el ID
#     address = serializers.StringRelatedField(many=False)  # devuelve el __str__
#
#     class Meta:
#         model = UserP
#         fields = ('first_name', 'last_name', 'gender', 'email', 'phone', 'active', 'fecha_alta', 'address')


class ProfileAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('id',)
        # fields = '__all__'

        # fields = ('address', 'city', 'state', 'country', 'zip_code')


class ProfileMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('name', 'url', 'user_id')


class ProfileUserSerializer(serializers.ModelSerializer):
    address = ProfileAddressSerializer()
    # media = ProfileMediaSerializer(many=True, read_only=True)

    class Meta:
        model = UserP
        fields = ('first_name', 'last_name', 'gender', 'email', 'phone', 'active', 'fecha_alta', 'address', 'media_set')
