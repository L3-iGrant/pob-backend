from django.urls import path

from . import views

urlpatterns = [
    path('<int:tender_id>/', views.publish_tender),
]