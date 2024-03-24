from django.shortcuts import render
from companysAPIdjango.serialazers import CompanySerializer
from pages.models import Company
from pages.models import Address
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

class CompanyListView(APIView):
    serializer_class = CompanySerializer

    def get(self, request, format=None):
        companies = Company.objects.all().prefetch_related('address')
        serializer = CompanySerializer(companies, many=True)
        return Response({'company': serializer.data})
    

# class CompanyDetailView(APIView):
#     serializer_class = CompanySerializer
#     lookup_field = 'id'
#     def get_object(self):
#        pk = self.kwargs['pk']
#        return Company.objects.get(id=pk)
#     def get(self, request, pk, format=None):
#         company = self.get_object()
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)
    
class CompanyCreateAPIView(generics.GenericAPIView):
    serializer_class = CompanySerializer
    
    def post(self, request):
        data = request.data
        name_company = data['name_company']
        name_person = data['name_person']
        surname = data['surname']
        patronymic = data['patronymic']
        phone = data['phone']
        email = data['email']
        web_link = data['web_link']

        city = data['address.city']
        street = data['address.street']
        house_number = data['address.house_number']
        building_number = data['address.building_number']
        postal_code = data['address.postal_code']

        address, created = Address.objects.get_or_create(postal_code=postal_code, city=city, street=street, house_number=house_number, building_number=building_number)
        company = Company(name_company=name_company, name_person=name_person, surname=surname, patronymic=patronymic, phone=phone, email=email, web_link=web_link, address_id=address.id)

        company.save()

        return Response(data)
    
class CompanyUpdateAPIView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def update(self, request, *args, **kwargs):
        company = self.get_object()
        data = request.data
        name_company = data['name_company']
        name_person = data['name_person']
        surname = data['surname']
        patronymic = data['patronymic']
        phone = data['phone']
        email = data['email']
        web_link = data['web_link']
        company.name_company = name_company
        company.name_person = name_person
        company.surname = surname
        company.patronymic = patronymic
        company.phone = phone
        company.email = email
        company.web_link = web_link

        city = data['address.city']
        street = data['address.street']
        house_number = data['address.house_number']
        building_number = data['address.building_number']
        postal_code = data['address.postal_code']

        # Получаем адрес, связанный с компанией
        address = company.address
        address.city = city
        address.street = street
        address.house_number = house_number
        address.building_number = building_number
        address.postal_code = postal_code

        company.save()
        address.save()

        return Response({"name_company": company.name_company, 
                        "name_person": company.name_person, 
                        "surname": company.surname,
                        "patronymic": company.patronymic,
                        "phone": company.phone,
                        "email": company.email,
                        "web_link": company.web_link,
                        "address.city": city,
                        "address.street": street,
                        "address.house_number": house_number,
                        "address.building_number": building_number,
                        "address.postal_code": postal_code})
    

class CompanyDeleteAPIView(generics.DestroyAPIView):
    queryset = Company.objects.all()
    lookup_field = 'id'
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response("Объект успешно удален")