from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Componente(ABC):
    @abstractmethod
    def operacion(self) -> str:
        pass

class Parte(Componente):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def operacion(self) -> str:
        return self.nombre

class Subconjunto(Componente):
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._componentes: List[Componente] = []

    def agregar(self, componente: Componente) -> None:
        self._componentes.append(componente)

    def operacion(self) -> str:
        resultados = []
        for componente in self._componentes:
            resultados.append(componente.operacion())
        return f"{self.nombre}({', '.join(resultados)})"

if __name__ == "__main__":
    producto_principal = Subconjunto("Producto Principal")

    for i in range(1, 4):
        subconjunto = Subconjunto(f"Subconjunto{i}")
        for j in range(1, 5):
            parte = Parte(f"Parte{i}.{j}")
            subconjunto.agregar(parte)
        producto_principal.agregar(subconjunto)

    print(producto_principal.operacion())

    subconjunto_opcional = Subconjunto("Subconjunto Opcional")
    for i in range(1, 5):
        parte = Parte(f"ParteO.{i}")
        subconjunto_opcional.agregar(parte)
    producto_principal.agregar(subconjunto_opcional)

    print(producto_principal.operacion())