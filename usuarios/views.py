from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request as Req
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Usuario
from .serializers import PerfilSerializer, UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PerfilView(APIView):
    permission_classes = [IsAuthenticated]

    def handle_exception(self, exc):
        if isinstance(exc, (NotAuthenticated, PermissionDenied)):
            to_email = "martin.msr1304@gmail.com"
            send_mail(
                "Intento de acceso no autorizado",
                "Se ha intentado acceder a un recurso protegido sin autenticación.",
                None,  # Default from email
                [to_email],
                fail_silently=False,
            )

            return Response(
                {"mensaje": "Por favor, inicia sesión antes de continuar."}, status=401
            )
        return super().handle_exception(exc)

    def get(self, request: Req):
        user: Usuario = request.user
        serializer = PerfilSerializer(user)
        #         context = {"usuario": user.username, "mensaje": "Has accedido a tu perfil."}
        #         asunto = "Acceso al perfil"
        #         cuerpo_html = render_to_string("emails/acceso.html", context)
        #         cuerpo_txt = f"""
        # Hola {user.username},

        # Has accedido a tu perfil.

        # Si no fuiste tú, por favor contáctanos inmediatamente.

        # ---
        # Este correo fue enviado automáticamente por UAO App.
        #         """

        #         email = EmailMultiAlternatives(
        #             subject=asunto,
        #             body=cuerpo_txt,
        #             from_email=None,  # Default from email
        #             to=["martin.msr1304@gmail.com"],
        #         )
        #         email.attach_alternative(cuerpo_html, "text/html")
        #         try:
        #             email.send()

        #         except Exception as e:
        #             return Response(
        #                 {"detail": "Error al enviar el correo de notificación."}, status=500
        #             )

        return Response(serializer.data)
