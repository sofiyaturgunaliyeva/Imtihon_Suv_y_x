from django.db import models
from django.contrib.auth.models import User

class Suv(models.Model):
    brend = models.CharField(max_length=100)
    narx = models.IntegerField()
    litr = models.CharField(max_length=100)
    batafsil = models.TextField()

    def __str__(self):
        return self.brend

class Mijoz(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    manzil = models.TextField()
    qarz = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.PositiveSmallIntegerField()
    ish_vaqti = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    kiritilgan_sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ism

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    miqdor = models.CharField(max_length=100)
    umumiy_narx = models.IntegerField()
    qabul_qilgan_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    yetkazib_berish_haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.suv.brend

