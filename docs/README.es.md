# Letter Dispatcher — LIGHT

La edición local, todo en el navegador. Abre `index.html` en la raíz de este archivo — la página explica la instalación en ruso, inglés, francés y español (selector RU/EN/FR/ES en la esquina superior de la página).

## Qué contiene el archivo, en resumen

- `app/index.html` — la aplicación en sí (se abre en cualquier navegador, funciona sin conexión después de la primera apertura, se puede instalar como icono en el escritorio o en la pantalla de inicio del teléfono — un botón dentro de la propia aplicación lo hace).
- `extension-lite/` — una extensión ligera para Chrome (abre un borrador de Gmail/Outlook listo para enviar en un clic).
- `docs/` — toda la documentación (este archivo y el resto).

## Qué puede hacer LIGHT y qué no

Funciona completamente en local, en el navegador de cada dispositivo, sin sincronización automática entre dispositivos o personas. La única forma de mover datos es manual — copiar y pegar mediante Google Sheets o Excel (los botones «Copy for Google Sheets» / «Import from Google Sheets» en la pestaña Contacts de la aplicación). Si necesitas sincronización real en vivo para un equipo, consulta el archivo separado **SYNC**; si necesitas archivos instalables independientes (`.exe`/`.apk`), consulta el archivo **EXE**.

## Documentos en esta carpeta

- `beta-tester-guide.ru/en/fr/es.html` — cómo usar la aplicación (para la persona a quien se la entregues).
- `google-sheets-excel-bridge.ru.md` — detalle completo sobre el intercambio con hojas de cálculo (en ruso; pide una traducción si la necesitas).
- `google-sheets-template/` — una plantilla de hoja de contactos ya lista (.xlsx).
- `google-sheets-template-install.ru/en/fr/es.md` — cómo instalar (abrir) esta plantilla específicamente en Google Sheets, y por separado en Excel.
- `quick-install.html`, `install.html` — los mismos pasos de instalación con capturas de pantalla, pensados para la versión ya publicada en línea (enlace incluido).
- `extension-lite/README.ru.md` — instalación de la extensión de Chrome.

*Esta carpeta antes se llamaba «Документы» — ahora es simplemente `docs`, para que el nombre se muestre correctamente en cualquier sistema y en cualquier ruta.*

Ver también: `README.ru.md`, `README.en.md`, `README.fr.md`.
