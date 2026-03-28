import re

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z]", "", text) # solo letras
    return text

def generate_username(nombre: str, apellido_paterno: str, apellido_materno: str) -> str:
    n = normalize(nombre)
    ap = normalize(apellido_paterno)
    am = normalize(apellido_materno)

    base = n[0] + ap + (am[0] if am else "")

    # Completar a minimo 8 caracteres
    if len(base) < 8:
        remaining = 8 - len(base)
        base += am[1:1 + remaining]

    return base[:20] # Limite razonable
