# Tienda de Ropa - POO en Python

## Descripción

Este proyecto es un sistema de compra de ropa desarrollado en Python utilizando la Programación Orientada a Objetos (POO). Permite al usuario seleccionar diferentes ítems de ropa, agregar productos a un carrito y procesar la compra.

## Estructura del Proyecto

El proyecto está estructurado en varias clases que representan los productos, categorías y la tienda. Las principales clases implementadas son:

### Clases

- **Producto**
  - Clase base que representa un producto genérico.
  - **Atributos**:
    - `_nombre`: Nombre del producto.
    - `_precio`: Precio del producto.
  - **Métodos**:
    - `obtener_precio()`: Retorna el precio del producto.
    - `mostrar_info()`: Muestra información básica del producto.

- **Ropa**
  - Clase que hereda de `Producto` y añade características específicas de la ropa.
  - **Atributos**:
    - `_talla`: Talla del producto.
  - **Métodos**:
    - `mostrar_info()`: Sobrescribe el método de `Producto` para incluir la talla.

- **Camisa**
  - Clase que hereda de `Ropa`, específica para camisas.
  - **Atributos**:
    - `_tipo_tela`: Tipo de tela de la camisa.
  - **Métodos**:
    - `mostrar_info()`: Sobrescribe el método de `Ropa` para mostrar información específica de la camisa.

- **Pantalon**
  - Clase que hereda de `Ropa`, específica para pantalones.
  - **Atributos**:
    - `_tipo_tela`: Tipo de tela del pantalón.
  - **Métodos**:
    - `mostrar_info()`: Sobrescribe el método de `Ropa` para mostrar información específica del pantalón.

- **Zapato**
  - Clase que hereda de `Ropa`, específica para zapatos.
  - **Atributos**: No tiene atributos adicionales.
  - **Métodos**:
    - `mostrar_info()`: Sobrescribe el método de `Ropa` para mostrar información específica del zapato.

- **Carrito**
  - Clase que maneja los productos seleccionados por el usuario.
  - **Atributos**:
    - `productos`: Lista de productos en el carrito.
  - **Métodos**:
    - `agregar_producto(producto)`: Agrega un producto al carrito.
    - `calcular_total()`: Calcula el total de la compra.
    - `mostrar_compra()`: Muestra los productos en el carrito y el total a pagar.

- **Tienda**
  - Clase que gestiona la interacción con el usuario y los productos disponibles.
  - **Atributos**:
    - `productos`: Lista de productos disponibles en la tienda.
  - **Métodos**:
    - `agregar_producto(producto)`: Agrega un producto a la tienda.
    - `mostrar_productos()`: Muestra los productos disponibles.
    - `procesar_compra()`: Permite al usuario seleccionar productos y gestionar la compra.

