from Huffman import Huffman

"""
Ejemplo pasando frecuencias preconstruidas
"""
freq = {
    "Z": 2,
    "K": 7,
    "M": 24,
    "C": 32,
    "U": 37,
    "D": 42,
    "L": 42,
    "E": 120
}
hh = Huffman()
input_string = "EDCML"
bb = hh.encode(input_string, freq)
ss = hh.decode(bb)

print("Cadena original: ", input_string)
print()
print("Codificando en bytes: ", bb)
print("Decodificado: ", ss)
print()

print("Tabla resumen ordenado por probabilidad")
hh.print_summary_ordered_by_probability()
print()

print("Arbol de huffman en formato json")
hh.print_huffman_tree()
print()

print("Longitud promedio")
long_promedio = hh.calculate_average_length()
print(long_promedio, " bits por simbolo")

print("Entropia")
entropia = hh.calculate_entropy()
print(entropia)

print("Eficiencia")
print(entropia / long_promedio)

