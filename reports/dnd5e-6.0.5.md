# Informe DND5e — release-6.0.5

Fecha UTC: 2026-10-04T14:00:47.361799+00:00
Foundry objetivo: 14.368
Comparación: release-6.0.5 → release-6.0.5

Auditoría estática: PASS no acredita compatibilidad funcional. ERROR indica fallo de datos/rango; REVISAR requiere comprobación humana.

| Repositorio | Estado | Tipo | Commit |
|---|---|---|---|
| foundryvtt-sinregistrar/dnd5e-2024-cleric-domains | REVISAR | JavaScript/compendios | a0146b0455b0 |
| foundryvtt-sinregistrar/dnd5e-2024-wizard-schools | REVISAR | JavaScript/compendios | 21678c2ee52b |
| foundryvtt-sinregistrar/dnd5e-death-token-effects | REVISAR | JavaScript/compendios | 84682c6aaedb |
| foundryvtt-sinregistrar/translate-dnd5e-cleric-domains-2024-es | REVISAR | Babele + JavaScript | 4d807f7d4dbb |
| foundryvtt-sinregistrar/translate-dnd5e-dm-2024-es | REVISAR | Babele + JavaScript | 4c8dd73094a4 |
| foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es | REVISAR | Babele + JavaScript | f47fdc2c2e50 |
| foundryvtt-sinregistrar/translate-dnd5e-phandelver-below-es | REVISAR | Babele + JavaScript | 9a8e09fa348d |
| foundryvtt-sinregistrar/translate-dnd5e-phb-2024-es | REVISAR | Babele + JavaScript | e4e77965a7e9 |
| foundryvtt-sinregistrar/translate-dnd5e-sdr2-es | REVISAR | Babele + JavaScript | a3803ae8dcfe |
| foundryvtt-sinregistrar/translate-dnd5e-tashas-cauldron | REVISAR | Babele + JavaScript | a6f4c56ded81 |
| foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es | REVISAR | Babele + JavaScript | 9912a946be6e |
| foundryvtt-sinregistrar/translate-dnd5e-wizard-schools-2024-es | REVISAR | Babele + JavaScript | af6bf1cd65a0 |

## foundryvtt-sinregistrar/dnd5e-2024-cleric-domains
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **PACK_RUNTIME**: Rutas comprobadas; bases LevelDB y migraciones requieren importación en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-2024-wizard-schools
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **PACK_RUNTIME**: Rutas comprobadas; bases LevelDB y migraciones requieren importación en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-death-token-effects
- **UNVERIFIED**: Foundry 14.368: verificación declarada 14.363
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada ausente
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-cleric-domains-2024-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd5e-2024-cleric-domains, dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-dm-2024-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **UPSTREAM_PATH**: dev-tools/translation/validate-target-labels.mjs: ruta no encontrada systems/dnd5e/lang/en.js
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-dungeon-masters-guide
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-monster-manual
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-phandelver-below-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-phandelver-below
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-phb-2024-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-sdr2-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-tashas-cauldron
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-tashas-cauldron
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-tomb-annihilation
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-wizard-schools-2024-es
- **UNVERIFIED**: DND5e 6.0.5: verificación declarada 6.0.3
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd5e-2024-wizard-schools, dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## Límites
No se ejecuta código de terceros. No se cargan Foundry, Babele ni contenido comercial. No se demuestra cobertura de traducciones sin compendios fuente. Los repositorios se auditan en HEAD de su rama por defecto; no necesariamente coinciden con el ZIP publicado.
