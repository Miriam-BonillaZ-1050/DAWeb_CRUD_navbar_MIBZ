from django.shortcuts import render, redirect
from .models import Pago

def inicio_vistaPago(request):
    los_pagos = Pago.objects.all()  # Cambiado de Cliente a Pago
    return render(request, 'gestionarPagos.html', {'mis_pagos': los_pagos})

def registrarPago(request):
    id_pago = request.POST["num_id_pago"]
    fecha_venta = request.POST["date_fecha_venta"]
    monto_total = request.POST["txt_monto_total"]
    tipo = request.POST["txt_tipo_pago"]
    descripcion_compra = request.POST["txt_descripcion_compra"]
    id_producto = request.POST["txt_id_producto"]
    id_cliente = request.POST["txt_id_cliente"]
    id_empleado = request.POST["txt_id_empleado"]

    guardar_pago = Pago.objects.create(
        id_pago=id_pago, 
        fecha_venta=fecha_venta, 
        monto_total=monto_total,
        tipo=tipo, 
        descripcion_compra=descripcion_compra,
        id_producto=id_producto,
        id_cliente=id_cliente,
        id_empleado=id_empleado
    )
    return redirect('pago')

def seleccionarPago(request, id_pago):
    pago = Pago.objects.get(id_pago=id_pago)
    return render(request, "editarPago.html", {"mis_pagos": pago})

def editarPago(request):
    id_pago = request.POST["num_id_pago"]
    fecha_venta = request.POST["date_fecha_venta"]
    monto_total = request.POST["txt_monto_total"]
    tipo = request.POST["txt_tipo_pago"]
    descripcion_compra = request.POST["txt_descripcion_compra"]
    id_producto = request.POST["txt_id_producto"]
    id_cliente = request.POST["txt_id_cliente"]
    id_empleado = request.POST["txt_id_empleado"]
    
    pago = Pago.objects.get(id_pago=id_pago)
    pago.fecha_venta = fecha_venta
    pago.monto_total = monto_total
    pago.tipo = tipo
    pago.descripcion_compra = descripcion_compra
    pago.id_producto = id_producto
    pago.id_cliente = id_cliente
    pago.id_empleado = id_empleado
    pago.save()
    
    return redirect('pago')

def borrarPago(request, id_pago):
    pago = Pago.objects.get(id_pago=id_pago)
    pago.delete()
    return redirect("pago")
