import numpy as np

dados = np.random.uniform(0, 10, 100)

calculos = [f"Média: {np.mean(dados):.2f}", f"Mediana: {np.median(dados):.2f}", f"Desvio Padrão: {np.std(dados):.2f}", f"Valor Máximo: {np.max(dados):.2f}", f"Valor Mínimo: {np.min(dados):.2f}"]

print(calculos)




array_int = np.random.randint(1, 101, 50)

#lista ordenada
print(f"Lista Ordenada: \n{np.sort(array_int)}")



#print dos multiplos de 2

mult_2 = array_int[array_int % 2 == 0]
print(f"Múltiplos de 2: \n{mult_2}\n")


#print dos multiplos de 5

mult_5 = array_int[array_int % 5 == 0]
print(f"Múltiplos de 5: \n{mult_5}\n")


#------------------------------------------------------------------


array_int2 = np.random.randint(1, 100, 50)

array_float = np.random.uniform(0, 10, 50)

pares = array_int[array_int2 % 2 == 0]
print(f"Múltiplos de 2: \n{pares}\n")

multiplos_5 = array_int[array_int2 % 5 == 0]
print(f"Múltiplos de 5: \n{multiplos_5}\n")

print(f"Ordenada: \n{np.sort(array_int2)}")

calculos2 = [f"Média: {np.mean(array_float):.2f}", f"Mediana: {np.median(array_float):.2f}", f"Desvio Padrão: {np.std(array_float):.2f}", f"Valor Máximo: {np.max(array_float):.2f}", f"Valor Mínimo: {np.min(array_float):.2f}"]
print(calculos2)

maioresqcinco = array_int[array_int > 5]
print(f"Maiores que Cinco: {maioresqcinco}")


array_soma = array_int2 + array_float
print(array_soma)

mediaarraysoma = [f"Média do array soma: {np.mean(array_soma):.2f}"]
print(mediaarraysoma)