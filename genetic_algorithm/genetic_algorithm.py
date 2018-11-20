#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import math
import matplotlib.pyplot as plt

cidades = []
distancia_min = []

ponto_x = open("data/coordenadasx.dat", 'r').readlines()
ponto_y = open("data/coordenadasy.dat", 'r').readlines()

pontos = int(random.randrange(1, 32))
print(pontos, "pontos especificos")

for i in range(0, pontos): 
    cidades.append( [ ponto_x[random.randint(0, len(ponto_x)-1)], ponto_y[random.randint(0, len(ponto_y)-1)] ] )

print(cidades)
input()

# distancia entre 2 pontos
def get_distancia(p1, p2): 
    if not isinstance(p1, list) or not isinstance(p2, list):
        print("entre com dois pontos (X, Y).")
        return
    return (math.sqrt( math.pow(int(p1[0]) - int(p2[0]), 2) + math.pow(int(p1[1]) - int(p2[1]), 2)))

# funcao objetivo
# soma de todas as distâncias das cidades 
def fitness(lista): 
    soma = 0

    if not isinstance(lista, list):
        print("entre com uma lista como paramentro")
    
    for i in range(0, len(lista)-1):      
        soma += (int(get_distancia(cidades[lista[i]], cidades[lista[i+1]])))
        if i == len(lista)-2:                        
            break            
    return soma 

# distancia entre cada cidade em uma lista
def distancia_entre_pontos(lista): 
    distancia_atual = []    
    
    if not isinstance(lista, list):
        print("entre com uma lista como paramentro")
    
    for i in range(0, len(lista)):
        distancia_atual.append(get_distancia(cidades[lista[i]], cidades[lista[i+1]]))
        if i == len(lista)-2:                                    
            break        
    return distancia_atual

# funcao para geracao de pares
def gerar_pares(lista, qtd):
    pares = []
    sorteados = []
    done = False

    for i in range(0, qtd):
        dois_a_dois = []
        
        while True:
            par_1 = random.randint(0, len(lista) - 1)           

            if par_1 not in sorteados:
                while True:
                    par_2 = random.randint(0, len(lista) - 1)                    
                    if par_2 not in sorteados and par_1 != par_2:
                        dois_a_dois.append(lista[par_1])
                        dois_a_dois.append(lista[par_2])
                        sorteados.append(par_1)
                        sorteados.append(par_2)
                        done = True
                        break
            if done == True:
                done = False
                pares.append(dois_a_dois)
                break
    plt.plot(pares)
    return pares
                
# roleta: lista de distâncias invertidas
# qtd: quantidade de indivíduos.
def roletar(roleta, qtd):   
    if not isinstance(roleta, list):
        print("entre com uma lista como paramentro")
        
    populacao = []
    # cada indice da roleta representa uma porcentagem => total = 1
    rodando_roleta = roleta[0]
    spin = []
    
    for i in range(0, len(roleta)):        
        spin.append(rodando_roleta)
        rodando_roleta += roleta[i]        
    
    for i in range(0, qtd):
        aleatorio = random.random()        
        nova_populacao = 0                         
        
        for j in range(0, len(spin)):
            if aleatorio < spin[j]:
                break
            else:
                nova_populacao += 1                
        populacao.append(nova_populacao)
    plt.plot(populacao)
    return populacao

# funcao de troca
def crossover(pares, entrada): 
    cortes = []
    
    for i in range(0, int(entrada/2)):
        cut_point = random.randint( int(len(cidades) / 2), len(cidades) - 1)        
        cortes.append(int(cut_point))        

    cut_pares = [] 
    left_pares = [] 
    original_pares = []
    
    cp = []
    lp = []
    op = []
    index = 0    

    for i in range(0, len(pares)):
        for j in range(0, len(pares[i])):
            avoid_error = False
            for k in range(0, len(cidades)):      
                # obtem o idice do par da populacao gerada
                index = pares[i][j]
                # obtem a cidade correspondente a uma população
                cidade = populacao[j][k]
                op.append(cidade)
                
                if k <= cortes[i]:
                    cp.append(cidade)
                else:
                    lp.append(cidade)

            cut_pares.append(cp)
            left_pares.append(lp)
            original_pares.append(op)
            
            cp = []
            lp = []
            op = []            
            
    print("\npontos de corte: ", cortes, "(INDEXS)")

    i = 0
    
    while i < len(cut_pares):
        for j in range(0, 1):
                for k in range(0, len(original_pares[i+1])):
                    if original_pares[i+1][k] not in cut_pares[i]:
                        cut_pares[i].append(original_pares[i+1][k])
                for k in range(0, len(original_pares[i])):
                    if original_pares[i][k] not in cut_pares[i+1]:
                        cut_pares[i+1].append(original_pares[i][k])                                
        i += 2
    return cut_pares          
            
# funcao de mutação
def mutacao(pares): 
    mutacao = 0.1
    rand = 0    
    
    # por par...
    for i in range(0, len(pares)-1): 
        # par por cidade
        for j in range(0, len(pares[i])): 
            rand = random.random()
            if rand <= mutacao:
                print("mutação no par ", i)
                pos_1 = random.randint(0, len(cidades)-1)
                while True:
                    pos_2 = random.randint(0, len(cidades)-1)
                    if pos_1 != pos_2:
                        aux = pares[i][pos_1]
                        pares[i][pos_1] = pares[i][pos_2]
                        pares[i][pos_2] = aux                        
                        break  
    plt.plot(pares)
    return pares

# gerando pontos
def gerando_pontos(): 
    ponto_selecionado = []
    ponto_selecionado.append(0)
    contador = 0
    
    # cidade escolhida dentre as 100
    while True:
        chosen_city = random.randint(1, len(cidades)-1) 
        # adicionar a cidade na lista caso ainda não esteja
        if not chosen_city in ponto_selecionado: 
            # adicionando na lista as cidades sorteadas
            ponto_selecionado.append(chosen_city) 
            contador += 1
        if contador == len(cidades)-1:
            break
    plt.plot(ponto_selecionado)
    return ponto_selecionado

populacao = []
distancia = []
roleta = []
distancia_invertida = []

entrada = input("quantidade inicial da populaçao: ")
entrada = int(entrada)

nova_populacao = []

qtd_execucao = input("informe quantas vezes o procedimento deverá ser executado: ")
qtd_execucao = int(qtd_execucao)

for i in range(0, entrada): # Gera os N indivíduos iniciais
    nova_populacao = gerando_pontos()
    populacao.append(nova_populacao) # Adiciona a lista de Cidades sorteadas à Lista de Populações!                             

for i in range(0, qtd_execucao):
    if i == 0:
        for i in range(0, len(populacao)):
            print(populacao[i])
        for j in range(0, len(populacao)):
            # somatorio das distancias
            resultado_fitness = fitness(populacao[j]) 
             # adicionando a distancia entre os pontos na lista de distancia
            distancia.append(resultado_fitness)            
            # distancias invertidas
            distancia_invertida.append(1 / resultado_fitness) 
    else:
        for j in range(0, len(populacao)):
            resultado_fitness = fitness(populacao[j])
            distancia.append(resultado_fitness)            
            distancia_invertida.append(1 / resultado_fitness)
    
    print("distancias após troca 'crossover'  --> ", distancia, "\n")
    print(" ------- > menor distancia: ", float(min(distancia)), "m." )    
    distancia_min.append(float(min(distancia)))

    # distancia_invertida / somatorio das distancias
    for i in range(0, len(distancia_invertida)):
        roleta.append( (distancia_invertida[i] / sum(distancia_invertida)) ) 

    rodar_populacao = roletar(roleta, entrada)
    pares = gerar_pares(rodar_populacao, int(entrada/2))
    
    print("--------------------------------------------------------------------------------")
    pares = mutacao(crossover(pares, entrada))
    for i in range(0, len(pares)):
        print(pares[i])
    nova_populacao = []
    
    populacao = []

    for i in range(0, len(pares)):    
        populacao.append(pares[i])

    resultado_fitness = []
    plt.plot(resultado_fitness)
    roleta = []
    plt.plot(roleta)
    
print("--------------------------------------------------------------------------------")
print("procedimento", qtd_execucao, " vezes executado", " com pop inicial = ", entrada)
print("\nmenor distancia encontrada: ", min(distancia_min), " m.")

file = open('distancias.txt', 'w')
file.close()

file = open('distancias.txt', 'w')

for i in range(0, len(distancia_min)):
    file.write(str(int(distancia_min[i]))+"\n")

file.close()

input("\nprecione qualquer tecla para continuar...")

plt.show()


# In[ ]:




