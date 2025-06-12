import re

# archivo de Pi
with open("Pi125MDP.txt", "r") as archivo:
    pi_datos = archivo.read()

#  expresiones regulares
expresiones = {
    1: r"1415",
    2: r"1415[13579]",
    3: r"(?:[02468]){3}",
    4: r"(?:[02468]){3}9",
    5: r"(?:[02468]){3}[13579]",
    6: r"(?:[02468]){3}[09]",
    7: r"(?:[02468]){2}(?:[13579]{1,3})?",
    8: r"(?:[13579]){2}0",
    9: r"[13579](?:[02468]){2,}",
    10: r"11[13579]",
    11: r"11[13579][02468]",
}

# Realizar las busquedas
resultados = []
for req_num, pattern in expresiones.items():
    matches = re.findall(pattern, pi_datos)
    resultados.append(f"Requerimiento {req_num}:\nPatron: {pattern}\nCoincidencias: {len(matches)}\n")

# Guardar en archivo
with open("busqueda-pi.txt", "w") as out_file:
    out_file.write("\n".join(resultados))
