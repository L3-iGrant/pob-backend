from django.contrib import admin
from django.urls import path, include
from .views import UserList, UserDetail, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
        path('/', UserList.as_view()),
        path('/<int:pk>/', UserDetail.as_view()),
        path('/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
