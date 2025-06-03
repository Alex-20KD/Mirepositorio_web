from entidades import DocumentoAdopcion, Antecedente, FirmaDigital
from servicios import verificar_entidad, procesar_documento
from utils import crear_documento_adopcion
import asyncio
from datetime import date

# Variables y tipos
nombre = "Carlos Pérez"
fecha = date(2023, 10, 5)
hash_valido = "a"*64

# Arreglo de objetos
documentos = [
    DocumentoAdopcion(id=1, nombre_menor=nombre, fecha_emision=fecha),
    Antecedente(id=2, descripcion="Sin antecedentes", valido=True),
    FirmaDigital(id=3, firmante="Carlos Pérez", hash_firma=hash_valido),
]

# Callback
for doc in documentos:
    verificar_entidad(doc, lambda valido: print(f"{type(doc).__name__} validado: {valido}"))

# Async/Await y Promesas
async def main():
    resultados = await asyncio.gather(*(procesar_documento(doc) for doc in documentos))
    for res in resultados:
        print(res)

asyncio.run(main())

# Spread
nuevo_doc = crear_documento_adopcion(
    id=10,
    nombre_menor="Lucía Gómez",
    fecha_emision=date(2022, 5, 20)
)
print(f"Documento creado con Spread: {nuevo_doc}")



