from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class UserLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)


        if serializer.is_valid():
            user = serializer.user
            return Response({
                'refresh': serializer.validated_data['refresh'],
                'access': serializer.validated_data['access'],
                'username': user.username,
                'email': user.email,
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
