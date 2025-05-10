def rotina_do_juan(dia_da_semana):
   if dia_da_semana in ['segunda', 'segunda-feira','quarta', 'quarta-feira']:
       print('Juan: trabalha e tem aula de inglês.')
   elif dia_da_semana in ['domingo','sábado']:
       print('Juan: joga LoL.')
   else:
       print('Juan trabalha e treina.')


rotina_do_juan(input('Oi, Juan! Que dia é hoje?').strip().lower())
