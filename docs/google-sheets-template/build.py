import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter
from openpyxl.comments import Comment

ACCENT = "1E4B8F"
ACCENT_SOFT = "E3EAF6"
GOOD = "2F7A4F"
GOOD_SOFT = "E3F1E8"
INK = "1F2A24"
MUTED = "5C6A63"
BORDER_CLR = "D9DDD4"
STRIPE = "F5F6F3"

# Soft/pastel fill per suggested Group value — matches the app's own
# "assign a soft color to a group" feature, so a row's Group visually
# stands out here the same way its contacts do in the app. Applied via
# conditional formatting (below), which compares against the "Group Names"
# sheet's cells rather than these literal strings — so renaming a value on
# that sheet (see build_group_names_sheet) carries its tint along with it
# instead of breaking it.
GROUP_COLORS = [
    ("Sales", "DCE8FA"),
    ("Support", "E0F2E5"),
    ("Marketing", "EAE0F7"),
    ("VIP", "FBF0CB"),
    ("Partners", "D9F2EE"),
    ("Leads", "FBE2EA"),
    ("Vendors", "FCE8D5"),
    ("Internal", "E7E9E6"),
]

FONT_NAME = "Arial"

thin = Side(style="thin", color=BORDER_CLR)
box = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = openpyxl.Workbook()

# ---------------------------------------------------------------- Contacts
ws = wb.active
ws.title = "Contacts"

headers = ["Name", "Email", "Office address", "Group"]
col_widths = [24, 30, 34, 18]

for i, (h, w) in enumerate(zip(headers, col_widths), start=1):
    col = get_column_letter(i)
    ws.column_dimensions[col].width = w
    cell = ws.cell(row=1, column=i, value=h)
    cell.font = Font(name=FONT_NAME, size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor=ACCENT)
    cell.alignment = Alignment(horizontal="left", vertical="center")
    cell.border = box

ws.row_dimensions[1].height = 24
ws.freeze_panes = "A2"

examples = [
    ["Jane Doe (example)", "jane.doe@example.com", "500 Market St, San Francisco", "Sales"],
    ["John Smith (example)", "john.smith@example.com", "12 rue de Rivoli, Paris", "Support"],
]
example_font = Font(name=FONT_NAME, size=10.5, italic=True, color=MUTED)
for r, row in enumerate(examples, start=2):
    for c, val in enumerate(row, start=1):
        cell = ws.cell(row=r, column=c, value=val)
        cell.font = example_font
        cell.fill = PatternFill("solid", fgColor=STRIPE)
        cell.border = box
        cell.alignment = Alignment(vertical="center")

ws["A2"].comment = Comment(
    "Пример строки — можно удалить или перезаписать своими данными.\n"
    "Example row — delete or overwrite with your own data.\n"
    "Ligne d'exemple — supprimez-la ou remplacez-la par vos données.",
    "Letter Dispatcher template",
)

first_blank = 4
last_blank = 200
normal_font = Font(name=FONT_NAME, size=10.5, color=INK)
for r in range(first_blank, last_blank + 1):
    band = PatternFill("solid", fgColor=STRIPE) if r % 2 == 0 else PatternFill(fill_type=None)
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=r, column=c)
        cell.font = normal_font
        cell.fill = band
        cell.border = box

ws.sheet_view.showGridLines = False

# ---------------------------------------------------------------- Group Names (visible, editable — backs the Group dropdown)
# Kept as a normal, visible sheet (not hidden, as the very first version of
# this template had it) specifically so people can find and rename these
# values themselves — see the "Customize the group names" section in each
# Instructions sheet. The Contacts dropdown and the row-tint conditional
# formatting both point at these cells rather than literal text, so editing
# a name here (or adding one in a currently-blank row) takes effect
# everywhere in the file immediately, with no other edits required.
GN_SHEET = "Group Names"
gn_ws = wb.create_sheet(GN_SHEET)
group_presets = [g for g, _ in GROUP_COLORS]

gn_ws.column_dimensions["A"].width = 50
gn_ws["A1"] = "Group Names"
gn_ws["A1"].font = Font(name=FONT_NAME, size=16, bold=True, color=ACCENT)
gn_ws["A2"] = (
    "These are the choices offered in the Group dropdown on the Contacts sheet, and the "
    "color each matching row gets tinted there. Rename any value below or replace it with "
    "your own — the dropdown and the row colors update immediately, everywhere in this file."
)
gn_ws["A2"].font = Font(name=FONT_NAME, size=10.5, color=MUTED)
gn_ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
gn_ws.row_dimensions[2].height = 82

GN_HEADER_ROW = 4
GN_FIRST_ROW = GN_HEADER_ROW + 1
GN_LAST_ROW = GN_FIRST_ROW + len(group_presets) - 1

hc = gn_ws.cell(row=GN_HEADER_ROW, column=1, value="Group name")
hc.font = Font(name=FONT_NAME, size=11, bold=True, color="FFFFFF")
hc.fill = PatternFill("solid", fgColor=ACCENT)

for i, g in enumerate(group_presets):
    r = GN_FIRST_ROW + i
    cell = gn_ws.cell(row=r, column=1, value=g)
    cell.font = Font(name=FONT_NAME, size=11, color=INK)
    cell.fill = PatternFill("solid", fgColor=GROUP_COLORS[i][1])

dv = DataValidation(
    type="list",
    formula1=f"='{GN_SHEET}'!$A${GN_FIRST_ROW}:$A${GN_LAST_ROW}",
    allow_blank=True,
    showDropDown=False,
)
dv.error = "Choose a group from the list, or type your own — this is just a suggestion, not a strict rule."
dv.errorTitle = "Custom group"
dv.error_style = "information"
ws.add_data_validation(dv)
dv.add(f"D2:D{last_blank}")

# Tint each row by its Group value — soft colors matching the app's own
# per-group tinting. Applies to the whole visible row (A:D) so a contact
# reads as belonging to its group at a glance, same intent as the app.
# Compares against the Group Names cell (not the literal text) so a rename
# there is picked up automatically instead of silently breaking the tint.
cf_range = f"A2:D{last_blank}"
for i, (group_name, hex_color) in enumerate(GROUP_COLORS):
    gn_row = GN_FIRST_ROW + i
    fill = PatternFill("solid", fgColor=hex_color)
    ws.conditional_formatting.add(
        cf_range,
        FormulaRule(formula=[f"$D2='{GN_SHEET}'!$A${gn_row}"], fill=fill, stopIfTrue=True),
    )

# ---------------------------------------------------------------- Instructions (generic builder, one per language)

def build_instructions_sheet(wb, sheet_name, t):
    ins = wb.create_sheet(sheet_name)
    ins.sheet_view.showGridLines = False
    ins.column_dimensions["A"].width = 3
    ins.column_dimensions["B"].width = 92

    row = [2]

    def title_row(text, size=16):
        c = ins.cell(row=row[0], column=2, value=text)
        c.font = Font(name=FONT_NAME, size=size, bold=True, color=ACCENT)
        row[0] += 1

    def section_row(text):
        r = row[0]
        ins.merge_cells(start_row=r, start_column=2, end_row=r, end_column=2)
        c = ins.cell(row=r, column=2, value=text)
        c.font = Font(name=FONT_NAME, size=12, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=ACCENT)
        c.alignment = Alignment(vertical="center", indent=1)
        ins.row_dimensions[r].height = 22
        row[0] += 1

    def body_row(text, bold=False, color=INK, wrap=True, height=None):
        r = row[0]
        c = ins.cell(row=r, column=2, value=text)
        c.font = Font(name=FONT_NAME, size=10.5, bold=bold, color=color)
        c.alignment = Alignment(vertical="top", wrap_text=wrap)
        if height:
            ins.row_dimensions[r].height = height
        row[0] += 1

    def callout_row(text, fill=ACCENT_SOFT, text_color=ACCENT, height=44):
        r = row[0]
        ins.merge_cells(start_row=r, start_column=2, end_row=r, end_column=2)
        c = ins.cell(row=r, column=2, value=text)
        c.font = Font(name=FONT_NAME, size=10.5, bold=True, color=text_color)
        c.fill = PatternFill("solid", fgColor=fill)
        c.alignment = Alignment(vertical="center", horizontal="left", wrap_text=True, indent=1)
        ins.row_dimensions[r].height = height
        row[0] += 1

    def legend_row(swatch_hex, label):
        # Colors the label cell itself (rather than a separate narrow swatch
        # column) so the sample renders reliably in every viewer/exporter —
        # a thin column-A swatch turned out invisible in some PDF exports.
        r = row[0]
        lb = ins.cell(row=r, column=2, value=label)
        lb.font = Font(name=FONT_NAME, size=10.5, bold=True, color=INK)
        lb.fill = PatternFill("solid", fgColor=swatch_hex)
        lb.border = box
        lb.alignment = Alignment(vertical="center", indent=1)
        ins.row_dimensions[r].height = 20
        row[0] += 1

    def blank():
        row[0] += 1

    title_row(t["title"])
    body_row(t["subtitle"], color=MUTED)
    blank()

    section_row(t["s1_head"])
    body_row(t["s1_body"], height=t["s1_h"])
    blank()

    section_row(t["s2_head"])
    body_row(t["s2_body"], height=t["s2_h"])
    blank()

    section_row(t["s3_head"])
    body_row(t["s3_body"], height=t["s3_h"])
    blank()

    section_row(t["s4_head"])
    body_row(t["s4_body"], height=t["s4_h"])
    for group_name, hex_color in GROUP_COLORS:
        legend_row(hex_color, group_name)
    blank()

    callout_row(t["callout"], height=t["callout_h"])
    blank()

    body_row(t["footer"], color=MUTED, height=t["footer_h"])
    blank()

    section_row(t["s5_head"])
    body_row(t["s5_body"], height=t["s5_h"])

    return ins


RU = dict(
    title="Letter Dispatcher ↔ Google Sheets",
    subtitle="Как использовать эту таблицу как адресную книгу для приложения Letter Dispatcher.",
    s1_head="1. Заполните лист «Contacts»",
    s1_body=(
        "Столбцы должны идти строго в этом порядке: Name, Email, Office address, Group.\n"
        "Обязательны только Name и Email (в правильном формате, например name@example.com) — "
        "Office address и Group можно оставлять пустыми.\n"
        "Строки с пометкой «(example)» — это образец, их можно удалить или заменить своими данными."
    ),
    s1_h=55,
    s2_head="2. Перенести контакты ИЗ таблицы в приложение",
    s2_body=(
        "1) Выделите заполненные строки в Contacts (можно вместе с заголовком — приложение само его распознает).\n"
        "2) Скопируйте (Ctrl+C / ⌘+C).\n"
        "3) В Letter Dispatcher откройте вкладку Contacts → «Import from Google Sheets».\n"
        "4) Вставьте (Ctrl+V) в поле и нажмите «Import pasted rows»."
    ),
    s2_h=70,
    s3_head="3. Перенести контакты ИЗ приложения обратно в таблицу",
    s3_body=(
        "В Letter Dispatcher, вкладка Contacts:\n"
        "• «Copy for Google Sheets» — скопирует все контакты в буфер обмена, вставьте их в лист Contacts.\n"
        "• «Download CSV» — скачает файл .csv, который Google Sheets открывает через Файл → Импортировать."
    ),
    s3_h=55,
    s4_head="4. Подсветка строк по группе",
    s4_body=(
        "Как и в самом приложении, строка автоматически подсвечивается мягким цветом в зависимости "
        "от значения в столбце Group — для этих восьми вариантов из выпадающего списка:"
    ),
    s4_h=40,
    callout=(
        "ℹ  Это ручной обмен буфером обмена / файлом, а не автоматическая синхронизация — "
        "изменения в одном месте не появляются в другом сами по себе, перенос нужно повторять."
    ),
    callout_h=44,
    footer=(
        "Столбец Group в Contacts подсказывает варианты выше, но можно вписать и своё значение — "
        "это не строгий список."
    ),
    footer_h=28,
    s5_head="5. Настройка названий групп",
    s5_body=(
        "Откройте лист «Group Names» (вкладка внизу этого файла), чтобы переименовать любой из "
        "восьми вариантов или заменить его своим — выпадающий список на листе Contacts и цвета "
        "строк выше обновятся сразу же, во всём файле.\n"
        "Контакты, у которых уже стоит старое название, сохранят его как обычный текст — если нужно "
        "обновить и их, используйте Найти и заменить (Ctrl+H) по столбцу Group."
    ),
    s5_h=74,
)

EN = dict(
    title="Letter Dispatcher ↔ Google Sheets",
    subtitle="How to use this sheet as the address book for the Letter Dispatcher app.",
    s1_head='1. Fill in the "Contacts" sheet',
    s1_body=(
        "Columns must be in exactly this order: Name, Email, Office address, Group.\n"
        "Only Name and Email are required (in a valid format, e.g. name@example.com) — "
        "Office address and Group can be left blank.\n"
        'Rows marked "(example)" are sample data — delete them or overwrite with your own.'
    ),
    s1_h=55,
    s2_head="2. Bring contacts FROM this sheet INTO the app",
    s2_body=(
        "1) Select the filled-in rows in Contacts (you can include the header row — "
        "the app recognizes it automatically).\n"
        "2) Copy (Ctrl+C / ⌘+C).\n"
        '3) In Letter Dispatcher, open the Contacts tab → "Import from Google Sheets".\n'
        '4) Paste (Ctrl+V) into the box and click "Import pasted rows".'
    ),
    s2_h=70,
    s3_head="3. Bring contacts FROM the app BACK into this sheet",
    s3_body=(
        "In Letter Dispatcher, Contacts tab:\n"
        '• "Copy for Google Sheets" — copies all contacts to your clipboard; paste them into the Contacts sheet.\n'
        '• "Download CSV" — downloads a .csv file, which Google Sheets opens via File → Import.'
    ),
    s3_h=55,
    s4_head="4. Row colors by group",
    s4_body=(
        "Just like in the app, a row is automatically tinted a soft color based on its Group value — "
        "for these eight options from the dropdown list:"
    ),
    s4_h=40,
    callout=(
        "ℹ  This is a manual clipboard/file exchange, not automatic syncing — changes made in one place "
        "don't appear in the other by themselves; you need to repeat the transfer."
    ),
    callout_h=44,
    footer=(
        "The Group column in Contacts suggests the options above, but you can type your own value too — "
        "it isn't a strict list."
    ),
    footer_h=28,
    s5_head="5. Customize the group names",
    s5_body=(
        "Open the “Group Names” sheet (tab at the bottom of this file) to rename any of the "
        "eight options, or replace them with your own — the dropdown on the Contacts sheet and the row "
        "colors above update immediately, everywhere in this file.\n"
        "Contacts that already have the old name keep it as plain text; use Find & Replace (Ctrl+H / "
        "⌘+H) on the Group column if you want to update them too."
    ),
    s5_h=74,
)

FR = dict(
    title="Letter Dispatcher ↔ Google Sheets",
    subtitle="Comment utiliser cette feuille comme carnet d'adresses pour l'application Letter Dispatcher.",
    s1_head="1. Remplissez la feuille « Contacts »",
    s1_body=(
        "Les colonnes doivent être exactement dans cet ordre : Name, Email, Office address, Group.\n"
        "Seuls Name et Email sont obligatoires (au bon format, par ex. name@example.com) — "
        "Office address et Group peuvent rester vides.\n"
        "Les lignes marquées « (example) » sont des exemples — supprimez-les ou remplacez-les par vos propres données."
    ),
    s1_h=78,
    s2_head="2. Transférer les contacts DE cette feuille VERS l'application",
    s2_body=(
        "1) Sélectionnez les lignes remplies dans Contacts (vous pouvez inclure l'en-tête — "
        "l'application le reconnaît automatiquement).\n"
        "2) Copiez (Ctrl+C / ⌘+C).\n"
        "3) Dans Letter Dispatcher, ouvrez l'onglet Contacts → « Import from Google Sheets ».\n"
        "4) Collez (Ctrl+V) dans le champ et cliquez sur « Import pasted rows »."
    ),
    s2_h=70,
    s3_head="3. Ramener les contacts DE l'application VERS cette feuille",
    s3_body=(
        "Dans Letter Dispatcher, onglet Contacts :\n"
        "• « Copy for Google Sheets » — copie tous les contacts dans le presse-papiers ; collez-les dans la feuille Contacts.\n"
        "• « Download CSV » — télécharge un fichier .csv, que Google Sheets ouvre via Fichier → Importer."
    ),
    s3_h=55,
    s4_head="4. Couleur des lignes selon le groupe",
    s4_body=(
        "Comme dans l'application, une ligne est automatiquement teintée d'une couleur douce selon sa valeur "
        "de Group — pour ces huit options de la liste déroulante :"
    ),
    s4_h=40,
    callout=(
        "ℹ  Il s'agit d'un échange manuel (presse-papiers ou fichier), pas d'une synchronisation automatique — "
        "les changements faits d'un côté n'apparaissent pas de l'autre tout seuls ; il faut répéter le transfert."
    ),
    callout_h=44,
    footer=(
        "La colonne Group dans Contacts suggère les valeurs ci-dessus, mais vous pouvez aussi saisir la "
        "vôtre — ce n'est pas une liste stricte."
    ),
    footer_h=28,
    s5_head="5. Personnaliser les noms de groupes",
    s5_body=(
        "Ouvrez la feuille « Group Names » (onglet en bas de ce fichier) pour renommer l'une des huit "
        "options, ou la remplacer par la vôtre — la liste déroulante de la feuille Contacts et les couleurs "
        "de lignes ci-dessus se mettent à jour immédiatement, partout dans ce fichier.\n"
        "Les contacts qui ont déjà l'ancien nom le gardent en texte simple ; utilisez Rechercher/Remplacer "
        "(Ctrl+H / ⌘+H) sur la colonne Group si vous voulez aussi les mettre à jour."
    ),
    s5_h=74,
)

build_instructions_sheet(wb, "Instructions (EN)", EN)
build_instructions_sheet(wb, "Instructions (FR)", FR)
build_instructions_sheet(wb, "Инструкция (RU)", RU)

import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "Letter_Dispatcher_Contacts_Template.xlsx"
wb.save(OUT)
print("saved", os.path.abspath(OUT))
