from rest_framework import viewsets
from rest_framework import views, viewsets
from rest_framework.response import Response
from django.http import FileResponse
from .models import Alumno
from .serializers import AlumnoSerializer
from django.core.mail import send_mail
from utils.reporte_bienvenida import generar_reporte_bienvenida


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

    def perform_create(self, serializer: AlumnoSerializer):
        alumno = serializer.save()
        # Aquí puedes realizar acciones adicionales después de crear el alumno
        # Por ejemplo, generar un reporte de bienvenida
        # from utils.reporte_bienvenida import generar_reporte_bienvenida
        # reporte = generar_reporte_bienvenida(alumno)
        # if reporte:
        #     # Guardar el reporte en un archivo o enviarlo por correo
        # Generar el reporte de bienvenida
        # reporte = generar_reporte_bienvenida(alumno)

        # if reporte:
        #     # Enviar el reporte por correo
        #     send_mail(
        #     subject="Bienvenido a UAO",
        #     message="Adjunto encontrarás tu reporte de bienvenida.",
        #     from_email="no-reply@uao.edu",
        #     recipient_list=[alumno.email],
        #     fail_silently=False,
        #     )
        #     pass
        # Si necesitas hacer algo con el reporte, puedes hacerlo aquí
        return alumno

    def perform_update(self, serializer: AlumnoSerializer):
        alumno = serializer.save()

        reporte = generar_reporte_bienvenida(alumno)

        # Aquí puedes realizar acciones adicionales después de actualizar el alumno
        return alumno


class CartaBienvenidaView(views.APIView):
    def get(self, request, pk):
        try:
            alumno = Alumno.objects.get(pk=pk)
            reporte = generar_reporte_bienvenida(alumno)
            return FileResponse(
                reporte,
                as_attachment=True,
                filename=f"reporte_bienvenida_{alumno.curp}.pdf",
            )
        except Alumno.DoesNotExist:
            return Response({"detail": "Alumno no encontrado."}, status=404)
