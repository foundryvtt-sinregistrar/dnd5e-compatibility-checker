# Guía de documentación de módulos D&D5e

Esta guía mantiene una presentación coherente entre los módulos y traducciones de este conjunto. Se aplica a los README de usuario y a los changelog; no sustituye la documentación técnica específica de cada proyecto.

## README bilingüe

- `README.md` es la versión en español y `README.en.md` la versión en inglés.
- Ambas versiones comienzan con el título del módulo y un selector de idioma:

  ```md
  **Español** | [English](README.en.md)
  ```

  ```md
  [Español](README.md) | **English**
  ```

- Las dos versiones deben comunicar el mismo comportamiento, requisitos y limitaciones. Pueden diferir únicamente en ejemplos o terminología traducida.

## Orden de las secciones

Usa estas secciones, en este orden, cuando sean aplicables:

1. Estado / Status.
2. Requisitos / Requirements.
3. Instalación / Installation.
4. Activación y uso / Activation and use.
5. Actualización / Updating.
6. Contenido incluido / Included content.
7. Limitaciones / Limitations.
8. Soporte y contribuciones / Support and contributions.
9. Desarrollo / Development.
10. Licencia y créditos / License and credits.

Las guías, capturas, tablas, API y notas técnicas se mantienen en subsecciones de la sección que corresponda; no se elimina información funcional solo para ajustarse a la plantilla.

## Compatibilidad e instalación

- La compatibilidad documentada debe coincidir con `module.json` (`minimum` y `verified`).
- Utiliza el manifiesto de la última release, no la rama `main`:

  ```text
  https://github.com/foundryvtt-sinregistrar/<module-id>/releases/latest/download/module.json
  ```

- Las insignias de release deben ser dinámicas. No uses badges enlazadas a una etiqueta fija salvo que se documenten explícitamente como una versión histórica.

## Changelog

- El archivo comienza con `# Changelog` y `## [Unreleased]`.
- Cada versión se escribe como `## [X.Y.Z] - AAAA-MM-DD`.
- Conserva las fechas y el historial publicados.
- Agrupa cambios nuevos bajo `### Added`, `### Changed`, `### Fixed`, `### Removed` o `### Security` cuando facilite la lectura.

## Terminología

- Usa `Foundry VTT`, `dnd5e` para el identificador del sistema y `D&D5e` para el nombre del sistema en prosa.
- Usa el nombre oficial de módulos y compendios tal como aparece en Foundry.
- Evita mezclar inglés y español dentro de una misma frase, salvo nombres propios, identificadores, rutas o API.
