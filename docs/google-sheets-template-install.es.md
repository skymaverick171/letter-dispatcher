# Cómo instalar nuestra plantilla de hoja de cálculo en Google Sheets y Excel

La carpeta `google-sheets-template/` junto a este archivo contiene un archivo ya preparado, `Letter_Dispatcher_Contacts_Template.xlsx` — una tabla de contactos con las columnas **Name, Email, Office, Group** ya configuradas (el mismo orden que Letter Dispatcher espera al importar). A continuación: cómo abrirla en Google Sheets, y por separado, en Excel.

## Abrirla en Google Sheets

Los archivos `.xlsx` no se abren en Google Sheets con doble clic — hay que subir el archivo a Google Drive una vez. Dos formas de hacerlo, ambas rápidas:

**Opción 1 — mediante Google Drive (recomendada)**

1. Abre [drive.google.com](https://drive.google.com) e inicia sesión con tu cuenta de Google.
2. Haz clic en **«+ Nuevo» → «Subir archivo»** y selecciona `Letter_Dispatcher_Contacts_Template.xlsx`.
3. Una vez subido, haz doble clic en el archivo en Drive → se abre en el visor integrado → arriba, haz clic en **«Abrir con» → «Google Sheets»**.
4. Google crea automáticamente una copia en formato Google Sheets — a partir de ahí es una hoja de cálculo normal, que guarda los cambios automáticamente.

**Opción 2 — directamente desde Google Sheets**

1. Abre [sheets.google.com](https://sheets.google.com) → **«En blanco»** (o «Importar» directamente, si Google lo ofrece).
2. Menú **«Archivo» → «Importar»** → pestaña **«Subir»** → arrastra `Letter_Dispatcher_Contacts_Template.xlsx`, o búscalo.
3. En el cuadro de importación, elige **«Reemplazar hoja de cálculo»** (si abriste una en blanco) o **«Crear nueva hoja de cálculo»** → «Importar datos».

Ambos métodos dan el mismo resultado: una hoja de Google normal con los encabezados y una fila de ejemplo, lista para completar.

## Abrirla en Excel

No hace falta ningún paso adicional — `.xlsx` es el formato nativo de Excel. Simplemente haz doble clic en `Letter_Dispatcher_Contacts_Template.xlsx` y se abrirá como un libro de Excel normal (o usa «Archivo → Abrir» desde dentro de Excel si la carpeta está en otro dispositivo).

## Qué sigue

1. Reemplaza la fila de ejemplo (justo debajo del encabezado) con tus propias personas — una fila por contacto: **Name, Email, Office, Group**.
2. Una vez lista la tabla, copia las filas que necesites (sin la fila de encabezado) y pégalas en Letter Dispatcher mediante el bloque **«Import from Google Sheets»** en la pestaña «Contacts» (más detalles en `google-sheets-excel-bridge.ru.md`, junto a este archivo — por ahora solo en ruso).
3. La columna «Group» define la etiqueta de color del contacto en la aplicación — usa los mismos nombres de grupo para todos a quienes quieras agrupar (por ejemplo «Sales», «VIP», etc.).

El formato de columnas es fijo e idéntico tanto si usas Google Sheets como Excel — es la misma tabla, solo que abierta en aplicaciones distintas.
