#!/usr/bin/env python
# coding: utf-8

# # Python do Zero I
# 
# <small>Material para o Live Coding 1, 26/01/2022, referente à [semana 12 do curso](https://ericbrasiln.github.io/intro-historia-digital/mod4b/sem12.html#)</small>
# 
# O objetivo desse encontro virtual é tirar dúvidas quanto à instalação do Python e do Visual Studio Code e apresentar alguns conceitos básicos de programação.

# 
# 
# ![python](https://cdn.pixabay.com/photo/2017/01/31/23/21/animal-2028134_960_720.png)
# 
# ---
# 
# **OBS:**
# 
# Trechos e exemplos foram retirados dos seguintes  materiais:
# 
# * [Introductions to cultural analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/index.html) de [Melanie Walsh](https://melaniewalsh.org/);
# * [Python Basics 1-3](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-1.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless;
# * [Pense Python 2ª edição](https://penseallen.github.io/PensePython2e/) de Allen Downey.

# ## Pq Python?
# 
# [Python](https://docs.constellate.org/key-terms/#python) é uma das linguagens de programação que mais crescem no mundo. Aprender Python] é uma ótima escolha pois é uma linguagem:
# 
# * amplamente adotada nas humanidades digitais e ciência de dados;
# * que tem uma curva de aprendizado menor do que outras linguagens; 
# * flexível, possuíndo amplo suporte para lidar com dados numéricos e textuais;
# * que lembra o inglês e é legível para quem sabe esse idioma.

# ## Anatomia de um script Python
# Adaptado do curso [Introduction to Cultural Analytics & Python](https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/03-Anatomy-Python-Script.html) de Melanie Walsh.
# 
# Geralmente, o código escrito em Python para executar alguma função, salvo em um arquivo com a extensão *.py*, chamdo **script** possui uma estrutura que segue certo padrão. Ou melhor, possui um conjunto de elementos básicos e lógicos.
# 
# Vamos olhar o script abaixo e entender cada trecho.
# 

# In[1]:


'''
Esse script pretende ser um exemplo de como se
estrutura um script Python.
'''

# Importando bilbiotecas
import time

# cria variável com o dia e hora atual
now = time.strftime("%d/%m/%Y %H:%M:%S")

#print() é uma função para imprimir um valor na tela
print(now)

# input() é uma função para receber um valor digitado pelo usuário  
name = input("Digite seu nome: ")

print('\nOlá, ' + name + '!')
# fim do script


# ## Terminal 
# 
# Além de poder executar comandos de Python no Jupyter Notebook, podemos e comumente vamos executar comandos e scripts diretamente através de linhas de comando no terminal.
# 
# ```
# python3 <nome-do-script>.py
# 
# ``` 
# 
# Ou ainda, você pode acessar o python em seu terminal e executar comandos de forma interativa:
# 
# ![terminal1.png](data:image/png;base64,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)
# 

# ## Operadores Aritméticos
# 
# [Python Basics 1](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-1.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# |Operador| Operação| Exemplo | Resultado |
# |---|----|---|---|
# |\*\*| Potência| 3 ** 3 | 27 |
# |%| Resto da divição| 34 % 6 | 4 |
# |/| Divisão | 30 / 6 | 5|
# |//| Divisão inteira | 27 // 6 | 4 |
# |\*| Multiplicação | 7 * 8 | 56 |
# |-| Subtração | 18 - 4| 14|
# |+| Adição | 4 + 3 | 7 |

# ## Operadores relacionais
# 
# [Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# |Operador|Significado|
# |---|---|
# |==|Igual|
# |!=|diferente|
# |<|Menor que|
# |>|Maior que|
# |<=|Menor ou igual que|
# |>=|Maior ou igual que|

# ## Operadores Booleanos (and/or/not)
# 
# [Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# ### and
# 
# ```True and True = True```

# ### or
# 
# |Expressão|Avaliação|
# |---|---|
# |True or True|True|
# |True or False|True|
# |False or True|True|
# |False or False|False|
# 

# ## Variáveis
# Traduzido de [Variables](https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/04-Variables.html) Melanie Walsh.
# 
# As variáveis são um dos blocos de construção fundamentais do Python. Uma variável é como um pequeno contêiner onde você armazena valores e dados, como nomes de arquivos, palavras, números, coleções de palavras e números e muito mais.

# ### Definindo variáveis
# 
# O nome da variável apontará para um valor que você "atribui" a ele. Você pode pensar em atribuição de variável como colocar um valor "dentro" da variável, como se a variável fosse uma pequena caixa 🎁
# 
# Você atribui variáveis com um sinal de igual `=`. Em Python, um único sinal de igual `=` é o "operador de atribuição". Um sinal de igual duplo `==` é o sinal de igual "real".

# In[2]:


# criar uma variável
nome = 'Maria'
#imprimir o valor da variável
print(nome)


# In[3]:


2+2 == 4


# ### Nomeando variáveis
# 
# Os nomes das variáveis podem ser tão longos ou curtos quanto você quiser e podem incluir:
# - letras maiúsculas e minísculas (A-Z)
# - dígitos (0-9)
# - underscores (_)
# 
# No entanto, os nomes das variáveis * não podem * incluir:
# - ❌ outras pontuações (-.!?@)
# - ❌ spaces ( )
# - ❌ uma palavra reservada do Python
# 
# Variáveis claras e nomeadas com precisão irão:
# 
# * tornar seu código mais legível (para você e para outras pessoas)
# * reforçar sua compreensão do Python e do que está acontecendo no código
# * esclarecer e fortalecer seu pensamento
# 
# Para maiores informações veja o [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

# ### Palavras-chave do Python
# Retirado de [Pense Python](https://penseallen.github.io/PensePython2e/02-vars-expr-instr.html) de Allen Downey, capítulo 2.
# 
# O interpretador usa palavras-chave para reconhecer a estrutura do programa e elas não podem ser usadas como nomes de variável.
# 
# O Python 3 tem estas palavras-chave:
# 
# ```
# and         del         from        None        True
# as          elif        global      nonlocal    try
# assert      else        if          not         while
# break       except      import      or          with
# class       False       in          pass        yield
# continue    finally     is          raise
# def         for         lambda      return
# ```
# 
# Você não precisa memorizar essa lista. Na maior parte dos ambientes de desenvolvimento, as palavras-chave são exibidas em uma cor diferente; se você tentar usar uma como nome de variável, vai perceber.

# ### Redefinindo variáveis
# 
# As variáveis não são fixas, é possível atribuir novos valores a uma varivável que já havia sido definida anteriormente.

# In[4]:


nome = 'Eric'
print(nome)


# ## Tipos de Dados
# 

# Existem quatro tipos essenciais de dados Python com diferentes poderes e capacidades:
# 
# - Strings (texto)
# - Inteiros (números inteiros)
# - Floats (números decimais)
# - Booleans (verdadeiro / falso)

# 
# |Tipo | Explicação | Exemplo |
# |---|---|---|
# |integer|número inteiro| -3, 0, 2, 534|
# |float|número decimal | 6.3, -19.23, 5.0, 0.01|
# |string|texto| 'Hello world', '1700 butterflies', '', '1823'|
# |boolean|Verdadeiro ou Falso| True/False|
# 

# Você pode verificar o tipo de dados de qualquer valor usando a função `type ()`.

# In[5]:


type(nome)


# ### print() input() e format()
# 
# Para imprimir na tela um valor devemos utilizar a função `print()`.
# 
# Para receber um valor de entrada do usuário, usamos a função `input()`.
# 
# Usamos format() para formatar strings.

# In[6]:


print(nome)

new_name = input('Digite seu nome: ')
print(new_name)

print(f'Olá, {new_name}! Como vai?')


# ### Strings

# Uma *string* é um tipo de dados Python que é tratado como texto, mesmo que contenha um número. As strings são sempre colocadas entre aspas simples `'isto é uma string'` ou aspas duplas `"isto é uma string"`.
# 
# Segundo [Allen Downey](https://penseallen.github.io/PensePython2e/08-strings.html):
# 
# >Strings não são como números inteiros, de ponto flutuante ou booleanos. Uma string é uma sequência, ou seja, uma coleção ordenada de outros valores. (...) Uma string é uma sequência de caracteres.

# É possível acessar um caracter específico da string com o operador []
# 
# A expressão entre colchetes chama-se índice. O índice aponta qual caractere da sequência você quer
# 
# ---

# **Vamos usar um exemplo que preste**
# 
# <img src="https://www.beyonce.com/uploads/2021/09/090821_valentinojeans_02_ekpqrul_gen.gif" alt="queen bey" width="200">

# In[7]:


music = 'Formation'
music[1]


# **Opa! o caractere na posição 1 da string music não deveria ser 'U'?**
# 
# A contagem de índices no Python começa em `0`, ou seja, o primeiro caractere é na posição 0.
# 
# A indexação é baseada na distância do ponto de partida e como o primeiro elemento está a uma distância *zero* do ponto de partida, seu índice é `0`.

# In[8]:


music[0]


# E pra acessar o último elemento da string, você pode usar índices negativos.

# In[9]:


music[-1]


# #### len()
# 
# len() é uma função que retorna o número de caracteres de uma string.

# In[10]:


len(music)


# In[11]:


another_music = 'Mood 4 eva'
len(another_music)


# #### Manipulando *strings*

# ##### Fatiamento de strings
# 
# Segundo [Allen Downey](https://penseallen.github.io/PensePython2e/08-strings.html):
# 
# >O operador [n:m] retorna a parte da string do “enésimo” caractere ao “emésimo” caractere, incluindo o primeiro, mas excluindo o último. Este comportamento é contraintuitivo, porém pode ajudar a imaginar os índices que indicam a parte entre os caracteres.

# In[12]:


old_music = 'Crazy in love'


# In[13]:


old_music[2:5]


# In[14]:


old_music[:5] # se omitir o primeiro número, ele começa no início da string


# In[15]:


old_music[3:] # se omitir o último número, a fatia vai até o final da string


# In[16]:


old_music[3:3] # Se o primeiro índice for maior ou igual ao segundo, o resultado é uma string vazia, representada por duas aspas


# ##### Concatenando strings

# In[17]:


nome = 'Beyoncé'
nome_completo = nome + ' ' + 'Knowles'
print(nome_completo)


# ##### Métodos de strings

# In[18]:


# lower() converte todas as letras para minusculas
nome_completo = nome_completo.lower()
print(nome_completo)


# In[19]:


# upper() converte todas as letras para maiusculas
nome_completo = nome_completo.upper()
print(nome_completo)


# In[20]:


# replace - substitui uma string por outra
nome_completo = nome_completo.replace('KNOWLES', 'KNOWLES-CARTER')
print(nome_completo)


# In[21]:


# split - divide uma string em várias strings
f_name, l_name = nome_completo.split(' ')
print(f_name)
print(l_name)


# In[22]:


# find - encontra a posição de uma string dentro de outra
nome_completo.find('KNOWLES')


# In[23]:


# rfind - encontra a posição de uma string dentro de outra, mas começa a busca pelo final
nome_completo.rfind('K')


# In[24]:


# count - conta quantas vezes uma string aparece dentro de outra
nome_completo.count('E')


# In[25]:


# strip - remove os espaços em branco no início e no final da string
movie = ' Lion King             '
movie.strip()


# #### Saiba mais sobre strings
# 
# [ABZ-Aaron](https://github.com/ABZ-Aaron) criou um repositório no Github com cheat sheets para os métdoso de strings. Lś você também encontra cheat sheets sobre listas e dicionários. 
# 
# Veja o [repositório](https://github.com/ABZ-Aaron/CheatSheets).

# ## Listas

# Allen Downey define uma lista em Python:
# 
# >Como uma string, uma lista é uma sequência de valores. Em uma string, os valores são caracteres; em uma lista, eles podem ser de qualquer tipo. Os valores em uma lista são chamados de elementos, ou, algumas vezes, de itens.
# 
# >Há várias formas para criar uma lista; a mais simples é colocar os elementos entre colchetes ([ e ])

# Listas são mutáveis. Podem conter elementos de qualquer tipo.

# In[26]:


musics = ['Lemonade', 'Halo', 'Freedom','Flawless']
years = [2000, 2019, 2016, 2013]
empty = []
multi = ['singer', 1.70, ['jay-z', 'blue ivy']]


# In[27]:


years[1] = 2016
years


# In[28]:


len(musics)


# Índices de listas funcionam da mesma forma que os índices de strings

# ### Métodos de listas

# In[29]:


# append - adiciona um elemento ao final de uma lista
musics.append('Formation')


# In[30]:


# extend toma uma lista como argumento e adiciona todos os elementos
new_songs = ['Crazy in love', 'Hold up']
musics.extend(new_songs)
print(musics)


# In[31]:


# sort - ordena uma lista
musics.sort()


# In[32]:


musics.sort(reverse=True)


# In[33]:


musics.append('Artpop')
print(musics)


# In[34]:


#pop - remove um elemento da lista
musics.pop() # remove o ultimo elemento da lista
print(musics)


# In[35]:


# del - remove um elemento da lista
del musics[0]


# In[36]:


# remove - remove um elemento da lista
musics.remove('Halo')
print(musics)


# In[37]:


# transformar uma lista em uma string
# join - separa os elementos da lista com o separador passado
str_musics = ', '.join(musics)
print(str_musics)


# ## Controle de fluxo
# 
# [Python Basics 2](https://hub.binder.constellate.org/user/ithaka-tdm-notebooks-mb3z11hb/notebooks/python-basics-2.ipynb) de [Nathan Kelber](http://nkelber.com/) e Ted Lawless

# ### Tipos de controle de fluxo
# 
# 
# |Declaração|Significado|Condição de execução|
# |---|---|---|
# |`if`|se|se a condição for atendida|
# |`elif`|senão se|se nenhuma condição anterior for atendida *e* esta condição for atendida|
# |`else`|senão|se nenhuma condição for atendida (nenhuma condição é fornecida para uma instrução `else`)|
# |`while`|enquanto|enquanto a condição for verdadeira|
# |`for`|para|executar em um loop um quantidade de vezes|
# |`try`|tentar|tente isso e execute o código `except` se ocorrer um erro|

# ### Criando iterações for
# 
# É fundamental entender a estrutura de iteração, realizar um loop com python.
# 
# Iterar é a capacidade de executar um bloco de instruções repetidamente.

# In[38]:


# utilizar for para percorrer a lista musics
for music in musics:
    length_music = len(music)
    print(f'A música é {music} e ela possui {length_music} letras.\n')


# In[39]:


# utilizar range para percorrer um intervalo de valores
for i in range(0, len(musics)):
    print(f'A música é {musics[i]} e ela possui {len(musics[i])} letras.\n')
    


# In[40]:


# create a list
list_names = []
# input the names of the students
for i in range(1,6):
    name = input(f'Digite o nome do estudante número {i}: ')
    list_names.append(name)
    


# In[41]:


# loop na lista musics e salva cada item em um arquivo txt
for music in musics:
    # abre o arquivo txt
    file = open(music + '.txt', 'w') # w = write
    # escreve o valor usando format
    file.write(str(f'A música é {music} e ela possui {len(music)} letras.\n'))
    file.close() # fecha o arquivo


# ### while
# 
# Fluxo de execução para uma instrução while:
# 
# 1. Determine se a condição é verdadeira ou falsa.
# 
# 1. Se for falsa, saia da instrução while e continue a execução da próxima instrução.
# 
# 1. Se a condição for verdadeira, execute o corpo e então volte ao passo 1.

# In[42]:


# criar uma lista de uma contagem de 10 até 0
import time
count = 10
while count > 0:
    print(count)
    time.sleep(1)
    count -= 1
print("Ok, Ladies, now let's get in formation!")


# ### if / elif / else
# 
# Operações condicionais

# In[43]:


number = int(input('Digite um número: '))


# In[44]:


if number > 0:
    print('positive')


# In[45]:


if number < 0:
    print('negative')


# In[46]:


if number == 0:
    print('zero')


# In[47]:


if number > 0:
    print(f'o número {number} positivo')
else:
    print(f'o número {number} negativo')


# In[48]:


if number > 0:
    print(f'o número {number} positivo')
elif number == 0:
    print(f'o número {number} é zero')
else:
    print(f'o número {number} negativo')


# ---