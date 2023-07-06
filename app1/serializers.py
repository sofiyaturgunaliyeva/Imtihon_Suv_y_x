from rest_framework import serializers
from .models import *

class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'



# 5.	BuyurtmaSerializer uchun quyidagicha validation yozing:
# Agar buyurtmadagi mijozning qarzi 500000 dan ko’p bo’lsa,
# “Qarzingiz juda ko’p, buyurtma qilolmaysiz!” ma’nosida ValidationError bersin. (10 ball)

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'

    def validate(self, qarz):
        mijoz_qarzi = qarz['mijoz'].qarz
        if mijoz_qarzi > 500000:
            raise serializers.ValidationError("Qarzingiz juda ko'p, buyurtma qilolmaysiz!")
        return qarz

