# Map My World API

- Esta API proporciona funcionalidades para gestionar ubicaciones, categorías y recomendaciones.

## Instalación
1. Clona este repositorio.
2. Ejecuta `python3 -m pip install virtualenv`
3. Luego `python3 -m virtualenv env`
4. Y ahora `source env/bin/activate`
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `uvicorn app.main:app --reload`.

# Modelos
## Modelo de Ubicación

### Descripción:
Representa una ubicación geográfica con coordenadas de latitud y longitud.

### Atributos:
- `id` (Integer): Identificador único de la ubicación. Clave primaria.
- `latitude` (Float): La latitud de la ubicación.
- `longitude` (Float): La longitud de la ubicación.

### Ejemplo:
```json
{
    "id": 1,
    "latitude": 40.7128,
    "longitude": -74.0060
}
```

## Modelo de Categoría

### Descripción:
Representa una categoría para ubicaciones, como "restaurante", "hotel", etc.

### Atributos:
- `id` (Integer): Identificador único de la categoría. Clave primaria.
- `name` (String): El nombre de la categoría.

### Ejemplo:
```json
{
    "id": 1,
    "name": "Restaurante"
}
```

## Modelo de de Revisión de Ubicación por Categoría

### Descripción:
Representa la asociación entre ubicaciones y categorías, indicando cuándo se revisó por última vez una ubicación para una categoría específica.

### Atributos:
- `id` (Integer): Identificador único de la revisión de ubicación por categoría. Clave primaria.
- `location_id` (Integer): Clave foránea que hace referencia al campo id en la tabla locations.
- `category_id` (Integer): Clave foránea que hace referencia al campo id en la tabla categories.
- `last_reviewed` (Timestamp): Marca de tiempo que indica cuándo se revisó por última vez la ubicación para la categoría.

### Ejemplo:
```json
{
    "id": 1,
    "location_id": 1,
    "category_id": 1,
    "last_reviewed": "2024-03-15T10:30:00"
}
```

## Uso
### Endpoints
- Crea una nueva ubicación.
    - POST /api/locations/
    ```json
    {
        "longitude":12312675324431.23,
        "latitude":8342763123124324.435345
    }
    ```
    Response:

    ```json
    {
        "id": 1,
        "longitude": 12312675324431.23,
        "latitude": 8342763123124324.435345
    }
    ```
    
- Crea una nueva categoria.
    - POST /api/categories/
    ```json
    {
        "name": "restaurant"
    }
    ```
    Response:

    ```json
    {
        "id": 1,
        "name": "restaurant"
    }
    ```
    
- Crea una nueva recomendación.
    - POST /api/recommendations/
    ```json
    {
        "location_id": 1,
        "category_id": 1,
        "last_reviewed": "2024-03-01T12:00:00"
    }
    ```
    Response:

    ```json
    {
        "location_id": 1,
        "category_id": 1,
        "last_reviewed": "2024-03-01T12:00:00"
    }
    ```
    - GET /api/recommendations/
    Response:

    ```json
   [
        {
            "location_id": 1,
            "category_id": 1,
            "last_reviewed": "2024-03-01T12:00:00"
        },
        {
            "location_id": 2,
            "category_id": 3,
            "last_reviewed": "2024-03-15T10:30:00"
        }
    ]
    ```
