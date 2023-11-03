#!/usr/bin/env python
# coding: utf-8

# # Conversão de todas as bases
# ## Anotação: Em alguns casos com decimais como .25 e .75 os valores são calculados incorretamente. Revisar a parte do cálculo fracionário, mas o cálculo inteiro continua funcionando. Talvez posso reduzir ainda mais o código também.

# In[14]:


from IPython.display import clear_output
from time import sleep

# Limpar terminal
def limpar_terminal():
    clear_output(wait=True)

# Verificar o sinal
def sinal_n(n):
  sinal = False
  if '-' in n: # Caso lista contenha "-" no caso da hexadecimal
    n.remove('-') # Remove sinal da lista
    sinal = True
  return sinal, n

# Quebrar o número se conter '.'
def break_dot(base,opcao,numero):
  limpar_terminal()
  convertido.append(''.join(str(digito) for digito in numero))
  sinal, numero = sinal_n(numero)
  trocar_num(numero, base)

  if '.' in numero: # Se o número contém vírgula faça
    inteira = numero[:numero.index('.')]
    decimal = numero[numero.index('.'):]
    decimal.remove('.')
  else: # Senão apenas inteiro
    inteira = numero
    decimal = 0

  result(base, opcao, inteira, decimal, sinal)

def result(b,o,i,d,s):

  # Verificar Opções
  if o == '1':
    ans = inteira(i, d, b, s)
  if o == '2':
    ans = convert_to_dec(i, d, b, s)
  ans = (''.join(str(digito) for digito in ans))

  imprimirConv(ans,b,o)


def trocar_char(n,resultado): # Trocar número por caractere
  if n == 10:
    resultado.append('A')
  if n == 11:
    resultado.append('B')
  if n == 12:
    resultado.append('C')
  if n == 13:
    resultado.append('D')
  if n == 14:
    resultado.append('E')
  if n == 15:
    resultado.append('F')
  return resultado

def trocar_num(num,b): # Trocar caractere por número
  if b == 16:
    for i in range(0, len(num), 1):
      if 'A' == num[i]:
        num[i] = 10
      if 'B' == num[i]:
        num[i] = 11
      if 'C' == num[i]:
        num[i] = 12
      if 'D' == num[i]:
        num[i] = 13
      if 'E' == num[i]:
        num[i] = 14
      if 'F' == num[i]:
        num[i] = 15

# Conversão de bases para decimal

def convert_to_dec(i, d, b, s):
  resultado = []
  if s == True:
        resultado.append('-')
  ans = 0
  indice = 0
  expoente = len(i)

  while expoente > 0: # Enquanto maior que zero faça

    expoente -= 1 # Ex.: len(i) = 1iter ---> expoente = 4 - 1 / 2iter --> expoente = 3 - 1 ...
    ans += (b**expoente)*(int(i[indice])) # b^e x n
    indice += 1 # Começa do primeiro algarismo Ex.: 1iter ---> indice = 0 2iter ---> indice = 1 ...

  if d != 0: # Se decimal diferente de zero faça

    expoente = -(len(d))

    while expoente < 0: # Enquanto maior que zero

      indice = -(expoente + 1) # Começa do último algarismo | Ex.: len(i) = 1iter ---> indice = -(-4 + 1) = 3
      ans += (b**expoente)*(int(d[indice]))
      expoente += 1 #Ex.: len(d) = 1iter---> expoente = -4 + 1 = -3

  resultado.append(ans)
  return resultado

# Conversão inteira

def inteira(n,d,b,s):
    resultado = []

    if s == True:
        resultado.append('-')
    # Checar qual base converter
    if b == 2:
      base = [0,1]
    if b == 8:
      base = [0,1,2,3,4,5,6,7]
    if b == 16:
      base = [0,1,2,3,4,5,6,7,8,9]


    n = int(''.join(digito for digito in n))
    if n in base:# Se há n em base faça
        resultado.append(base[base.index(n)])
    else:
       while n >= b: # Enquanto for maior igual b faça
        if n % b > 9:
          resultado = trocar_char(n % b, resultado) # Caso maior que 9 faz a troca
        else:
          resultado.append(n % b) # adiciona o resto
        n = n//b # divisão inteira
        #print(n) # teste
        if n < b: # se n menor que a base
          if b == 16 and n > 9:
            resultado = trocar_char(n,resultado)
          else:
            resultado.append(n) # adicione
          resultado.reverse() # inverter para leitura correta

    resultado = trocar_char(n,resultado)

    if d != 0:
      resultado.append('.')
      resultado = decimal(d, b, resultado)

    return resultado

# Conversão decimal

def decimal(n,b,resultado):

    n = float(''.join(digito for digito in n))/10

    contador = 0
    while n != 0: # Enquanto não for 0 faça

        """
        Ex.:
        b = 8
        n = 0.625
        n = n*8 = 5.0
        adicionar 5 ao resultado
        separa 0.0
        fim
        """

        n = n*b # Multiplicar n por b Ex.: 0.625 * 5 =
        n = list(str(n)) # Transformar n em lista de caracteres
        resultado.append(''.join(digito for digito in n[:n.index('.')])) # Adicionar digito antes da virgula Ex.: 5
        n= n[n.index('.'):] # Separar a parte inteira Ex.: ['.','0']
        n = float(''.join(digito for digito in n))  # Unir de lista de string em único string para float Ex.: ['.','0'] -> 0.0

        if (n % b): # Se d seja divisível por b então faça
                contador += 1 # Adicione 1 ao contador
                if contador == 8:
                    return resultado

    return resultado

# Imprimir resultado

def imprimirConv(ans,base,opcao):
    limpar_terminal()
    if opcao == '1':
      if base == 2:
        print("Base Binária (", end="")
      if base == 8:
        print("Base Octal (", end="")
      if base == 16:
        print("Base Hexadecimal (", end="")
    if opcao == '2':
      print("Base Decimal (", end="")
      base = 10

    print(ans,end=")")
    print(base)
    ans_historico.append(ans) # adiciona historico na memoria
    base_ans.append(base) # adiciona o histórico numeros convertidos na base númerica


# Imprimir cada mensagem do menu de acordo com opção
def imprimirMsg(opcao):
  if opcao == '1':
    mensagem = f"""
    1. DEC ----> BIN
    2. DEC ----> OCT
    3. DEC ----> HEX
    4. All
    Any. Back
    """
  if opcao == '2':
     mensagem = f"""
    1. BIN ----> DEC
    2. OCT ----> DEC
    3. HEX ----> DEC
    4. All
    Any. Back
      """
  if opcao == 'menu':
    mensagem = f"""
    Conversões
    ----------
    1. DEC ----> BIN, OCT, HEX
    2. DEC <---- BIN, OCT, HEX
    3. BIN, OCT e HEX <----> BIN, OCT, HEX
    4. END
      """
  print(mensagem)

def menu():
  print("Digite qualquer tecla")
  input()
  limpar_terminal()
  imprimirMsg('menu')
  # Limpar o resultado
  # resultado = [] # declarar lista vazia (não funciona?)
  # resultado.clear() # método clear()
  # resultado[:] = [] # operador slicing


  opcao1 = input()
  sleep(0.5) # Espera n segundos
  limpar_terminal()

  if opcao1 == '1':

    imprimirMsg(opcao1)
    opcao2 = input()
    if opcao2 == '1':
        break_dot(2,'1',set_entrada())
    if opcao2 == '2':
        break_dot(8,'1',set_entrada())
    if opcao2 == '3':
        break_dot(16,'1',set_entrada())
    if opcao2 == '4':
      print("Em construção")

  if opcao1 == '2':

    imprimirMsg(opcao1)
    opcao2 = input()
    if opcao2 == '1':
        break_dot(2,'2',set_entrada())
    if opcao2 == '2':
        break_dot(8,'2',set_entrada())
    if opcao2 == '3':
        break_dot(16,'2',set_entrada())
    if opcao2 == '4':
      print("Em construção")
  if opcao1 == '3':
    print("Em construção")
  if opcao1 == '4':
    print("")
  else:
    menu()

  # Ao final das conversões vai imprimir isso
  limpar_terminal()
  # Printar conversões
  print("Memória: ",end="")
  i = 0
  for numero in ans_historico:
    print("(", end='')
    print(numero,end='')
    print(")", end='')
    print(base_ans[i], ";", end='')
    i += 1
  print("")
  # Printar números quais números foram convertidos
  print("Convertido: ",end="")
  for numero in convertido:
    print(" ",numero,";", end='')

def set_entrada():
   print("Digite o número a ser convertido: ", end="")
   numero = list(input()) # Entrada
   return numero

ans_historico = []
base_ans = []
convertido = []
menu()


# ## Anotação: O código antigo que eu fiz aparentemente não tem esse erro, mas não consigo identificar o motivo dessa resposta diferente ainda. 

# In[15]:


# Conversão inteira
def inteira(n,b):

    # Checar qual base converter
    if b == 2:
      base = [0,1]
    if b == 8:
      base = [0,1,2,3,4,5,6,7]
    if b == 16:
      base = [0,1,2,3,4,5,6,7,8,9]
      trocarChar(n)


    if n in base:# Se há n em base faça
        resultado.append(base[base.index(n)])
    else:
       while n >= b: # Enquanto for maior igual b faça
        if n % b > 9:
          trocarChar(n % b)
        else:
          resultado.append(n % b) # adiciona o resto
        n = n//b # divisão inteira
        #print(n) # teste
        if n < b: # se n menor que a base
          if b == 16 and n > 9:
            trocarChar(n)
          else:
            resultado.append(n) # adicione
          resultado.reverse() # inverter para leitura correta
    return resultado

# Conversão decimal

def decimal(n,b):
    contador = 0
    while n != 0: # Enquanto não for 0 faça

        """
        Ex.:
        b = 8
        n = 0.625
        n = n*8 = 5.0
        adicionar 5 ao resultado
        separa 0.0
        fim
        """

        n = n*b # Multiplicar n por b Ex.: 0.625 * 5 =
        n = list(str(n)) # Transformar n em lista de caracteres
        resultado.append(''.join(digito for digito in n[:n.index('.')])) # Adicionar digito antes da virgula Ex.: 5
        n= n[n.index('.'):] # Separar a parte inteira Ex.: ['.','0']
        n = float(''.join(digito for digito in n))  # Unir de lista de string em único string para float Ex.: ['.','0'] -> 0.0

        if (n % b): # Se d seja divisível por b então faça
                contador += 1 # Adicione 1 ao contador
                if contador == 10:
                    return resultado

    return resultado

def trocarChar(n):
  if n == 10:
    resultado.append('A')
  if n == 11:
    resultado.append('B')
  if n == 12:
    resultado.append('C')
  if n == 13:
    resultado.append('D')
  if n == 14:
    resultado.append('E')
  if n == 15:
    resultado.append('F')


def imprimirMsg():

  mensagem = f"""
  1. Conversão decimal para binário
  2. Conversão decimal para octal
  3. Conversão decimal para hexadecimal
  4. Fim
  """
  print(mensagem)

# Imprimir resultado

def imprimirConv(resultado,sinal,base):

    if base == 2:
      print("Base Binária (", end="")
    if base == 8:
      print("Base Octal (", end="")
    if base == 16:
      print("Base Hexadecimal (", end="")

    if sinal == True:
        print("-", end="")

    print(''.join(str(digito) for digito in resultado), end="")
    #for digito in resultado:    # Para cada digito em resultado imprimir
        #print(digito, end="")
    print(")",end="")
    print(base)

# Menu de opções
def menu():

    # Limpar o resultado
    # resultado = [] # declarar lista vazia (não funciona?)
    # resultado.clear() # método clear()
    resultado[:] = [] # operador slicing

    opcao = input()

    if opcao == '1':
        convert_dec(2)
    if opcao == '2':
        convert_dec(8)
    if opcao == '3':
        convert_dec(16)
    if opcao == '4':
        print("Fim")
    else:
        menu()

# Converter base decimal para outras bases
def convert_dec(base):

    sinal = False # Sinal Posivito = False
    print("Digite um número a ser convertido:", end=" ")
    # Entrada do número
    numero = list(input()) # Transformar entrada em lista

    # Checar se é um número quebrado
    if '.' in numero: # numero real

        i = int(''.join(digito for digito in numero[:numero.index('.')])) # Unir parte inteira em int
        d = float(''.join(digito for digito in numero[numero.index('.'):])) # Unir parte decimal em float
        numero = float(''.join(digito for digito in numero)) # Unir número em float

    else:  # Número inteiro
        i = int(''.join(digito for digito in numero))
        d = 0 # Sem casa decimal
        numero = float(i)

    if numero >= 0:
        resultado = inteira(i,base)
        if d != 0:
                resultado.append(".")
                resultado = decimal(d,base)

    else:
          i = i*-1
          sinal = True # Sinal Negativo = True
          resultado = inteira(i,base)
          if d != 0:
                resultado.append(".")
                resultado = decimal(d,base)

    imprimirConv(resultado,sinal,base)
    imprimirMsg()


resultado = [] # Declarar lista vazia do resultado
imprimirMsg() # Imprimir a mensagem
menu()


# In[ ]:




