"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

list_a = [1, 2, 3, 44, 5, 6, 7]
list_b = [1, 2, 3, 4]
a_b = list(zip(list_a, list_b))

sum_list = [sum(i) for i in a_b]

print(sum_list)