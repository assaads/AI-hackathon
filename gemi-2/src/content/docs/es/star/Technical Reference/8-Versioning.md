---
title: Control de versiones: Proyecto Starlight
description: Comprender el control de versiones y las actualizaciones dentro del proyecto Starlight.
---

## Control de versiones

El proyecto Starlight, como muchos proyectos de software, sigue un sistema de control de versiones para realizar un seguimiento de los cambios y las mejoras a lo largo del tiempo. Comprender el control de versiones es crucial para mantenerse actualizado con las últimas funciones y garantizar la compatibilidad.

### Versionamiento semántico

Starlight se adhiere al [versionamiento semántico](https://semver.org/), que utiliza un formato de número de versión de tres partes: `MAYOR.MENOR.PARCHE`.

*   **MAYOR:** Se incrementa para cambios significativos que pueden introducir incompatibilidades con versiones anteriores. 
*   **MENOR:** Se incrementa para nuevas características o funcionalidades que son compatibles con versiones anteriores.
*   **PARCHE:** Se incrementa para correcciones de errores o actualizaciones menores que no afectan la compatibilidad.

### Verificación de la versión actual

Para determinar la versión actual de Starlight que estás utilizando, consulta el archivo `package.json` en el directorio raíz de tu proyecto. El número de versión aparecerá en la sección `dependencies` o `devDependencies`.

### Actualización a una nueva versión

1.  **Consultar las notas de la versión:** Antes de actualizar, revisa las notas de la versión para la nueva versión para comprender los cambios y cualquier posible problema de compatibilidad.
2.  **Actualizar dependencias:** Utiliza npm o yarn para actualizar el paquete `@astrojs/starlight` a la versión deseada:

```bash
npm update @astrojs/starlight
```

o

```bash
yarn upgrade @astrojs/starlight
```

3.  **Abordar los cambios importantes:** Si la nueva versión introduce cambios importantes, modifica tu código en consecuencia para garantizar la compatibilidad.

## Guía de migración

Para las actualizaciones de versiones principales que implican cambios significativos, se proporcionará una guía de migración para ayudar a los usuarios a realizar la transición de sus proyectos a la nueva versión sin problemas. Esta guía describirá los pasos necesarios y destacará cualquier ajuste requerido para mantener la funcionalidad. 


