from django.urls import path
from . import views

urlpatterns = [
    path("pago", views.inicio_vistaPago, name="pago"),
    path("registrarPago/", views.registrarPago, name="registrarPago"),
    path("seleccionarPago/<id_pago>", views.seleccionarPago, name="seleccionarPago"),
    path("editarPago/", views.editarPago, name="editarPago"),
    path("borrarPago/<id_pago>", views.borrarPago, name="borrarPago"),
]
