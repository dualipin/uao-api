from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import send_mail


@shared_task
def enviar_correo_bienvenida(email):
    """
    Tarea para enviar un correo de bienvenida al usuario.
    """
    # Aquí iría la lógica para enviar el correo
    send_mail(
        "Bienvenido a nuestra plataforma",
        "Gracias por registrarte.",
        "from@example.com",
        [email],
        fail_silently=False,
    )
    return f"Correo enviado a {email}"
