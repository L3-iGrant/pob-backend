from rest_framework import generics
from .models import IGrantUser
from .serializers import IGrantUserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
class UserList(generics.ListAPIView):
    serializer_class = IGrantUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        email = self.request.user.email
        return IGrantUser.objects.filter(email=email)


class UserDetail(generics.RetrieveAPIView):
    queryset = IGrantUser.objects.all()
    serializer_class = IGrantUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['user_type'] = user.user_type

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer