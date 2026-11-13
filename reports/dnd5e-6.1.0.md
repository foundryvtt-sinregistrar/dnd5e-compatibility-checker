# Informe DND5e — release-6.1.0

Fecha UTC: 2026-11-13T19:40:21.441239+00:00
Foundry objetivo: 14.370
Comparación: release-6.0.6 → release-6.1.0

Auditoría estática: PASS no acredita compatibilidad funcional. ERROR indica fallo de datos/rango; REVISAR requiere comprobación humana.

| Repositorio | Estado | Tipo | Commit |
|---|---|---|---|
| foundryvtt-sinregistrar/.github | NO APLICA | desconocido | a2225c1e744d |
| foundryvtt-sinregistrar/dnd5e-2024-cleric-domains | REVISAR | JavaScript/compendios | 991dc7a4d6f6 |
| foundryvtt-sinregistrar/dnd5e-2024-wizard-schools | REVISAR | JavaScript/compendios | 9b777d3f5b8c |
| foundryvtt-sinregistrar/dnd5e-death-token-effects | REVISAR | JavaScript/compendios | 40bd8e0f987b |
| foundryvtt-sinregistrar/dnd5e-spell-advancement | REVISAR | JavaScript/compendios | 405661f95555 |
| foundryvtt-sinregistrar/foundryvtt-sinregistrar | NO APLICA | desconocido | 1e32436c23b3 |
| foundryvtt-sinregistrar/patrol-intelligence | ERROR DE AUDITORÍA | desconocido |  |
| foundryvtt-sinregistrar/translate-dnd5e-cleric-domains-2024-es | REVISAR | Babele + JavaScript | 8b1dfaa232a1 |
| foundryvtt-sinregistrar/translate-dnd5e-dm-2024-es | REVISAR | Babele + JavaScript | d2c7d12041ea |
| foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es | REVISAR | Babele + JavaScript | bacaaefddfdc |
| foundryvtt-sinregistrar/translate-dnd5e-phandelver-below-es | REVISAR | Babele + JavaScript | aa0816160d36 |
| foundryvtt-sinregistrar/translate-dnd5e-phb-2024-es | REVISAR | Babele + JavaScript | bb86cce0f90c |
| foundryvtt-sinregistrar/translate-dnd5e-sdr2-es | REVISAR | Babele + JavaScript | 73c8ff878591 |
| foundryvtt-sinregistrar/translate-dnd5e-tashas-cauldron | REVISAR | Babele + JavaScript | f6983bf880da |
| foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es | REVISAR | Babele + JavaScript | c48e02017736 |
| foundryvtt-sinregistrar/translate-dnd5e-wizard-schools-2024-es | REVISAR | Babele + JavaScript | ce1dff698217 |

## foundryvtt-sinregistrar/.github
- **NO_MANIFEST**: Sin module.json en raíz
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-2024-cleric-domains
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **PACK_RUNTIME**: Rutas comprobadas; bases LevelDB y migraciones requieren importación en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-2024-wizard-schools
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **PACK_RUNTIME**: Rutas comprobadas; bases LevelDB y migraciones requieren importación en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-death-token-effects
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-spell-advancement
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/foundryvtt-sinregistrar
- **NO_MANIFEST**: Sin module.json en raíz
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/patrol-intelligence
- **AUDIT_FAILED**: Command '['git', '-c', 'advice.detachedHead=false', 'clone', '--quiet', '--depth=1', '--branch', 'main', 'https://github.com/foundryvtt-sinregistrar/patrol-intelligence.git', '/tmp/tmpan06x10i/patrol-intelligence']' returned non-zero exit status 128.
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-cleric-domains-2024-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd5e-2024-cleric-domains, dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-dm-2024-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **UPSTREAM_PATH**: dev-tools/translation/validate-target-labels.mjs: ruta no encontrada systems/dnd5e/lang/en.js
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-dungeon-masters-guide
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-monster-manual
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-phandelver-below-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-phandelver-below
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-phb-2024-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-sdr2-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-tashas-cauldron
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-tashas-cauldron
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-tomb-annihilation
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-wizard-schools-2024-es
- **UNVERIFIED**: DND5e 6.1.0: verificación declarada 6.0.6
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd5e-2024-wizard-schools, dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## Límites
No se ejecuta código de terceros. No se cargan Foundry, Babele ni contenido comercial. No se demuestra cobertura de traducciones sin compendios fuente. Los repositorios se auditan en HEAD de su rama por defecto; no necesariamente coinciden con el ZIP publicado.
