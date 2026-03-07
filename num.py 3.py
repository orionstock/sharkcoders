import numpy as np

dados = np.random.normal(5, 2, 500)

dados_filtrados = dados[dados > 7]

#print(dados_filtrados)

#print(len(dados_filtrados))

#-------------------------------------------------------

dadoss = np.random.normal(20, 5, 365)

dadoss_filtrados = dadoss[dadoss > 30]

#print("Dias com > 30ºC:", len(dadoss_filtrados))

percentagem = (len(dadoss_filtrados) / len(dadoss)) * 100

#print(percentagem)


#----------------------------------------------------

temperatura = np.random.normal(22, 4, 1000)

concentracaoco2 = np.random.normal(400, 50, 1000)

condicao_critica = (temperatura > 28) & (concentracaoco2 > 450)

temperatura_critica = temperatura[condicao_critica]
concentracaoco2_critica = concentracaoco2[condicao_critica]

quantidade_critica = len(temperatura_critica)

percentagem = (quantidade_critica / len(temperatura))

if quantidade_critica > 0:
    calculo1 = np.mean(temperatura_critica), np.std(temperatura_critica)

    calculo2 = np.mean(concentracaoco2_critica), np.std(concentracaoco2_critica)

print(calculo1, calculo2)



