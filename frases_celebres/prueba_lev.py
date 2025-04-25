''' Prueba de distancia de Levenshtein '''
import Levenshtein

#input1 = "ser o no ser, esa es la cuestion"
#input2 = "hacer o no hacer, no hay intento"
input1 ="el futuro no esta escrito"
input2 = "el futuro no esta establecido"

dist = Levenshtein.distance(input1, input2)
ratio = Levenshtein.ratio(input1, input2)
set_ratio = Levenshtein.setratio(input1, input2)
hamming = Levenshtein.hamming(input1, input2)
print(f"{input1} vs {input2}")
print(f"Distancia: {dist}")
print(f"Ratio: {ratio}")
print(f"Set Ratio: {set_ratio}")
print(f"Hamming: {hamming}")
