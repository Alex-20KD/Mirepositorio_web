from dataclasses import dataclass
from typing import Protocol
from datetime import date

# Simulación de interfaces con Protocol
class Legalizable(Protocol):
    def validar(self) -> bool: ...

@dataclass
class DocumentoAdopcion:
    id: int
    nombre_menor: str
    fecha_emision: date

    def validar(self) -> bool:
        return self.fecha_emision <= date.today()

@dataclass
class Antecedente:
    id: int
    descripcion: str
    valido: bool

    def validar(self) -> bool:
        return self.valido

@dataclass
class FirmaDigital:
    id: int
    firmante: str
    hash_firma: str

    def validar(self) -> bool:
        return len(self.hash_firma) == 64  # Suponiendo SHA-256
