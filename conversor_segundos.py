entrada = int(input('Por favor, entre com o número de segundos que deseja converter:'))

dia = entrada // 86400

seg_rest = entrada % 86400

hora = seg_rest // 3600

seg_rest_hora = seg_rest % 3600

minutos = seg_rest_hora // 60

seg_rest_min = seg_rest_hora % 60 

print (dia , 'dias,' , hora ,'horas,' , minutos ,'minutos e' , seg_rest_min, 'segundos.')


