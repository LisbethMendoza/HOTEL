from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ReservaServicio, ServicioExtra, Reserva
from django.shortcuts import render
import json

@csrf_exempt
def crear_reserva_servicio(request):
    if request.method == "POST":
        nombre_cliente = request.POST.get("nombre_cliente")
        servicios_seleccionados = request.POST.getlist("servicios_seleccionados")

        # Agregar impresión de depuración
        print(f"Nombre Cliente: {nombre_cliente}")
        print(f"Servicios Seleccionados: {servicios_seleccionados}")

        if not nombre_cliente:
            return JsonResponse({"error": "El nombre del cliente es requerido"}, status=400)

        if not servicios_seleccionados:
            return JsonResponse({"error": "Debe seleccionar al menos un servicio"}, status=400)

        reserva = Reserva.objects.filter(nombre_cliente__icontains=nombre_cliente).first()

        if not reserva:
            return JsonResponse({"error": "Reserva no encontrada para el cliente."}, status=404)

        servicios = ServicioExtra.objects.filter(id__in=servicios_seleccionados)

        if not servicios.exists():
            return JsonResponse({"error": "Servicios no encontrados"}, status=404)

        for servicio in servicios:
            ReservaServicio.objects.create(
                reserva=reserva,
                servicio_extra=servicio
            )

        return render(request, 'servicio.html', {'servicios': ServicioExtra.objects.all(), 'servicios_seleccionados': servicios})


    return JsonResponse({"error": "Método no permitido"}, status=405)


@csrf_exempt
def actualizar_total_pago(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nombre_cliente = data.get("nombre_cliente")
        servicios_seleccionados = data.get("servicios_seleccionados")

        if not nombre_cliente:
            return JsonResponse({"error": "El nombre del cliente es requerido"}, status=400)

        if not servicios_seleccionados:
            return JsonResponse({"error": "Debe seleccionar al menos un servicio"}, status=400)

        reserva = Reserva.objects.filter(nombre_cliente__icontains=nombre_cliente).first()

        if not reserva:
            return JsonResponse({"error": "Reserva no encontrada para el cliente."}, status=404)

        servicios = ServicioExtra.objects.filter(id__in=servicios_seleccionados)

        if not servicios.exists():
            return JsonResponse({"error": "Servicios no encontrados"}, status=404)

        total_servicios = sum(servicio.precio for servicio in servicios)

        reserva.total_pago += total_servicios
        reserva.save()

        return render(request, 'servicio.html', {'servicios': ServicioExtra.objects.all(), 'servicios_seleccionados': servicios})

    return JsonResponse({"error": "Método no permitido"}, status=405)
