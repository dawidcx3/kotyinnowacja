from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Polowanie', views.HuntingViewSet)
router.register(r'Dane', views.UserViewSet)
router.register(r'Dane kotów', views.CatViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]