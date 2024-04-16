from __future__ import annotations
from abc import ABC, abstractmethod

class ImplementacionLaminador(ABC):
    @abstractmethod
    def producir_lamina(self) -> str:
        pass


class LaminadorCincoMetros(ImplementacionLaminador):
    def producir_lamina(self) -> str:
        return "Produciendo una lámina de acero con un ancho de 1.5 metros y 0.5” de espesor usando el laminador de 5 metros."


class LaminadorDiezMetros(ImplementacionLaminador):
    def producir_lamina(self) -> str:
        return "Produciendo una lámina de acero con un ancho de 1.5 metros y 0.5” de espesor usando el laminador de 10 metros."


class Lamina:
    def __init__(self, implementacion: ImplementacionLaminador) -> None:
        self._implementacion = implementacion

    def producir(self) -> str:
        return self._implementacion.producir_lamina()


class LaminaExtendida(Lamina):
    def producir(self) -> str:
        return f"{super().producir()} \nOperación extendida."


def codigo_cliente(lamina: Lamina) -> None:
    print(lamina.producir())


if __name__ == "__main__":
    print("Produciendo láminas usando el laminador de 5 metros:")
    implementacion = LaminadorCincoMetros()
    lamina = Lamina(implementacion)
    codigo_cliente(lamina)

    print("\nProduciendo láminas usando el laminador de 10 metros:")
    implementacion = LaminadorDiezMetros()
    lamina = LaminaExtendida(implementacion)
    codigo_cliente(lamina)