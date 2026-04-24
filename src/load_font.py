from PyQt6.QtGui import QFontDatabase

def load_font():
    font_id = QFontDatabase.addApplicationFont("style\font\Playfair_Display\PlayfairDisplay-VariableFont_wght.ttf")
    if font_id == -1:
        print("Error: Font could not be loaded!")
        return
        
    # 2. Retrieve the actual font family name (e.g., "Caudex")
    # A single file can contain multiple families, so it returns a list
    families = QFontDatabase.applicationFontFamilies(font_id)
    print(f"Successfully loaded font: {families[0]}")
    
    return families[0]
    