from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image
from io import BytesIO
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from alumnos.models import Alumno, Documentacion
from datetime import datetime


def generar_reporte_bienvenida(alumno: Alumno):
    documentos = Documentacion.objects.filter(alumno=alumno).first()
    buffer = BytesIO()  # <- GENERAMOS EN MEMORIA

    # Configurar fuentes (asumiendo fuentes estándar)
    try:
        pdfmetrics.registerFont(TTFont("Arial", "arial.ttf"))
        pdfmetrics.registerFont(TTFont("Arial-Bold", "arialbd.ttf"))
        main_font = "Arial"
        bold_font = "Arial-Bold"
    except:
        main_font = "Helvetica"
        bold_font = "Helvetica-Bold"

    # Configuración del documento con márgenes exactos
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=42,
        leftMargin=60,
        topMargin=60,
        bottomMargin=42,
    )

    # Estilos personalizados para coincidir exactamente con el PDF original
    styles = getSampleStyleSheet()

    # Estilo de título principal
    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Heading1"],
        fontName=bold_font,
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=6,
        textColor=black,
        leading=16,
    )

    # Estilo de subtítulo
    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["Heading2"],
        fontName=bold_font,
        fontSize=14,
        alignment=TA_CENTER,
        spaceAfter=14,
        textColor=black,
        leading=14,
    )

    # Estilo de datos del estudiante
    student_data_style = ParagraphStyle(
        "StudentDataStyle",
        parent=styles["Normal"],
        fontName=bold_font,
        fontSize=10,
        spaceAfter=6,
        textColor=black,
        leading=12,
    )

    # Estilo de texto normal
    normal_style = ParagraphStyle(
        "NormalStyle",
        parent=styles["Normal"],
        fontName=main_font,
        fontSize=12,
        spaceAfter=6,
        textColor=black,
        leading=12,
        alignment=TA_LEFT,
    )

    # Estilo de texto normal con espacio después reducido
    normal_compact_style = ParagraphStyle(
        "NormalCompactStyle", parent=normal_style, spaceAfter=2, leading=12
    )
    
    small_style = ParagraphStyle(
        "SmallStyle",
        fontName=main_font,
        fontSize=10,
        spaceAfter=4,
        textColor=black,
        leading=12,
        alignment=TA_LEFT,
    )

    # Estilo para documentos entregados
    docs_style = ParagraphStyle(
        "DocsStyle",
        parent=normal_style,
        spaceBefore=12,
        fontName=bold_font,
        spaceAfter=6,
    )

    # Contenido del documento
    story = []

    try:
        logo_left = Image("assets/logo-alfa-y-omega.jpg")
        logo_left._restrictSize(1.5 * inch, 1 * inch)

        logo_right = Image("assets/logo-tabscoob.jpg")
        logo_right._restrictSize(1.5 * inch, 1 * inch)
    except Exception as e:
        print(f"Error al cargar las imágenes: {e}")
        logo_left = None
        logo_right = None

    col_width = [1.5 * inch, 4 * inch, 1.5 * inch]  # Ancho de cada columna

    universidad = Paragraph("Universidad Alfa y Omega", title_style)
    extension = Paragraph(
        f"Extensión {alumno.extension.nombre if alumno.extension else 'Desconocida'}",
        subtitle_style,
    )

    header_table = Table([[logo_left, universidad, logo_right]], colWidths=col_width)

    header_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                (
                    "ALIGN",
                    (0, 0),
                    (0, 0),
                    "LEFT",
                ),  # Logo izquierdo alineado a la izquierda
                ("ALIGN", (1, 0), (1, 0), "CENTER"),  # Título centrado
                (
                    "ALIGN",
                    (2, 0),
                    (2, 0),
                    "RIGHT",
                ),  # Logo derecho alineado a la derecha
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    story.append(header_table)
    story.append(extension)
    story.append(Spacer(1, 8 * mm))  # Espacio después del subtítulo

    # Datos del estudiante (alineado a la izquierda)
    story.append(Paragraph("<b>Datos del Estudiante:</b>", student_data_style))
    story.append(
        Paragraph(
            f"Nombre: <b>{alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno}</b>",
            normal_style,
        )
    )
    story.append(Paragraph(f"Carrera: <b>{alumno.carrera}</b>", normal_style))
    story.append(Spacer(1, 8 * mm))
    
    def tipo_saludo(genero: str):
        if genero == 'M':
            return "Estimado"
        elif genero == 'F':
            return "Estimada"
        else:
            return "Estimado/a"
        
    def tipo_bienvenida(genero: str):
        if genero == 'M':
            return "Bienvenido"
        elif genero == 'F':
            return "Bienvenida"
        else:
            return "Bienvenido/a"

    # Saludo
    story.append(
        Paragraph(
            f"<b>{tipo_saludo(alumno.genero)} {alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno},</b>",
            normal_style,
        )
    )
    story.append(Spacer(1, 8 * mm))

    # Cuerpo del mensaje (texto exacto del original)
    welcome_lines = [
        f"¡Es un placer darte la bienvenida a la Universidad Alfa y Omega extensión {alumno.extension.nombre}!",
        "Nos llena de alegría recibirte como parte de nuestra comunidad académica y acompañarte en",
        "este emocionante camino hacia tu desarrollo profesional y personal.",
        "",
        "Sabemos que ingresar a la universidad representa un gran paso en tu vida, y queremos que",
        "sepas que aquí encontrarás un entorno de aprendizaje enriquecedor, profesores comprometidos",
        "y una comunidad estudiantil que te apoyará en cada desafío.",
        "",
        "En la Universidad Alfa y Omega, valoramos la excelencia, la curiosidad y el espíritu de",
        "superación. Estamos seguros de que en la carrera de Derecho, desarrollarás",
        "habilidades clave y adquirirás conocimientos que te prepararán para un futuro brillante.",
        "",
        f"¡{tipo_bienvenida(alumno.genero)} a esta gran familia universitaria, {alumno.nombre} {alumno.apellido_paterno}! Te deseamos mucho éxito",
        "en esta nueva etapa.",
    ]

    for line in welcome_lines:
        if line == "":
            story.append(Spacer(1, 4 * mm))  # Espacio entre párrafos
        else:
            story.append(Paragraph(line, normal_compact_style))

    story.append(Spacer(1, 8 * mm))

    # Firma
    story.append(Paragraph("<b>Con entusiasmo y los mejores deseos,</b>", normal_style))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("<b>Universidad Alfa y Omega</b>", normal_style))
    story.append(Spacer(1, 12 * mm))

    # Documentos entregados
    story.append(Paragraph("<b>Documentos entregados:</b>", docs_style))
    story.append(
        Paragraph(
            f"Acta de Nacimiento: {'SI' if documentos.acta_nacimiento else 'NO'} | "
            f"CURP: {'SI' if documentos.curp else 'NO'} | "
            f"Certificado de Bachillerato: {'SI' if documentos.certificado_bachillerato else 'NO'} | "
            f"Certificado Médico: {'SI' if documentos.certificado_medico else 'NO'}",
            small_style,
        )
    )
    story.append(
        Paragraph(f"Generado el {datetime.now().strftime('%d/%m/%Y')}", small_style)
    )

    # Generar el PDF
    doc.build(story)
    buffer.seek(0)
    return buffer 
