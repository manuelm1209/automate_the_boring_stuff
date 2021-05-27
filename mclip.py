#! python3
import pyperclip
import sys

# mclip.py - copia al portapapeles un texto en un diccionario dependiendo de la
# palabra que se ingrese primer argumento de la variable sys.argv

TEXT = {"agree": """Si, estoy de acuerdo. Suena bien para mi.""",
        "busy": """Sorry, can we do this later this week or next week?""",
        "upsell": """Would you consider making this a monthly donation?"""}

keyphrase = sys.argv[1]  # primer argumento en la linea de comandos posterior a mclip.py

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("text for " + keyphrase + "copied to clipboard.")
else:
    print("los valores correctos para ingresar despues de mclip.py son:")
    for i in TEXT:
        print(TEXT[i])
    print("Ejemplo: mclip.py busy")
