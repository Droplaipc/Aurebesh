# Diccionario Aurebesh
# - Introducir el texto en español.
# - Traducirlo.
# - Retornar la traducción


def traductor(text_spanish: str):
    # Variables
    aurebesh_dict = {
        'A': '𐲠', 'B': '𐳁', 'C': '𐳂', 'D': '𐳃', 'E': '𐳄',
        'F': '𐳅', 'G': '𐳆', 'H': '𐳇', 'I': '𐳈', 'J': '𐳉',
        'K': '𐳊', 'L': '𐳋', 'M': '𐳌', 'N': '𐳍', 'O': '𐳎',
        'P': '𐳏', 'Q': '𐳐', 'R': '𐳑', 'S': '𐳒', 'T': '𐳓',
        'U': '𐳔', 'V': '𐳕', 'W': '𐳖', 'X': '𐳗', 'Y': '𐳘',
        'Z': '𐳙', " ": " ", "Ñ": "$"
    }
    tildes = ["Á", "É", "Í", "Ó", "Ú"]
    sin_tildes = ["A", "E", "I", "O", "U"]

    # Limpieza de datos
    text_spanish = text_spanish.upper()
    new_phrase = ""

    # Core
    for i in text_spanish:
        if i in tildes:
            i = sin_tildes[tildes.index(i)]
        new_phrase += aurebesh_dict[i]

    return new_phrase



