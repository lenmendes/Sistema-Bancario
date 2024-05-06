message = "Hello world!"
print(message)

#######################################
#Tipos de Dados
print (1 + 10) #int # int()
print (1.5 + 1 + 0.5) #float # float()
print(True) #boolean # bool()
print(False) #boolean 
print("Python") #string #str()

#######################################
#variaveis e constantes 

#variavel 
age = 23
name = 'Guilherme'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age, name = (28,'Guilherme') #pode ser escrito assim 
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

#constante - Letras em capslock
nome = 'Guilherme'
idade = 28 

nome, idade = ('Giovanna', 27)
nome, idade = 'Giovanna', 27 # o () pode ser opcional 
print(nome, idade)

#exemplos

limite_saque_diario = 1000

BRAZILIAN_STATES = ['SP', 'RJ', 'SC', 'RS']

#######################################
#conversao de tipos 

#inteiro para float 
preco = 10 
print (preco)

preco = float(preco)
print(preco)

preco = 10 / 2
print(preco)

#float para inteiro 
preco = 10.30 
print(preco)

preco = int(preco)
print(preco)

#conersão por divisão 
preco = 10 
print(preco)

print(preco / 2)

print(preco // 2)

#numerico para string 
preco = 10.50
idade = 28

print(str(preco))
print(str(idade))

texto = f'idade {idade} preco {preco}'
print(texto)

#string para numero 
preco = '10.50'
idade = '28'

print(float(preco))
print(int(idade))

#exemplos

print(int(1.984982))
print(int('10'))
print(float('10.10'))
print(float('100'))

valor = 10 
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100 / 2)
print(100 // 2)

#######################################
#funções de entrada e saida 

#input 

## nome = input('Informe o seu nome: ')

#print 

nome = 'Guilherme'
sobrenome = 'Carvalho'

print(nome, sobrenome)
print(nome, sobrenome, end='...\n') #\n quebra de linha
print(nome, sobrenome, sep='#') #sep estapço vazio, mas pode botar algo 

#exemplo

nome = input('Informe o seu nome: ')
idade = input('Informe a sua idade: ')
print(nome, idade, end='...\n')
print(nome, idade, sep='#', end='...\n')
print(nome, idade, sep='#')
#########################################
# tipos de operadores 

#operadores aritiméticos
# adição 
print(1 + 1)

# subtração 
print(10 - 2)

# multiplicação 
print(4 * 3)

# divisão 
print(12 / 3)

#divisao inteira
print(12 // 2)

# módulo
print(10 % 3)

# exponenciação 
print(2 ** 3)

print(10 - 5 * 2)
print((10 - 5) * 2)
print(10 ** 2 * 2)
print(10 ** (2 * 2))
print(10 / 2 * 4)

# exemplos 

produto_1 = 10
produto_2 = 20

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = 10 + 5 * 4
print(x)

y = (10 + 5) * 4
print(y)

z = 10 / 2 + 25 * 2 - 2 ** 2
print(z)

w = (10 / 2) + (25 * 2) - (2 ** 2)
print(w)


#operadores de comparação 
#igualdade

saldo = 450
saque = 200

print (saldo == saque)

#diferença

saldo = 450
saque = 200

print(saldo != saque)

#maior que/ maior ou igual

saldo = 450
saque = 200

print(saldo > saque)

saldo = 450
saque = 200

print(saldo >= saque)

#menor que/ menor ou igual 

saldo = 450
saque = 200

print(saldo < saque)

saldo = 450
saque = 200

print(saldo <= saque)

#exemplo 

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)


#operadores de atribuição 
#atribuição simples

saldo = 500 #o sinal de = 
print(saldo)

#atribuição com adição 
saldo = 500
saldo +=200 
print(saldo)

#atribuição com subtração
saldo = 500
saldo -=100 
print(saldo)

#atribuição com multiplicação
saldo = 500
saldo *= 2
print(saldo)

#atribuição com divisão
saldo = 500
saldo /= 5
print(saldo)

saldo = 500
saldo //= 5
print(saldo)

#atribuição com modulo
saldo = 500
saldo %= 480
print(saldo)

#atribuição com exponenciação
saldo = 80
saldo **= 2
print(saldo)


#operadores logicos 
saldo = 1000
saque = 200
limite = 100

saldo >= saque 
saque <= limite 

#operador E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite

#operador OU
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite      

#operador de negação 
contatos_emergencia = []

not 1000 > 1500
not contatos_emergencia #lista vazia em pyhton é considerado false
not "saque 1500;"
not "" #string vazia em pyhton é considerado false

#   A diferença está nas condições de verdadeiro AND (E) retorna verdadeiro se as duas entradas forem verdadeiras, 
#   OR(OU) retorna verdadeiro se pelo menos uma das entradas for verdadeira (uma OU outra), 
#   NOT (NÃO) simplesmente inverte o resultado, ou seja, se a entrada for verdadeira ela retorna falsa e vice-versa.
#   
#   true AND true = true 
#   true AND false = false 
#   false AND false = false 
#   true OR true = true 
#   true OR false = true 
#   false OR false = false


#parênteses 

saldo = 1000
saque = 250 
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

#operadores de identidade 
curso = 'Curso de Pyhton'
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
curso is not nome_curso
curso is limite 

#operadores de associação
curso = "Curso de Python"
frutas = ["laranja", "uva", "limao"]
saques = [1500, 100]

"Pyhton" in curso 
"maçã" not in frutas 
200 in saques 

#########################################
#estruturas condicionais e de repetição 

#bloco em python 

def sacar(valor): # inicio do bloco do metodo
    saldo = 500
    if saldo >= valor: #inicio do bloco if
        print("valor sacado")
        print("retire o seu dinheiro na boca do caixa.")
        # fim do bloco if
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
# fim do bloco de metodo

def depositar(valor):
    saldo = 500
    saldo += valor


sacar (100)


#estruturas adicionais 

#if 

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")

if saldo < saque:
    print("Saldo insuficiente!")

#if/else

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque!")
else:
    print("Saldo insuficiente!")


#if/elif/else

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opção inválida")


#exemplos 

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar tirar a CHN')

if idade < MAIOR_IDADE:
    print('ainda nao pode tirar o CNH.')
#ou 
if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar tirar a CHN')
else:
    print('ainda nao pode tirar a CNH')


if idade >= MAIOR_IDADE:
    print('Maior de idade, pode tirar tirar a CHN')
elif idade == IDADE_ESPECIAL:
    print('pode fazer aulas teóricas, mas nao pode fazer aulas prátivas.')
else:
    print('ainda nao pode tirar a CNH')

#if aninhado 
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450 

if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('saque realizado com uso de cheque especial!')
    else:
        print('nao foi possivel realizar o saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    else:
        print('saldo insuficiente!')


#estruturas de repetição 7

#receba um numero do teclado e exiba os 2 numeros seguintes

a = int(input('informe um numero inteiro: '))
print(a)

a += 1
print(a)

a += 1
print(a) #jeito sujo de fazer repetição 


#for - usa quando sabemos o numero exato de repetições 
texto = input('informe um texto:')
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

print() #add uma quebra de linha

#for/else
texto =  ''
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

else:
    print() #add uma quebra de linha
    print("executa no final do laço")

#range
#range(stop) -> range object 
#range(start, stop[, step]) -> range object

list(range(4))

#range com for

for numero in range (0, 11):
    print(numero, end='')

#exibindo a tabuada do 5
for numero in range(0, 51, 5): #inicio, fim e step 
    print(numero, end='')

#while - quando nao sabemos o numero exato de quantas vezes deve ser executado 

opcao = -1 

while opcao != 0:
    opcao = int(input('[1] sacar \n[2] extrato \n[3] sair \n'))

if opcao == 1:
    print('sacando...')
elif opcao == 2:
    print('exibindo o extrato...')


while True:
    numero = int(input('informe um numero'))

    if numero == 10:
        break

print(numero)

while True:
    numero = int(input('informe um numero'))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue


print(numero)

########################### dominando strings e fatiamento
#conhecendo metodos uteis da classe string 
#Strings 

#maiúscula, menúscula e título 

curso = 'pYtHon'

print(curso.upper()) #PYTHON

print(curso.lower()) #python 

print(curso.title()) #Python 

#eliminando espaços em branco 

curso = '   Python'

print(curso.strip()) #'Python'

print(curso.lstrip()) #'Python  '

print(curso.rstrip()) #'   Python'

#junções e centralização 

curso = 'Python'

print(curso.center(10, '#'))  ###Python##'

print('.'.join(curso))  #'P.y.t.h.o.n'

#exemplos 

nome = 'gUIlherME'

print(nome.upper())
print(nome.lower())
print(nome.tittle())


texto = '  olá mundo!   '

print(texto + '.')
print(texto.strip() + '.')
print(texto.rstrip() + '.')
print(texto.lstrip() + '.')

menu = 'Python'

print('####Python####')
print(menu.center(14))
print(menu.center(14, '#'))
print('P-y-t-h-o-n')
print('-'.join(menu))

# fatiamento de string

#old style %

nome = 'guilherme'
idade = 28
profissao =  'programador'
linguagem = 'python'

print('olá, me chamo $s. Eu tenho $d anos de idade, trabalho como %s e estou matriculado no curso de %s. ' % (nome, idade, profissao, linguagem))
#olá, me chamo guilerme. Eu tenho 28 anos de idade, trabalho como programador e estou matriculado no curso de python.

# $s - string /  %d - numeros inteiros / %f - valores de pontos flutuantes

#metodo format 

nome = 'guilherme'
idade = 28
profissao =  'programador'
linguagem = 'python'

print('olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}. '.format (nome, idade, profissao, linguagem))

print('olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}. '.format (linguagem, profissao, idade, nome))

print('olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. '.format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

nome = 'guilherme'
idade = 28
profissao =  'programador'
linguagem = 'python'

dados = {'nome': nome, 'idade': idade, 'profissao': profissao, 'linguagem': linguagem}

print('olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. '.format(**dados))

#f-string 

nome = 'guilherme'
idade = 28
profissao =  'programador'
linguagem = 'python'

print(f'olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}. ')

#formatar strings com f=string 

PI = 3.14159

print(f'valor de PI: {PI:.2f}') #valor de PI: 3.14

print(f'valor de PI: {PI:10.2f}') #valor de PI:           3.14


#fatiamento 

nome = 'guilherme arthur de carvalho'

nome[0] 
print(nome[0]) # 'g'

nome[:9] 
print(nome[:9]) # 'guilherme'

nome[10:] 
print(nome[10:]) # 'arthur de carvalho'

nome[10:16] 
print(nome[10:16]) # 'arthur'

nome[10:16:2] 
print(nome[10:16:2]) # 'atu'

nome[:]
print(nome[:])  # 'guilherme arthur de carvalho'

nome[::-1] 
print(nome[::-1]) # 'gohlavrac ed ruhtra emrehliug'

#strings triplas 

nome ='guilherme'

mensagem = f'''
olá meu nome é {nome},
eu estou aprendendo python
'''
print(mensagem)
# olá meu nome é guilherme,
# eu estou aprendendo python 

nome ='guilherme'

mensagem = f'''
    olá meu nome é {nome},
eu estou aprendendo python
        essa mensagem tem diferentes recuos.
'''

print(mensagem)
#   olá meu nome é guilherme,
# eu estou aprendendo python
#        essa mensagem tem diferentes recuos.

print('''
      ===== MENU ====
      
      1 - DEPOSITAR
      2- SACAR
      0 - SAIR
      ===============

            OBRIGADO POR USAR NOSSO SISTEMA!!!!
''')

'''     ===== MENU ====
      
      1 - DEPOSITAR
      2 - SACAR
      0 - SAIR
      ===============

            OBRIGADO POR USAR NOSSO SISTEMA!!!!
'''

