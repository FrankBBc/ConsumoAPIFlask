# Mi Proyecto
# Clasificación de Textos con Flask y Transformers

Esta aplicación utiliza Flask y la librería Transformers para proporcionar un servicio de clasificación de textos basado en el modelo de clasificación cero disparos (zero-shot classification). Los usuarios pueden ingresar un texto y obtener una etiqueta de clasificación entre varias categorías.

## Requisitos

- Python 3.12
- pip (gestor de paquetes de Python)

## Instalación

1. **Clona este repositorio:**

    ```sh
    git clone https://github.com/FrankBBc/ConsumoAPIFlask.git
    cd ConsumoAPIFlask
    ```

2. **Crea y activa un entorno virtual:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    ```

3. **Instala las dependencias:**

    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. **Ejecuta la aplicación Flask:**

    ```sh
    python zeroshot2.py
    ```

2. **Abre tu navegador y ve a:**

    ```
    http://localhost:5010
    ```

3. **Ingresa un texto en el formulario y presiona "Clasificar" para obtener la clasificación.**

## Etiquetas de Clasificación

Las etiquetas disponibles para la clasificación son:

- Danza
- Política
- Deportes
- Religión
- Otros
- Tecnología
- Salud
- Ciencia
- Entretenimiento
- Educación
- Negocios
- Medio ambiente
- Historia
- Cultura
- Viajes
- Finanzas
- Moda
- Gastronomía
- Música
- Literatura

## Notas

- El modelo de clasificación utilizado es `facebook/bart-large-mnli`.
- El clasificador se inicializa una vez al inicio para mejorar el rendimiento.
- Se muestra un mensaje de "Procesando la clasificación..." mientras el texto está siendo clasificado.

![image](https://github.com/FrankBBc/ConsumoAPIFlask/assets/33704862/222b79a2-5cdb-47fb-8451-bf7128c61e95)

