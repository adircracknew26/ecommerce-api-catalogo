# productService


# 📦 API de Catálogo e Inventario (Product Service) - Equipo 2

Este proyecto es un microservicio desarrollado en Django y Django REST Framework, se usa para administrar los productos disponibles, sus precios y las existencias (stock).
Interacción: Proveedor de datos. El Equipo 3 consumirá esta API para validar precios y disponibilidad antes de crear un pedido.

## 🛠️ Tecnologías Utilizadas
* **Framework:** Django 4.x / Python 3.x
* **API:** Django REST Framework (DRF)
* **Documentación:** Swagger UI (vía `drf-spectacular`)
* **Base de Datos:** SQLite (Configurable a MySQL/PostgreSQL)

## 🚀 Instalación y Configuración Local

Sigue estos pasos para levantar el microservicio en tu máquina local:

 **Clonar el repositorio:**
   cd ecommerce-api-catalogo

**Instalar las dependencias:**

pip install django djangorestframework drf-spectacular python-decouple

**Aplicar las migraciones de la base de datos:**

python manage.py makemigrations
python manage.py migrate

**Levantar el servidor de desarrollo:**

python manage.py runserver

**Documentación de la API (Swagger)**
Este microservicio cuenta con documentación interactiva autogenerada. Una vez que el servidor esté corriendo, puedes ver y probar todos los endpoints accediendo a:

http://127.0.0.1:8000/api/docs/

**ENDPOINTS PRINCIPALES:**
GET	/api/products/	Lista todos los productos disponibles y sus precios.
POST	/api/products/	Crea un nuevo producto en el catálogo (Fase de inicialización).
GET	/api/products/<id>/	Muestra el detalle completo de un producto específico.
POST	/api/products/reduce-stock/	Recibe una lista de productos (producto_id, cantidad) y descuenta el stock de manera transaccional.
