IVA = 0.21
def es_par(numero):
    return numero % 2 == 0

def normalizar_nombre(nombre):
    """Quita espacios sobrantes y pone mayúscula inicial en cada palabra."""
    return nombre.strip().title()

def precio_con_iva(precio):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    return round(precio * (1 + IVA), 2)

def aplicar_descuento(precio, porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError("Porcentaje no válido")
    return round(precio * (1 - porcentaje / 100), 2)

def total_carrito(precios):
    if not precios:
        raise ValueError("El carrito está vacío")
    return round(sum(precios), 2)

def password_segura(password):
    """Segura si tiene 8 caracteres o más y al menos un dígito."""
    return len(password) >= 8 and any(c.isdigit() for c in password)

def media(numeros):
    return sum(numeros) / (len(numeros))