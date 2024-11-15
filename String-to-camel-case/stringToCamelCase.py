'''Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"'''



def to_camel_case(text):
    lista_de_palabras=text.replace("-"," ").replace("_"," ").split()
    string_final=""
    for palabra in lista_de_palabras:
        string_final+=palabra.title()
    return text[:1] + string_final[1:]