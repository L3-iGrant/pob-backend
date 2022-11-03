from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tender/', include('pob.tender.urls')),
]