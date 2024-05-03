---
title: Variables de entorno
description: Una guía para utilizar variables de entorno dentro del proyecto Starlight.
---

## Variables de entorno

Las variables de entorno ofrecen una forma de configurar tu proyecto Starlight con valores externos sin codificarlos directamente en tu código. Esto es particularmente útil para gestionar información sensible como claves API o credenciales de bases de datos.

### OPENAI\_API\_KEY

*   **Propósito:** Almacena la clave API para acceder a la API de OpenAI.
*   **Requerido:** Sí, si tienes la intención de utilizar la integración de OpenAI para la generación de texto.
*   **Cómo configurar:**
    1.  Crea un archivo `.env` en el directorio raíz de tu proyecto. 
    2.  Agrega la siguiente línea al archivo `.env`, reemplazando `your-api-key` con tu clave API real de OpenAI:

```
OPENAI_API_KEY=your-api-key
```

*   **Valor predeterminado:** Ninguno

### Otras variables de entorno

El proyecto Starlight se puede personalizar aún más utilizando variables de entorno adicionales según tus requisitos e integraciones específicas.

## Configuración de variables de entorno

*   **Archivo .env:** Crea un archivo `.env` en el directorio raíz de tu proyecto para almacenar variables de entorno. Cada línea del archivo debe seguir el formato `NOMBRE_DE_VARIABLE=valor`.
*   **Terminal:** Establece variables de entorno directamente en tu sesión de terminal utilizando el comando export:

```bash
export OPENAI_API_KEY=your-api-key
```

*   **Plataformas de alojamiento:** Muchas plataformas de alojamiento proporcionan mecanismos para establecer variables de entorno a través de sus paneles de control o archivos de configuración.

## Consideraciones importantes

*   **Seguridad:** Evita confirmar tu archivo `.env` en el control de versiones, especialmente si contiene información sensible.
*   **Alcance de la variable:** Las variables de entorno establecidas en el terminal solo están disponibles dentro de esa sesión específica.
*   **Mejores prácticas:** Sigue las prácticas de codificación segura y evita exponer claves API o secretos en el código del lado del cliente. 





