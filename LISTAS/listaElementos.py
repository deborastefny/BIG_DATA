# criação de uma lista com n elementos
frutas = ['banana', 'maçã', 'uva', 'pera', 'abacaxi', 'laranja']

# exibir elementos da lista usando print normal
# print(frutas)

# exibir elementos da lista usando laço de repetição
#for fruta in frutas:
    #print(fruta)
    
    # exibir o primeiro elemento da lista
#print(frutas[0])        

#exibir usando elementos vazios
#print(frutas[1:-2])

#como adicionar elementos na lista
frutas.append('mamão')  
print(frutas)

#inserir elementos na lista
frutas.insert(1, 'morango') 
print(frutas)

#remover elementos da lista
frutas.remove('banana') 
print(frutas)

#tamanho da lista
print(len(frutas))  

#quantidade de vezes que um elemento aparece na lista
print(frutas.count('uva'))

#ordenação da lista
frutas.sort()   
print(frutas)

#inverter a ordem da lista
frutas.reverse()
print(frutas)   


