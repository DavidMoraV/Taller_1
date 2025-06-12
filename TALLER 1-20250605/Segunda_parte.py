import re

# archivo del Quijote
with open("quijote.txt", "r", encoding="utf-8") as archivo:
    quijote_data = archivo.read()

# expresiones regulares
expresiones_quijote = {
    1: r"(Cap[ií]tulo\s+[^\n]*)",  # encuentra titulos de capitulo
    2: r"\b(\w+)\s+y\s+(\w+)\b",  # palabra antes y después de "y"
    3: r"\b(pra|pre|pri|pro|pru)d",  # silaba seguida de "d"
    4: r"\b(cra|cre|cri|cro|cru)\w*\b",  # palabras que empiezan con cra-cru
    5: r"\b\w+(cho|cha|che|chi|chu)\b"  # palabras que terminan con cho-chu
}

# Ejecutar cada busqueda
resultados_quijote = []
for req_num, pattern in expresiones_quijote.items():
    matches = re.findall(pattern, quijote_data, re.IGNORECASE)
    unique_matches = set(matches) if req_num == 4 else matches
    resultados_quijote.append(
        f"Requerimiento {req_num}:\nPatron: {pattern}\nCoincidencias: {len(unique_matches)}\n"
    )

# Guardar en archivo
with open("busqueda-quijote.txt", "w", encoding="utf-8") as out_file:
    out_file.write("\n".join(resultados_quijote))
