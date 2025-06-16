from alumnos.models import Alumno


def generar_matricula(alumno: Alumno) -> str:
    abreviatura_carrera = alumno.carrera.abreviatura
    nombre_compuesto = f"{alumno.apellido_paterno[:2]}{alumno.apellido_materno[:1]}{alumno.nombre[:1]}".upper()
    ingreso = alumno.fecha_ingreso.year
    periodo = alumno.periodo_ingreso
    matricula = f"{abreviatura_carrera} {nombre_compuesto} {ingreso}-{periodo}"
    return matricula
