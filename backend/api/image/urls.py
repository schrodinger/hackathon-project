from django.urls import path

from api.image import views

urlpatterns = [path("", views.GenerateImage.as_view())]
