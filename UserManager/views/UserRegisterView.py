from rest_framework import generics
from rest_framework import permissions
from UserManager.models.PlanckUser import PlanckUser
from UserManager.serializers.UserSerializer import UserSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = PlanckUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
