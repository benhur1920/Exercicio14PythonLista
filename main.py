#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


def interrogatorio():
  interrogatorio = ["Telefonou para a vítima? (S/N)", "Esteve no local do crime? (S/N)", "Mora perto da vítima? (S/N)", "Devia para a vítima? (S/N)", "Já trabalhou com a vítima? (S/N)"]
  resp = []
  resposta = ''
  for i in range(len(interrogatorio)):
    resposta = verificandoResposta(interrogatorio[i])
    resp.append(resposta)
  return resp  
    
def verificandoResposta(interrogatorio):
  resposta = ''
  while resposta != 's' and resposta != 'n':
    resposta = input(f'\n{interrogatorio}').lower()
  return resposta

def verificarResultado(resp):
  contador = 0
  for i in range(len(resp)):
    if resp[i] == 's':
      contador += 1
  return contador
    
def exibirResultado(contador):
  print('\nResultado do interrogatorio')
  print('-----------------------------')
  print(f'contador = {contador}')
  if contador == 2:
    print("\nSuspeita")
  elif contador > 2 and contador < 5:
    print("Cúmplice")
  elif contador > 4:
    print("Assassino")
  else:
    print("Inocente")

#programa Principal
resp = interrogatorio()
contador = verificarResultado(resp)
exibirResultado(contador)
   