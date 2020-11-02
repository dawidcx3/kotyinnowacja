from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from rest_framework import permissions, generics, mixins, viewsets
from .models import Usr, Hunting, Cat
from .serializers import HuntingSerializer, UserSerializer, CatSerializer
       
class HuntingViewSet(viewsets.ModelViewSet):
    queryset = Hunting.objects.all()
    serializer_class = HuntingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Hunting.objects.filter(cat_owner=self.request.user)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
        
class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)
