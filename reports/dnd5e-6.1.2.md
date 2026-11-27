# Informe DND5e — release-6.1.2

Fecha UTC: 2026-11-27T21:15:40.895448+00:00
Foundry objetivo: 14.370
Comparación: release-6.0.6 → release-6.1.2

Auditoría estática: PASS no acredita compatibilidad funcional. ERROR indica fallo de datos/rango; REVISAR requiere comprobación humana.

| Repositorio | Estado | Tipo | Commit |
|---|---|---|---|
| foundryvtt-sinregistrar/.github | NO APLICA | desconocido | a2225c1e744d |
| foundryvtt-sinregistrar/dnd5e-2024-cleric-domains | REVISAR | JavaScript/compendios | ff7c653b4beb |
| foundryvtt-sinregistrar/dnd5e-2024-wizard-schools | REVISAR | JavaScript/compendios | d37abe382d9a |
| foundryvtt-sinregistrar/dnd5e-death-token-effects | REVISAR | JavaScript/compendios | baca8ccbaf7d |
| foundryvtt-sinregistrar/dnd5e-durability-crafting | REVISAR | JavaScript/compendios | c672034b0767 |
| foundryvtt-sinregistrar/dnd5e-spell-advancement | REVISAR | JavaScript/compendios | 55dded5ad24a |
| foundryvtt-sinregistrar/foundryvtt-sinregistrar | NO APLICA | desconocido | 1e32436c23b3 |
| foundryvtt-sinregistrar/patrol-intelligence | REVISAR | JavaScript/compendios | 2017c07f2cf8 |
| foundryvtt-sinregistrar/translate-dnd5e-cleric-domains-2024-es | REVISAR | Babele + JavaScript | 93352c1f0d5b |
| foundryvtt-sinregistrar/translate-dnd5e-dm-2024-es | REVISAR | Babele + JavaScript | c7f35b2bf2c7 |
| foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es | REVISAR | Babele + JavaScript | df5f8c073697 |
| foundryvtt-sinregistrar/translate-dnd5e-phandelver-below-es | REVISAR | Babele + JavaScript | 2e52cc77657d |
| foundryvtt-sinregistrar/translate-dnd5e-phb-2024-es | REVISAR | Babele + JavaScript | dd472074637f |
| foundryvtt-sinregistrar/translate-dnd5e-sdr2-es | REVISAR | Babele + JavaScript | a5ddc9142fa9 |
| foundryvtt-sinregistrar/translate-dnd5e-tashas-cauldron | REVISAR | Babele + JavaScript | 11c9625a7ce8 |
| foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es | REVISAR | Babele + JavaScript | cc970ac45bc1 |
| foundryvtt-sinregistrar/translate-dnd5e-wizard-schools-2024-es | REVISAR | Babele + JavaScript | c5ed46527df2 |

## foundryvtt-sinregistrar/.github
- **NO_MANIFEST**: Sin module.json en raíz
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-2024-cleric-domains
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **PACK_RUNTIME**: Rutas comprobadas; bases LevelDB y migraciones requieren importación en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-2024-wizard-schools
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **PACK_RUNTIME**: Rutas comprobadas; bases LevelDB y migraciones requieren importación en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-death-token-effects
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-durability-crafting
- **README_LANGUAGE_LINK**: README.md no enlaza a README.en.md
- **README_MANIFEST**: README.md no incluye el manifiesto de la última release
- **README_EN_MISSING**: Falta README.en.md; consulta DOCUMENTATION.md
- **CHANGELOG_TITLE**: CHANGELOG.md debe comenzar con # Changelog
- **CHANGELOG_UNRELEASED**: Falta la sección ## [Unreleased]
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/dnd5e-spell-advancement
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/foundryvtt-sinregistrar
- **NO_MANIFEST**: Sin module.json en raíz
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/patrol-intelligence
- **README_LANGUAGE_LINK**: README.md no enlaza a README.en.md
- **README_MANIFEST**: README.md no incluye el manifiesto de la última release
- **README_EN_MISSING**: Falta README.en.md; consulta DOCUMENTATION.md
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: patrol
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-cleric-domains-2024-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd5e-2024-cleric-domains, dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-dm-2024-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **UPSTREAM_PATH**: dev-tools/translation/validate-target-labels.mjs: ruta no encontrada systems/dnd5e/lang/en.js
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-dungeon-masters-guide
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-mm-2024-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-monster-manual
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-phandelver-below-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-phandelver-below
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-phb-2024-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-sdr2-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-tashas-cauldron
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-tashas-cauldron
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd-tomb-annihilation
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## foundryvtt-sinregistrar/translate-dnd5e-wizard-schools-2024-es
- **UNVERIFIED**: DND5e 6.1.2: verificación declarada 6.1.1
- **BABELE_COVERAGE**: JSON validado; IDs, nombres, mappings y cobertura requieren los compendios originales y prueba Babele
- **RUNTIME_PENDING**: Sintaxis comprobada; hooks, APIs y comportamiento requieren prueba en Foundry
- **DEPENDENCIES**: Dependencias no instaladas en esta auditoría: dnd5e-2024-wizard-schools, dnd-players-handbook
- Tarea Codex: revisar los hallazgos con sus archivos, adaptar lo necesario y ejecutar una prueba en Foundry con las dependencias indicadas. No cambiar verified automáticamente.

## Límites
No se ejecuta código de terceros. No se cargan Foundry, Babele ni contenido comercial. No se demuestra cobertura de traducciones sin compendios fuente. Los repositorios se auditan en HEAD de su rama por defecto; no necesariamente coinciden con el ZIP publicado.
