# Generar una lista con los elementos pares múltiplos de 3 menores a 1000.

even_numbers_list = []

for num in range(0, 1000, 3):
    even_numbers_list.append(num)


# print(even_numbers_list)

# //////////////////////////////////////////////////////////////////////////////////////////////


# A partir de dos listas A y B, generar dos nuevas listas: una de ellas llamada
# “intersección” con los elementos presentes en A y en B, la otra llamada
# “restante” que tenga los elementos de A y B que no están en ambas listas.

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

intersection = []
remaining = []

for num in list_a:
    if num in list_b:
        intersection.append(num)

for num in list_a:
    if num not in list_b:
        remaining.append(num)

for num in list_b:
    if num not in list_a:
        remaining.append(num)

# print(remainig)
# print(intersection)

# ///////////////////////////////////////////////////////////////////////////////////////////////////


# Dada una lista de tamaño variable determinar si cumple la propiedad "capicua", es decir, si los
# elementos leídos de derecha a izquierda son iguales a los leídos de izquierda a derecha.

odd_list_to_be_determined = [1, 2, 3, 4, 4, 2, 1]
even_list_to_be_determined = [1, 2, 3, 3, 2, 1]

def palindromic(list_to_be_determined):
    if len(list_to_be_determined) % 2 == 0:
        part_1 = list[: len(list_to_be_determined) // 2]
        part_2 = list[len(list_to_be_determined) // 2 :]

        if part_1 == sorted(part_2):
            return "Palindromic"

    else:
        part_1 = list[: len(list_to_be_determined) // 2]
        part_2 = list[len(list_to_be_determined) // 2 :]

        part_2.pop(0)
        
        if part_1 == sorted(part_2):
            return "Palindromic"
        

    return "Not palindromic"


# print(palindromic(odd_list_to_be_determined))
# print(palindromic(even_list_to_be_determined))

# /////////////////////////////////////////////////////////////////////////////////////////


# Implemente una función que dado 4 números enteros indique si hay, al menos, dos
# repetidos.

def repeated(num_a, num_b, num_c, num_d):
    numbers = [num_a, num_b, num_c, num_d]
    non_repeated_numbers = []

    for num in numbers:
        if num not in non_repeated_numbers:
            non_repeated_numbers.append(num)
        else:
            return "The numbers are repeated"

    return "The numbers are not repeated"


# print(repeated(1,3,3,4))

# ///////////////////////////////////////////////////////////////////////////////////////////


# Implemente un programa que ordene los pares calve-valor de un
# diccionario de manera ascendente.

dictionary = {
    1: 10,
    2: 9,
    3: 8,
    4: 7,
    5: 6
}

sort_by_keys = sorted(dictionary.keys())
sort_by_values = sorted(dictionary.values())


# print(sort_by_keys)
# print(sort_by_values)

# ////////////////////////////////////////////////////////////////////////////////////////


# Escriba un programa en Python para combinar una lista de diccionarios en
# un único diccionario. Las claves y los valores de los diccionarios son
# números enteros. En caso que una misma clave esté en varios
# diccionarios, sumar las correspondientes claves.

dict_list = [ {1: 10, 2: 20}, {1: 30, 4: 40}, {4: 50, 6: 60} ]
# output = {1: 40, 2: 20, 4: 90, 6: 60}
output = {}

for dictionary in dict_list:
    for key, val in dictionary.items():
        if dictionary[key] not in output:
            output[key] = val
    
        else:
            output[key] = dictionary[key] + val

print(output)