from django.urls import path

from api.smiles_to_mol import views

urlpatterns = [path("", views.SmilesToMol.as_view())]