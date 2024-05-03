from django.shortcuts import render
from rest_framework import viewsets, routers
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserApi (viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_queryset(self):
    queryset = User.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset
  
router = routers.DefaultRouter()
router.register(r'api', UserApi)
