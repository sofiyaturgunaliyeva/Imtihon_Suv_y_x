from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.views import APIView

from .models import *
from .serializers import *
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet


# 4 4.	Har bir jadval uchun API’lar yozib chiqing. Suv va Mijoz modellarida hamma
# requestlar uchun, Buyurtmada get va post uchun, Admin,
# Haydovchilarda faqat get(hammasini, masalan ‘/haydovchilar/’,
# birortasini ‘/haydovchi/3/’ kabi) requestlar uchun API’lar bo’lsin.



# 6.	Mijozlarni get qilishda ism va tel bo’yicha qidirish
# , qarzi bo’yicha tartiblash imkoniyatlarini qo’shing.
# Suvlarni get qilishda esa brendi bo’yicha qidirish,
# narxi bo’yicha tartiblash imkoniyatlari bo’lsin.

class SuvModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['brend']
    ordering_fields = ['narx']  # tartiblab chiqaradi


class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['ism','tel']
    ordering_fields = ['qarz']  # tartiblab chiqaradi

class BuyurtmaAPIView(APIView):
    def get(self, request):
        buyurtmalar = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(buyurtmalar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminlarAPIView(APIView):
    def get(self, request):
        adminlar = Admin.objects.all()
        serializer = AdminSerializer(adminlar, many=True)
        return Response(serializer.data)

class AdminAPIView(APIView):
    def get(self, request,pk):
        admin = Admin.objects.get(id=pk)
        serializer = AdminSerializer(admin)
        return Response(serializer.data)




class HaydovchilarAPIView(APIView):
    def get(self, request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar, many=True)
        return Response(serializer.data)

class HaydovchiAPIView(APIView):
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi)
        return Response(serializer.data)

