from Huffman import Huffman

""" Ejemplo sin pasar frecuencias"""
h = Huffman()
in_string = "Electronica y comunicaciones"
b = h.encode(in_string)
s = h.decode(b)

print("Cadena original: ", in_string)
print()
print("Codificando en bytes: ", b)
print("Decodificado: ", s)
print()

print("Tabla resumen ordenado por probabilidad")
h.print_summary_ordered_by_probability()
print()

print("Arbol de huffman en formato json")
h.print_huffman_tree()
print()

print("Longitud promedio")
l_promedio = h.calculate_average_length()
print(l_promedio, " bits por simbolo")

print("Entropia")
entr = h.calculate_entropy()
print(entr)

print("Eficiencia")
print(entr / l_promedio)

