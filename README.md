# dnd5e-compatibility-checker

Auditor centralizado de los módulos de `foundryvtt-sinregistrar` para DND5e y Foundry VTT. Contacto: foundryvtt@sinregistrar.es.

## Activación

1. Subir estos archivos a la rama `main` del repositorio existente `foundryvtt-sinregistrar/dnd5e-compatibility-checker`.
2. Habilitar Actions e Issues en el repositorio. El workflow requiere permisos `contents: write` e `issues: write`; una regla de protección que prohíba pushes del bot impedirá guardar el histórico.
3. Actions → Compatibilidad DND5e → Run workflow. Marcar `force` para repetir la release actual. La entrega incluye un informe inicial y su estado: usar force en la primera ejecución para publicar su Issue.
4. Con la cuenta **foundryvtt-sinregistrar**, activar Watch → Custom → Issues y configurar el correo de notificaciones de GitHub como **foundryvtt@sinregistrar.es**. La dirección en settings.json es informativa: no envía correos ni cambia tu cuenta.

El workflow consulta la última release estable oficial cada seis horas UTC. No recibe eventos del repositorio upstream. GitHub puede retrasar ejecuciones programadas y deshabilitar programaciones en repositorios públicos inactivos; comprobar periódicamente Actions. Las notificaciones de fallos de Actions dependen de tus ajustes personales. No requiere SMTP, API de IA ni gasto de tokens de Codex; se aplican las cuotas de Actions.

## Alcance y estados

| Estado | Significado |
|---|---|
| PASS ESTÁTICO | Pasan las comprobaciones implementadas; no certifica funcionamiento |
| REVISAR | Versiones sin verificar, referencias dudosas o pruebas funcionales pendientes |
| ERROR | JSON, sintaxis, rutas declaradas o rango de versión con errores |
| ERROR DE AUDITORÍA | No se pudo completar el análisis; la release se vuelve a intentar |
| NO APLICA | Sin module.json en la raíz |

Se descubren repositorios públicos no archivados del usuario mediante API paginada. Se excluyen el fork `dnd5e` y este checker. Se registra el commit exacto de cada rama por defecto. No se ejecuta código descargado. Se comprueban todos los JSON (incluidas claves duplicadas), sintaxis JS/MJS con Node, rutas de scripts/estilos/idiomas/packs, rangos Foundry/DND5e y verificación declarada. Se detectan rutas literales `systems/dnd5e/...` ausentes en el tag oficial y claves DND5E usadas en JavaScript que hayan desaparecido respecto a la anterior release auditada. Las referencias dinámicas no están cubiertas.

**No promete detectar todas las roturas de API, hooks, datos o templates.** Las bases LevelDB no se abren, no se validan migraciones ni comportamiento de efectos. Los módulos Babele siempre requieren revisión: validar JSON no comprueba IDs, nombres, mappings ni documentos sin traducir. Para esa fase hacen falta los compendios originales, especialmente los comerciales, y una instalación autorizada de Foundry. No se descargan productos comerciales ni se actualiza `verified`.

## Módulos encontrados el 04/10/2026

- dnd5e-2024-cleric-domains
- dnd5e-2024-wizard-schools
- dnd5e-death-token-effects
- translate-dnd5e-cleric-domains-2024-es
- translate-dnd5e-dm-2024-es
- translate-dnd5e-mm-2024-es
- translate-dnd5e-phandelver-below-es
- translate-dnd5e-phb-2024-es
- translate-dnd5e-sdr2-es
- translate-dnd5e-tashas-cauldron
- translate-dnd5e-tomb-annihilation-es
- translate-dnd5e-wizard-schools-2024-es

## Ejecución local

Python 3.12+, Git y Node 22. Sin dependencias Python adicionales.

```bash
python -m unittest discover -s tests -v
python scripts/check.py --force
```

`GH_TOKEN` es opcional para lectura pública; evita límites bajos de API sin autenticación. El token de Actions solo se utiliza contra la API de GitHub; las clonaciones son públicas y no reciben credenciales. Repositorios privados no están cubiertos.

Cambiar `foundry_version` en `config/settings.json` cuando cambie tu instalación y ejecutar con force. Actualmente se comprueba **14.368**, tomada de los manifiestos, no se supone que sea la versión instalada en tu equipo.

## Informes y recuperación

`reports/dnd5e-VERSION.md` contiene resumen y tareas de revisión; el JSON conserva hallazgos y commits para procesamiento. `reports/state.json` identifica la última release auditada completamente. La primera ejecución no compara claves contra una versión previa. Cada release tiene un Issue consolidado identificable mediante un marcador; force actualiza ese Issue incluso si está cerrado. Los informes de una misma versión se reemplazan con force; Git conserva sus versiones anteriores. Los artifacts duran 90 días.

Los errores de auditoría producen salida 2 y no avanzan el estado; los errores detectados en módulos sí generan informe y avanzan el estado. El Issue se publica antes de guardar el estado en Git; si la publicación falla, la siguiente ejecución reintenta. Si falla el guardado, corregir permisos y repetir. Las actualizaciones de módulos sin nueva release DND5e requieren ejecución force.

Para una comprobación funcional: preparar mundo de prueba y copia de seguridad, instalar versiones exactas de dependencias, activar módulo/Babele, importar compendios y probar fichas, avances, efectos y traducciones. Registrar esa evidencia antes de modificar versiones verified.
