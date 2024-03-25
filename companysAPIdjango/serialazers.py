from rest_framework import serializers
from pages.models import Company
from pages.models import Address



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Company
        fields = ('id', 'name_company', 'name_person', 'surname', 'patronymic', 'phone', 'email', 'web_link', 'address', 'address_id')

