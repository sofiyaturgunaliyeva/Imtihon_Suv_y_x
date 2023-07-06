from django.contrib import admin
from django.urls import path,include
from app1.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("suvlar",SuvModelViewSet)
router.register("mijozlar",MijozModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('buyurtmalar/', BuyurtmaAPIView.as_view()),
    path('haydovchilar/', HaydovchilarAPIView.as_view()),
    path('bitta_haydovchi/<int:pk>/', HaydovchiAPIView.as_view()),
    path('bitta_admin/<int:pk>/', AdminAPIView.as_view()),
    path('adminlar/', AdminlarAPIView.as_view()),
]
