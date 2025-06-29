from rest_framework import serializers
import re


def validar_curp(curp: str):
    """
    Valida el CURP (Clave Única de Registro de Población) mexicano.

    El CURP debe seguir el formato:
    - 18 caracteres alfanuméricos.
    - Comienza con dos letras mayúsculas, seguidas de dos letras del nombre y apellido.
    - Contiene una fecha en formato YYMMDD.
    - Incluye una letra que indica el sexo (H para hombre, M para mujer).
    - Termina con tres letras o números que son un código de homoclave y un dígito verificador.

    Args:
        curp (str): El CURP a validar.

    Returns:
        void: Lanza un error cuando algo es incorrecto.
    """
    regex = r"^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$"
    match = re.match(regex, curp)
    if not match:
        raise ValueError("CURP no tiene un formato válido.")

    curp17 = match[1]
    verifierDigit = int(match[2])

    dictionary = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    sum = 0

    for i in range(17):
        sum += dictionary.index(curp17[i]) * (18 - i)

    calculatedDigit = 10 - (sum % 10)
    if verifierDigit != (calculatedDigit if calculatedDigit != 10 else 0):
        raise ValueError("CURP no tiene un dígito verificador válido.")
