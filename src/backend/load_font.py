from PyQt6.QtGui import QFontDatabase

# 1. Register the font from the resource file
# Note: Ensure you have imported your compiled resources_rc file
font_id = QFontDatabase.addApplicationFont(":/font/font/Playfair_Display/PlayfairDisplay-VariableFont_wght.ttf")

# 2. Verify the family name (usually "Playfair Display")
if font_id != -1:
    families = QFontDatabase.applicationFontFamilies(font_id)
    if families:
        print(f"Successfully loaded: {families[0]}")
else:
    print("Font failed to load. Check your .qrc path!")