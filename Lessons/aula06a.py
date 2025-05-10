#Estrutura de dados - LISTAS []

event_list = [1848, 'Mazzini', 'Pio IX', 'Piemonte', 1871, 'V.E.R.D.I']
#Primeiro valor da lista é 0
print(event_list[1])
print(event_list[-1])
print(event_list[:3])
print(event_list[-4:-2])
print(len(event_list))

#Mudando itens na lista
event_list[2] = 'Garibaldi'
print(event_list)
print(event_list[1:3]) #O Python desconsidera o item a direita do número indicado.

#Juntando listas
new_events_list = ['Roma', 'Mola di Gaetta']
event_list = event_list + new_events_list
print(event_list)

