import asyncio

# Callback function
def verificar_entidad(entidad, callback):
    resultado = entidad.validar()
    callback(resultado)

# Promesa/async simulada
async def procesar_documento(entidad):
    await asyncio.sleep(1)
    if entidad.validar():
        return f"{type(entidad).__name__} válido."
    else:
        return f"{type(entidad).__name__} inválido."
