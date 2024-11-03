class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre  # Atributo encapsulado
        self._precio = precio

    def obtener_precio(self):
        return self._precio

    def mostrar_info(self):
        return f"{self._nombre}: ${self._precio}"  # Método para mostrar información


class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla  # Atributo específico de Ropa

    def mostrar_info(self):
        return f"{self._nombre} (Talla: {self._talla}): ${self._precio}"  # Sobrescritura


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return f"Camisa {self._nombre} (Talla: {self._talla}, Tela: {self._tipo_tela}): ${self._precio}"


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio, talla)
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return f"Pantalón {self._nombre} (Talla: {self._talla}, Tela: {self._tipo_tela}): ${self._precio}"


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio, talla)

    def mostrar_info(self):
        return f"Zapato {self._nombre} (Talla: {self._talla}): ${self._precio}"


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        return sum(producto.obtener_precio() for producto in self.productos)

    def mostrar_compra(self):
        print("Productos en el carrito:")
        for producto in self.productos:
            print(producto.mostrar_info())
        print(f"Total a pagar: ${self.calcular_total()}")


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles:")
        for idx, producto in enumerate(self.productos):
            print(f"{idx + 1}. {producto.mostrar_info()}")

    def procesar_compra(self):
        carrito = Carrito()
        while True:
            self.mostrar_productos()
            seleccion = input("Seleccione el producto a agregar al carrito (o 'salir' para terminar): ")
            if seleccion.lower() == 'salir':
                break
            if seleccion.isdecimal() and 1 <= int(seleccion) <= len(self.productos):
                carrito.agregar_producto(self.productos[int(seleccion) - 1])
            else:
                print("Selección inválida. Intente de nuevo.")
        carrito.mostrar_compra()


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda()
    
    # Agregando productos a la tienda
    tienda.agregar_producto(Camisa("Camisa Azul", 20, "M", "Algodón"))
    tienda.agregar_producto(Camisa("Camisa Roja", 25, "L", "Poliéster"))
    tienda.agregar_producto(Pantalon("Pantalón Negro", 30, "32", "Jean"))
    tienda.agregar_producto(Pantalon("Pantalón Verde", 35, "34", "Lino"))
    tienda.agregar_producto(Zapato("Zapato Deportivo", 50, "42"))
    tienda.agregar_producto(Zapato("Zapato Formal", 70, "44"))

    # Procesando la compra
    tienda.procesar_compra()