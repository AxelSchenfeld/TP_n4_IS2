# Implemente una clase que permita a un número cualquiera imprimir su valor, luego agregarle sucesivamente.
# a. Sumarle 2.
# b. Multiplicarle por 2.
# c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a las clases con las diferentes 
# operaciones. Use un patrón decorator para implementar.
class Componente():
    def realizar_operacion(self) -> float:
        pass

class Numero(Componente):
    def __init__(self, valor: float) -> None:
        self.valor = valor

    def realizar_operacion(self) -> float:
        return self.valor

class Decorador(Componente):
    _componente: Componente = None

    def __init__(self, componente: Componente) -> None:
        self._componente = componente

    @property
    def obtener_componente(self) -> Componente:
        return self._componente

    def realizar_operacion(self) -> float:
        return self._componente.realizar_operacion()

class SumarDos(Decorador):
    def realizar_operacion(self) -> float:
        return self.obtener_componente.realizar_operacion() + 2

class MultiplicarPorDos(Decorador):
    def realizar_operacion(self) -> float:
        return self.obtener_componente.realizar_operacion() * 2

class DividirPorTres(Decorador):
    def realizar_operacion(self) -> float:
        return self.obtener_componente.realizar_operacion() / 3

def cliente_codigo(componente: Componente) -> None:
    print(f"RESULTADO: {componente.realizar_operacion()}", end="")

if __name__ == "__main__":
    valor = float(input("Introduce un número: "))
    simple = Numero(valor)
    print("Cliente: Tengo un componente simple:")
    cliente_codigo(simple)
    print("\n")

    operacion = input("--a: sumar 2, b: multiplicar por 2, c: dividir por 3--: ")
    if operacion == 'a':
        decorador = SumarDos(simple)
    elif operacion == 'b':
        decorador = MultiplicarPorDos(simple)
    elif operacion == 'c':
        decorador = DividirPorTres(simple)
    else:
        print("Operación no válida.")
        exit(1)

    print("Cliente: Ahora tengo un componente decorado:")
    cliente_codigo(decorador)

    print("\n")