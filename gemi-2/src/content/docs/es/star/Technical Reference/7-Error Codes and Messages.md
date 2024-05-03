---
title: Códigos y mensajes de error: Integración de la API de OpenAI
description: Solución de problemas de errores comunes que se encuentran al usar la API de OpenAI dentro del proyecto Starlight.
---

## Errores de la API de OpenAI

Al interactuar con la API de OpenAI, es posible que encuentres varios códigos y mensajes de error. Aquí hay algunos comunes y orientación sobre cómo abordarlos:

*   **401 No autorizado:**
    *   **Significado:** Este error indica que tu clave API no es válida o falta.
    *   **Solución:**
        *   Verifica que tienes una clave API válida de OpenAI.
        *   Asegúrate de haber configurado correctamente la variable de entorno `OPENAI_API_KEY`.
        *   Comprueba que estás utilizando el endpoint de API y el método de solicitud correctos.

*   **429 Demasiadas solicitudes:**
    *   **Significado:** Has excedido el límite de velocidad para las solicitudes de API.
    *   **Solución:**
        *   Reduce la frecuencia de tus llamadas a la API.
        *   Considera actualizar tu plan de OpenAI para obtener límites de velocidad más altos.

*   **400 Solicitud incorrecta:**
    *   **Significado:** La solicitud que enviaste a la API está mal formada o contiene parámetros no válidos.
    *   **Solución:**
        *   Revisa cuidadosamente la documentación de la API y asegúrate de que los parámetros de tu solicitud sean correctos.
        *   Comprueba si hay errores tipográficos o campos obligatorios que faltan.

*   **500 Error interno del servidor:**
    *   **Significado:** Se ha producido un error en el lado del servidor de OpenAI. 
    *   **Solución:**
        *   Vuelve a intentar tu solicitud más tarde.
        *   Si el problema persiste, ponte en contacto con el soporte de OpenAI. 

## Consejos generales para la solución de problemas

*   **Consultar la documentación de la API:** Consulta la [documentación oficial de la API de OpenAI](https://beta.openai.com/docs/api-reference) para obtener información detallada sobre los códigos de error, los parámetros y los formatos de respuesta. 
*   **Registrar las respuestas de la API:** Registra la respuesta completa de la API para obtener información sobre los detalles específicos del error.
*   **Validar la entrada:** Asegúrate de que la indicación o consulta de entrada que estás enviando a la API sea válida y no contenga ningún error o carácter no admitido.
*   **Probar la clave API:** Utiliza OpenAI Playground para probar tu clave API y verificar que funciona correctamente. 


