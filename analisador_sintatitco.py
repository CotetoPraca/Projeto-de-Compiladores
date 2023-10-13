# Analisador sintático da gramática Algox

# Função auxiliar para traduzir os tokens em ID
def traduzirLinha(token):
  id = -1  # Inicializa o ID como inválido

  for entrada, valor in tabelaTraducao.items():
    if len(token) != len(entrada):
      continue  # Se os comprimentos forem diferentes, as strings não podem ser iguais

    igual = True  # Supomos que as strings são iguais até que um caractere diferente seja encontrado
    for i in range(len(entrada)):
      if token[i] != entrada[i]:
        igual = False
        break  # Encontramos um caractere diferente, saímos do loop interno
    if igual:
      id = valor
      break

  return id

# Tratativa de erro: remove valor do topo da pilha
def erro_sai(pilha):
  print(f"ERRO: removendo {pilha.pop()} da pilha")

# Tratativa de erro: remove a entrada atual
def erro_varre(entrada):
  print(f"ERRO: removendo {entrada.pop(0)} da entrada")

# Empilha a regra equivalente ao não-terminal <algoritmo>
def regra_algoritmo(pilha, opcao):
  if (opcao == 1): # <algoritmo> → <comando> <algoritmo_aux>
    pilha.append(tabelaTraducao.get('<algoritmo_aux>'))
    pilha.append(tabelaTraducao.get('<comando>'))

# Empilha a regra equivalente ao não-terminal <algoritmo_aux>
def regra_algoritmo_aux(pilha, opcao):
  if (opcao == 1): # <algoritmo_aux> → <comando> <algoritmo_aux>
    pilha.append(tabelaTraducao.get('<algoritmo_aux>'))
    pilha.append(tabelaTraducao.get('<comando>'))
  elif (opcao == 2): # <algoritmo_aux> → ε
    pass

# Empilha a regra equivalente ao não-terminal <algox>
def regra_algox(pilha, opcao):
  if (opcao == 1): # <algox> → PROGRAMA <nome_do_programa> INICIO <corpo_do_programa> FIM
    pilha.append(tabelaTraducao.get('FIM'))
    pilha.append(tabelaTraducao.get('<corpo_do_programa>'))
    pilha.append(tabelaTraducao.get('INICIO'))
    pilha.append(tabelaTraducao.get('<nome_do_programa>'))
    pilha.append(tabelaTraducao.get('PROGRAMA'))

# Empilha a regra equivalente ao não-terminal <comando>
def regra_comando(pilha, opcao):
  if (opcao == 1): # <comando> → <comando_atribuicao> <comando_aux>
    pilha.append(tabelaTraducao.get('<comando_aux>'))
    pilha.append(tabelaTraducao.get('<comando_atribuicao>'))
  elif (opcao == 2): # <comando> → <comando_entrada> <comando_aux>
    pilha.append(tabelaTraducao.get('<comando_aux>'))
    pilha.append(tabelaTraducao.get('<comando_entrada>'))
  elif (opcao == 3): # <comando> → <comando_repeticao> <comando_aux>
    pilha.append(tabelaTraducao.get('<comando_aux>'))
    pilha.append(tabelaTraducao.get('<comando_repeticao>'))
  elif (opcao == 4): # <comando> → <comando_saida> <comando_aux>
    pilha.append(tabelaTraducao.get('<comando_aux>'))
    pilha.append(tabelaTraducao.get('<comando_saida>'))
  elif (opcao == 5): # <comando> → <comando_selecao> <comando_aux>
    pilha.append(tabelaTraducao.get('<comando_aux>'))
    pilha.append(tabelaTraducao.get('<comando_selecao>'))

# Empilha a regra equivalente ao não-terminal <comando_aux>
def regra_comando_aux(pilha, opcao):
  if (opcao == 1): # <comando_aux> → <comando> <comando_aux>
    pilha.append(tabelaTraducao.get('<comando_aux>'))
    pilha.append(tabelaTraducao.get('<comando>'))
  elif (opcao == 2): # <comando_aux> → ε
    pass

# Empilha a regra equivalente ao não-terminal <comando_atribuicao>
def regra_comando_atribuicao(pilha, opcao):
  if (opcao == 1): # <comando_atribuicao> → <variavel> OPERADOR_ATRIBUICAO <expressao_aritmetica>
    pilha.append(tabelaTraducao.get('<expressao_aritmetica>'))
    pilha.append(tabelaTraducao.get('OPERADOR_ATRIBUICAO'))
    pilha.append(tabelaTraducao.get('<variavel>'))

# Empilha a regra equivalente ao não-terminal <comando_entrada>
def regra_comando_entrada(pilha, opcao):
  if (opcao == 1): # <comando_entrada> → LEIA <variavel> <comando_entrada_aux>
    pilha.append(tabelaTraducao.get('<comando_entrada_aux>'))
    pilha.append(tabelaTraducao.get('<variavel>'))
    pilha.append(tabelaTraducao.get('LEIA'))

# Empilha a regra equivalente ao não-terminal <comando_entrada_aux>
def regra_comando_entrada_aux(pilha, opcao):
  if (opcao == 1): # <comando_entrada_aux> → VIRGULA <variavel>
    pilha.append(tabelaTraducao.get('<variavel>'))
    pilha.append(tabelaTraducao.get('VIRGULA'))
  elif (opcao == 2): # <comando_entrada_aux> → ε
    pass

# Empilha a regra equivalente ao não-terminal <comando_repeticao>
def regra_comando_repeticao(pilha, opcao):
  if (opcao == 1): # <comando_repeticao> → ENQUANTO <expressao_relacional> <comando> FIM_ENQUANTO
    pilha.append(tabelaTraducao.get('FIM_ENQUANTO'))
    pilha.append(tabelaTraducao.get('<comando>'))
    pilha.append(tabelaTraducao.get('<expressao_relacional>'))
    pilha.append(tabelaTraducao.get('ENQUANTO'))

# Empilha a regra equivalente ao não-terminal <comando_saida>
def regra_comando_saida(pilha, opcao):
  if (opcao == 1): # <comando_saida> → ESCREVA <comando_saida_aux>
    pilha.append(tabelaTraducao.get('<comando_saida_aux>'))
    pilha.append(tabelaTraducao.get('ESCREVA'))

# Empilha a regra equivalente ao não-terminal <comando_saida_aux>
def regra_comando_saida_aux(pilha, opcao):
  if (opcao == 1): # <comando_saida_aux> → <variavel> <comando_saida_variavel_cadeia>
    pilha.append(tabelaTraducao.get('<comando_saida_variavel_cadeia>'))
    pilha.append(tabelaTraducao.get('<variavel>'))
  elif (opcao == 2): # <comando_saida_aux> → CADEIA <comando_saida_cadeia_variavel>
    pilha.append(tabelaTraducao.get('<comando_saida_cadeia_variavel>'))
    pilha.append(tabelaTraducao.get('CADEIA'))

# Empilha a regra equivalente ao não-terminal <comando_saida_cadeia_variavel>
def regra_comando_saida_cadeia_variavel(pilha, opcao):
  if (opcao == 1): # <comando_saida_cadeia_variavel> → VIRGULA <variavel>
    pilha.append(tabelaTraducao.get('<variavel>'))
    pilha.append(tabelaTraducao.get('VIRGULA'))
  elif (opcao == 2): # <comando_saida_cadeia_variavel> → ε
    pass

# Empilha a regra equivalente ao não-terminal <comando_saida_variavel_cadeia>
def regra_comando_saida_variavel_cadeia(pilha, opcao):
  if (opcao == 1): # <comando_saida_variavel_cadeia> → VIRGULA CADEIA
    pilha.append(tabelaTraducao.get('CADEIA'))
    pilha.append(tabelaTraducao.get('VIRGULA'))
  elif (opcao == 2): # <comando_saida_variavel_cadeia> → ε
    pass

# Empilha a regra equivalente ao não-terminal <comando_selecao>
def regra_comando_selecao(pilha, opcao):
  if (opcao == 1): # <comando_selecao> → SE <expressao_relacional> ENTAO <comando> FIM_SE
    pilha.append(tabelaTraducao.get('FIM_SE'))
    pilha.append(tabelaTraducao.get('<comando>'))
    pilha.append(tabelaTraducao.get('ENTAO'))
    pilha.append(tabelaTraducao.get('<expressao_relacional>'))
    pilha.append(tabelaTraducao.get('SE'))

# Empilha a regra equivalente ao não-terminal <constante>
def regra_constante(pilha, opcao):
  if (opcao == 1): # <constante> → CONSTANTE_INTEIRA
    pilha.append(tabelaTraducao.get('CONSTANTE_INTEIRA'))
  elif (opcao == 2): # <constante> → CONSTANTE_REAL
    pilha.append(tabelaTraducao.get('CONSTANTE_REAL'))

# Empilha a regra equivalente ao não-terminal <corpo_do_programa>
def regra_corpo_do_programa(pilha, opcao):
  if (opcao == 1): # <corpo_do_programa> → <declaracoes> <algoritmo>
    pilha.append(tabelaTraducao.get('<algoritmo>'))
    pilha.append(tabelaTraducao.get('<declaracoes>'))

# Empilha a regra equivalente ao não-terminal <declaracao>
def regra_declaracao(pilha, opcao):
  if (opcao == 1): # <declaracao> → <tipo> <variavel> <declaracao_aux>
    pilha.append(tabelaTraducao.get('<declaracao_aux>'))
    pilha.append(tabelaTraducao.get('<variavel>'))
    pilha.append(tabelaTraducao.get('<tipo>'))

# Empilha a regra equivalente ao não-terminal <declaracao_aux>
def regra_declaracao_aux(pilha, opcao):
  if (opcao == 1): # <declaracao_aux> → VIRGULA <variavel> <declaracao_aux>
    pilha.append(tabelaTraducao.get('<declaracao_aux>'))
    pilha.append(tabelaTraducao.get('<variavel>'))
    pilha.append(tabelaTraducao.get('VIRGULA'))
  elif (opcao == 2): # <declaracao_aux> → ε
    pass

# Empilha a regra equivalente ao não-terminal <declaracoes>
def regra_declaracoes(pilha, opcao):
  if (opcao == 1): # <declaracoes> → <declaracao> <declaracoes_aux>
    pilha.append(tabelaTraducao.get('<declaracoes_aux>'))
    pilha.append(tabelaTraducao.get('<declaracao>'))

# Empilha a regra equivalente ao não-terminal <declaracoes_aux>
def regra_declaracoes_aux(pilha, opcao):
  if (opcao == 1): # <declaracoes> → <declaracao> <declaracoes_aux>
    pilha.append(tabelaTraducao.get('<declaracoes_aux>'))
    pilha.append(tabelaTraducao.get('<declaracao>'))
  elif (opcao == 2): # <declaracoes> → ε
    pass

# Empilha a regra equivalente ao não-terminal <expressao_aritmetica>
def regra_expressao_aritmetica(pilha, opcao):
  if (opcao == 1): # <expressao_aritmetica> → <constante> <expressao_aritmetica_aux>
    pilha.append(tabelaTraducao.get('<expressao_aritmetica_aux>'))
    pilha.append(tabelaTraducao.get('<constante>'))
  elif (opcao == 2): # <expressao_aritmetica> → <variavel> <expressao_aritmetica_aux>
    pilha.append(tabelaTraducao.get('<expressao_aritmetica_aux>'))
    pilha.append(tabelaTraducao.get('<variavel>'))
  elif (opcao == 3): # <expressao_aritmetica> → ABRE <expressao_aritmetica> FECHA <expressao_aritmetica_aux>
    pilha.append(tabelaTraducao.get('<expressao_aritmetica_aux>'))
    pilha.append(tabelaTraducao.get('FECHA'))
    pilha.append(tabelaTraducao.get('<expressao_aritmetica>'))
    pilha.append(tabelaTraducao.get('ABRE'))

# Empilha a regra equivalente ao não-terminal <expressao_aritmetica_aux>
def regra_expressao_aritmetica_aux(pilha, opcao):
  if (opcao == 1): # <expressao_aritmetica_aux> → <operador_aritmetico> <expressao_aritmetica>
    pilha.append(tabelaTraducao.get('<expressao_aritmetica>'))
    pilha.append(tabelaTraducao.get('<operador_aritmetico>'))
  elif (opcao == 2): # <expressao_aritmetica_aux> → ε
    pass

# Empilha a regra equivalente ao não-terminal <expressao_logica>
def regra_expressao_logica(pilha, opcao):
  if (opcao == 1): # <expressao_logica> → <expressao_relacional> <expressao_logica_aux>
    pilha.append(tabelaTraducao.get('<expressao_logica_aux>'))
    pilha.append(tabelaTraducao.get('<expressao_relacional>'))
  elif (opcao == 2): # <expressao_logica> → OPERADOR_NOT ABRE <expressao_logica> FECHA <expressao_logica_aux>
    pilha.append(tabelaTraducao.get('<expressao_logica_aux>'))
    pilha.append(tabelaTraducao.get('FECHA'))
    pilha.append(tabelaTraducao.get('<expressao_logica>'))
    pilha.append(tabelaTraducao.get('ABRE'))
    pilha.append(tabelaTraducao.get('OPERADOR_NOT'))
  elif (opcao == 3): # <expressao_logica> → ABRE <expressao_logica> FECHA <expressao_logica_aux>
    pilha.append(tabelaTraducao.get('<expressao_logica_aux>'))
    pilha.append(tabelaTraducao.get('FECHA'))
    pilha.append(tabelaTraducao.get('<expressao_logica>'))
    pilha.append(tabelaTraducao.get('ABRE'))

# Empilha a regra equivalente ao não-terminal <expressao_logica_aux>
def regra_expressao_logica_aux(pilha, opcao):
  if (opcao == 1): # <expressao_logica_aux> → <operador_logico> <expressao_logica>
    pilha.append(tabelaTraducao.get('<expressao_logica>'))
    pilha.append(tabelaTraducao.get('<operador_logico>'))
  elif (opcao == 2): # <expressao_logica_aux> → ε
    pass

# Empilha a regra equivalente ao não-terminal <expressao_relacional>
def regra_expressao_relacional(pilha, opcao):
  if (opcao == 1): # <expressao_relacional> → <expressao_aritmetica> <operador_relacional> <expressao_aritmetica>
    pilha.append(tabelaTraducao.get('<expressao_aritmetica>'))
    pilha.append(tabelaTraducao.get('<operador_relacional>'))
    pilha.append(tabelaTraducao.get('<expressao_aritmetica>'))

# Empilha a regra equivalente ao não-terminal <nome_do_programa>
def regra_nome_do_programa(pilha, opcao):
  if (opcao == 1): # <nome_do_programa> → VARIAVEL <nome_do_programa_aux>
    pilha.append(tabelaTraducao.get('<nome_do_programa_aux>'))
    pilha.append(tabelaTraducao.get('VARIAVEL'))

# Empilha a regra equivalente ao não-terminal <nome_do_programa_aux>
def regra_nome_do_programa_aux(pilha, opcao):
  if (opcao == 1): # <nome_do_programa_aux> → VARIAVEL <nome_do_programa>
    pilha.append(tabelaTraducao.get('<nome_do_programa>'))
    pilha.append(tabelaTraducao.get('VARIAVEL'))
  elif (opcao == 2): # <nome_do_programa_aux> → ε
    pass

# Empilha a regra equivalente ao não-terminal <operador_aritmetico>
def regra_operador_aritmetico(pilha, opcao):
  if (opcao == 1): # <operador_aritmetico> → OPERADOR_ADICAO
    pilha.append(tabelaTraducao.get('OPERADOR_ADICAO'))
  elif (opcao == 2): # <operador_aritmetico> → OPERADOR_SUBTRACAO
    pilha.append(tabelaTraducao.get('OPERADOR_SUBTRACAO'))
  elif (opcao == 3): # <operador_aritmetico> → OPERADOR_PRODUTO
    pilha.append(tabelaTraducao.get('OPERADOR_PRODUTO'))
  elif (opcao == 4): # <operador_aritmetico> → OPERADOR_DIVISAO
    pilha.append(tabelaTraducao.get('OPERADOR_DIVISAO'))

# Empilha a regra equivalente ao não-terminal <operador_logico>
def regra_operador_logico(pilha, opcao):
  if (opcao == 1): # <operador_logico> → OPERADOR_AND
    pilha.append(tabelaTraducao.get('OPERADOR_AND'))
  elif (opcao == 2): # <operador_logico> → OPERADOR_OR
    pilha.append(tabelaTraducao.get('OPERADOR_OR'))

# Empilha a regra equivalente ao não-terminal <operador_relacional>
def regra_operador_relacional(pilha, opcao):
  if (opcao == 1): # <operador_relacional> → OPERADOR_MENOR_IGUAL
    pilha.append(tabelaTraducao.get('OPERADOR_MENOR_IGUAL'))
  elif (opcao == 2): # <operador_relacional> → OPERADOR_IGUAL
    pilha.append(tabelaTraducao.get('OPERADOR_IGUAL'))

# Empilha a regra equivalente ao não-terminal <tipo>
def regra_tipo(pilha, opcao):
  if (opcao == 1): # <tipo> → TIPO_INTEIRO
    pilha.append(tabelaTraducao.get('TIPO_INTEIRO'))
  elif (opcao == 2): # <tipo> → TIPO_REAL
    pilha.append(tabelaTraducao.get('TIPO_REAL'))
  elif (opcao == 3): # <tipo> → TIPO_CARACTER
    pilha.append(tabelaTraducao.get('TIPO_CARACTER'))
  elif (opcao == 4): # <tipo> → TIPO_CADEIA
    pilha.append(tabelaTraducao.get('TIPO_CADEIA'))
  elif (opcao == 5): # <tipo> → TIPO_LISTA_INT
    pilha.append(tabelaTraducao.get('TIPO_LISTA_INT'))
  elif (opcao == 6): # <tipo> → TIPO_LISTA_REAL
    pilha.append(tabelaTraducao.get('TIPO_LISTA_REAL'))

# Empilha a regra equivalente ao não-terminal <variavel>
def regra_variavel(pilha, opcao):
  if (opcao == 1): # <variavel> → VARIAVEL
    pilha.append(tabelaTraducao.get('VARIAVEL'))
  elif (opcao == 2): # <variavel> → VARIAVEL_LISTA
    pilha.append(tabelaTraducao.get('VARIAVEL_LISTA'))

def analisador_sintatico(arquivo, tabelaTraducao):
  try:
    with open(f"{arquivo}", "r") as arquivo:
      pilha = [] # Pilha do analisador sintático
      entrada_traduzida = [] # Pilha dos IDs relativos ao arquivo de entrada
      tolerancia = 0 # máximo de erros tolerados antes de definir como não reconhecido
      tentativa = 0 # Contador para a tolerância de erros
      final = False # Booleano para indicar o fim da analise

      for linha in arquivo:
        entrada_traduzida.append(traduzirLinha(linha.rstrip()))

        if (entrada_traduzida[-1] == -1): # Se a ultima entrada adicionada for invalida, não reconhece
          print("Não reconhece")
          final = True
          break

      if (entrada_traduzida[0] == tabelaTraducao.get('$')):
        print("Entrada vazia")

      else:
        pilha.append(tabelaTraducao.get('$')) # Empilha o ID do símbolo de final de cadeia $
        pilha.append(tabelaTraducao.get('<algox>')) # Empilha o ID do não terminal <algox>

        # Loop princial do analisador
        while(not final and tentativa <= tolerancia):
          # Lida com valores vazios no topo da pilha
          if (pilha[-1] == None):
            pilha.pop()

          # Caso a pilha fique vazia durante a execução, não reconhece
          if (len(pilha) == 0):
            tentativa = float('inf') # Garante que será maior que a toleração com o valor infinito positivo
            final = True

          # Se a entrada atual for $
          if (entrada_traduzida[0] == tabelaTraducao.get('$')):
            # Se o topo da pilha for $
            if (pilha[-1] == tabelaTraducao.get('$')):
              # Reconhecimento da entrada
              final = True
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            else:
              erro_sai(pilha)
              tentativa += 1

          # Se a entrada atual for ABRE
          elif (entrada_traduzida[0] == tabelaTraducao.get('ABRE')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica> ou <expressao_logica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_logica>')):
              pilha.pop()
              regra_expressao_aritmetica(pilha, opcao=3)
            # Se o topo da pilha for <expressao_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              pilha.pop()
              regra_expressao_relacional(pilha, opcao=1)
            # Se o topo da pilha for <operador_aritmetico> ou <operador_logico> ou <operador_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<operador_aritmetico>') or pilha[-1] == tabelaTraducao.get('<operador_logico>') or pilha[-1] == tabelaTraducao.get('<operador_relacional>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for CADEIA
          elif (entrada_traduzida[0] == tabelaTraducao.get('CADEIA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <comando_saida_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_aux>')):
              pilha.pop()
              regra_comando_saida_aux(pilha, opcao=2)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for CONSTANTE_INTEIRA
          elif (entrada_traduzida[0] == tabelaTraducao.get('CONSTANTE_INTEIRA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <constante>
            elif (pilha[-1] == tabelaTraducao.get('<constante>')):
              pilha.pop()
              regra_constante(pilha, opcao=1)
            # Se o topo da pilha for <expressao_aritmetica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>')):
              pilha.pop()
              regra_expressao_aritmetica(pilha, opcao=1)
            # Se o topo da pilha for <expressao_logica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica>')):
              pilha.pop()
              regra_expressao_logica(pilha, opcao=1)
            # Se o topo da pilha for <expressao_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              pilha.pop()
              regra_expressao_relacional(pilha, opcao=1)
            # Se o topo da pilha for <operador_aritmetico> ou <operador_logico> ou <operador_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<operador_aritmetico>') or pilha[-1] == tabelaTraducao.get('<operador_logico>') or pilha[-1] == tabelaTraducao.get('<operador_relacional>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for CONSTANTE_REAL
          elif (entrada_traduzida[0] == tabelaTraducao.get('CONSTANTE_REAL')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <constante>
            elif (pilha[-1] == tabelaTraducao.get('<constante>')):
              pilha.pop()
              regra_constante(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>')):
              pilha.pop()
              regra_expressao_aritmetica(pilha, opcao=1)
            # Se o topo da pilha for <expressao_logica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica>')):
              pilha.pop()
              regra_expressao_logica(pilha, opcao=1)
            # Se o topo da pilha for <expressao_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              pilha.pop()
              regra_expressao_relacional(pilha, opcao=1)
            # Se o topo da pilha for <operador_aritmetico> ou <operador_logico> ou <operador_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<operador_aritmetico>') or pilha[-1] == tabelaTraducao.get('<operador_logico>') or pilha[-1] == tabelaTraducao.get('<operador_relacional>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for ENQUANTO
          elif (entrada_traduzida[0] == tabelaTraducao.get('ENQUANTO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algoritmo>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo>')):
              pilha.pop()
              regra_algoritmo(pilha, opcao=1)
            # Se o topo da pilha for <algoritmo_aux>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando>
            elif (pilha[-1] == tabelaTraducao.get('<comando>')):
              pilha.pop()
              regra_comando(pilha, opcao=3)
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_repeticao>
            elif (pilha[-1] == tabelaTraducao.get('<comando_repeticao>')):
              pilha.pop()
              regra_comando_repeticao(pilha, opcao=1)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=2)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_atribuicao> ou <comando_entrada> ou <comando_saida> ou <comando_saida_aux> ou
            # <comando_selecao> ou <declaracoes> ou <expressao_aritmetica> ou <expressao_relacional> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>') or pilha[-1] == tabelaTraducao.get('<comando_entrada>') or pilha[-1] == tabelaTraducao.get('<comando_saida>') or
                  pilha[-1] == tabelaTraducao.get('<comando_saida_aux>') or pilha[-1] == tabelaTraducao.get('<comando_selecao>') or pilha[-1] == tabelaTraducao.get('<declaracoes>') or
                  pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_relacional>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for ENTAO
          elif (entrada_traduzida[0] == tabelaTraducao.get('ENTAO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica> ou <expressao_relacional> ou <variavel>
            elif ( pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for ESCREVA
          elif (entrada_traduzida[0] == tabelaTraducao.get('ESCREVA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algoritmo>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo>')):
              pilha.pop()
              regra_algoritmo(pilha, opcao=1)
            # Se o topo da pilha for <algoritmo_aux>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando>
            elif (pilha[-1] == tabelaTraducao.get('<comando>')):
              pilha.pop()
              regra_comando(pilha, opcao=4)
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida>')):
              pilha.pop()
              regra_comando_saida(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_atribuicao> ou <comando_entrada> ou
            # <comando_saida> ou <declaracoes> ou <expressao_relacional> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>') or pilha[-1] == tabelaTraducao.get('<comando_entrada>') or pilha[-1] == tabelaTraducao.get('<comando_saida>') or
                  pilha[-1] == tabelaTraducao.get('<declaracoes>') or pilha[-1] == tabelaTraducao.get('<expressao_relacional>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for FECHA
          elif (entrada_traduzida[0] == tabelaTraducao.get('FECHA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_logica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica_aux>')):
              pilha.pop()
              regra_expressao_logica_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica> ou <expressao_logica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_logica>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for FIM
          elif (entrada_traduzida[0] == tabelaTraducao.get('FIM')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algoritmo_aux>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=2)
            # Se o topo da pilha for <algoritmo> ou <corpo_do_programa> ou <comando>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo>') or pilha[-1] == tabelaTraducao.get('<corpo_do_programa>') or pilha[-1] == tabelaTraducao.get('<comando>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for FIM_ENQUANTO
          elif (entrada_traduzida[0] == tabelaTraducao.get('FIM_ENQUANTO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando> ou <comando_atribuicao> ou <comando_entrada> ou
            # <comando_repeticao> ou <comando_saida> ou <comando_saida_aux> ou <comando_selecao> ou
            # <expressao_aritmetica> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando>') or pilha[-1] == tabelaTraducao.get('<comando_atribuicao>') or pilha[-1] == tabelaTraducao.get('<comando_entrada>') or
                  pilha[-1] == tabelaTraducao.get('<comando_repeticao>') or pilha[-1] == tabelaTraducao.get('<comando_saida>') or pilha[-1] == tabelaTraducao.get('<comando_saida_aux>') or
                  pilha[-1] == tabelaTraducao.get('<comando_selecao>') or pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for FIM_SE
          elif (entrada_traduzida[0] == tabelaTraducao.get('FIM_SE')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando> ou <comando_atribuicao> ou <comando_entrada> ou
            # <comando_repeticao> ou <comando_saida> ou <comando_saida_aux> ou <comando_selecao> ou
            # <expressao_aritmetica> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando>') or pilha[-1] == tabelaTraducao.get('<comando_atribuicao>') or pilha[-1] == tabelaTraducao.get('<comando_entrada>') or
                  pilha[-1] == tabelaTraducao.get('<comando_repeticao>') or pilha[-1] == tabelaTraducao.get('<comando_saida>') or pilha[-1] == tabelaTraducao.get('<comando_saida_aux>') or
                  pilha[-1] == tabelaTraducao.get('<comando_selecao>') or pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for INICIO
          elif (entrada_traduzida[0] == tabelaTraducao.get('INICIO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <nome_do_programa_aux>
            elif (pilha[-1] == tabelaTraducao.get('<nome_do_programa_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=2)
            # Se o topo da pilha for <nome_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<nome_do_programa>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for LEIA
          elif (entrada_traduzida[0] == tabelaTraducao.get('LEIA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algoritmo>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo>')):
              pilha.pop()
              regra_algoritmo(pilha, opcao=1)
            # Se o topo da pilha for <algoritmo_aux>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando>
            elif (pilha[-1] == tabelaTraducao.get('<comando>')):
              pilha.pop()
              regra_comando(pilha, opcao=2)
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_entrada>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada>')):
              pilha.pop()
              regra_comando_entrada(pilha, opcao=1)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=2)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_atribuicao> ou <comando_repeticao> ou <comando_saida> ou
            # <comando_saida_aux> ou <comando_selecao> ou <declaracoes> ou
            # <expressao_aritmetica> ou <expressao_relacional> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>') or pilha[-1] == tabelaTraducao.get('<comando_repeticao>') or pilha[-1] == tabelaTraducao.get('<comando_saida>') or
                  pilha[-1] == tabelaTraducao.get('<comando_saida_aux>') or pilha[-1] == tabelaTraducao.get('<comando_selecao>') or pilha[-1] == tabelaTraducao.get('<declaracoes>') or
                  pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_relacional>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_ADICAO
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_ADICAO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=1)
            # Se o topo da pilha for <operador_aritmetico>
            elif (pilha[-1] == tabelaTraducao.get('<operador_aritmetico>')):
              pilha.pop()
              regra_operador_aritmetico(pilha, opcao=1)
            # Se o topo da pilha for <constante> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<constante>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_AND
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_AND')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_logica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica_aux>')):
              pilha.pop()
              regra_expressao_logica_aux(pilha, opcao=1)
            # Se o topo da pilha for <operador_logico>
            elif (pilha[-1] == tabelaTraducao.get('<operador_logico>')):
              pilha.pop()
              regra_operador_logico(pilha, opcao=1)
            # Se o topo da pilha for <expressao_aritmetica> ou <expressao_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_ATRIBUICAO
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_ATRIBUICAO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_DIVISAO
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_DIVISAO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=1)
            # Se o topo da pilha for <operador_aritmetico>
            elif (pilha[-1] == tabelaTraducao.get('<operador_aritmetico>')):
              pilha.pop()
              regra_operador_aritmetico(pilha, opcao=4)
            # Se o topo da pilha for <constante> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<constante>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_IGUAL
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_IGUAL')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <operador_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<operador_relacional>')):
              pilha.pop()
              regra_operador_relacional(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_MENOR_IGUAL
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_MENOR_IGUAL')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <operador_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<operador_relacional>')):
              pilha.pop()
              regra_operador_relacional(pilha, opcao=1)
            # Se o topo da pilha for <expressao_aritmetica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_NOT
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_NOT')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_logica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica>')):
              pilha.pop()
              regra_expressao_logica(pilha, opcao=2)
            # Se o topo da pilha for <operador_logico>
            elif (pilha[-1] == tabelaTraducao.get('<operador_logico>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_OR
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_OR')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_logica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica_aux>')):
              pilha.pop()
              regra_expressao_logica_aux(pilha, opcao=1)
            # Se o topo da pilha for <operador_logico>
            elif (pilha[-1] == tabelaTraducao.get('<operador_logico>')):
              pilha.pop()
              regra_operador_logico(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica> ou <expressao_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_PRODUTO
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_PRODUTO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=1)
            # Se o topo da pilha for <operador_aritmetico>
            elif (pilha[-1] == tabelaTraducao.get('<operador_aritmetico>')):
              pilha.pop()
              regra_operador_aritmetico(pilha, opcao=3)
            # Se o topo da pilha for <constante> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<constante>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for OPERADOR_SUBTRACAO
          elif (entrada_traduzida[0] == tabelaTraducao.get('OPERADOR_SUBTRACAO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=1)
            # Se o topo da pilha for <operador_aritmetico>
            elif (pilha[-1] == tabelaTraducao.get('<operador_aritmetico>')):
              pilha.pop()
              regra_operador_aritmetico(pilha, opcao=2)
            # Se o topo da pilha for <constante> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<constante>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for PROGRAMA
          elif (entrada_traduzida[0] == tabelaTraducao.get('PROGRAMA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algox>
            elif (pilha[-1] == tabelaTraducao.get('<algox>')):
              pilha.pop()
              regra_algox(pilha, opcao=1)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for SE
          elif (entrada_traduzida[0] == tabelaTraducao.get('SE')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algoritmo>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo>')):
              pilha.pop()
              regra_algoritmo(pilha, opcao=1)
            # Se o topo da pilha for <algoritmo_aux>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando>
            elif (pilha[-1] == tabelaTraducao.get('<comando>')):
              pilha.pop()
              regra_comando(pilha, opcao=5)
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=2)
            # Se o topo da pilha for <comando_selecao>
            elif (pilha[-1] == tabelaTraducao.get('<comando_selecao>')):
              pilha.pop()
              regra_comando_selecao(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_atribuicao> ou <comando_entrada> ou <comando_repeticao> ou
            # <comando_saida> ou <comando_saida_aux> ou <declaracoes> ou
            # <expressao_aritmetica> ou <expressao_relacional> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>') or pilha[-1] == tabelaTraducao.get('<comando_entrada>') or pilha[-1] == tabelaTraducao.get('<comando_repeticao>') or
                  pilha[-1] == tabelaTraducao.get('<comando_saida>') or pilha[-1] == tabelaTraducao.get('<comando_saida_aux>') or pilha[-1] == tabelaTraducao.get('<declaracoes>') or
                  pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<expressao_relacional>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for TIPO_CADEIA
          elif (entrada_traduzida[0] == tabelaTraducao.get('TIPO_CADEIA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <corpo_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<corpo_do_programa>')):
              pilha.pop()
              regra_corpo_do_programa(pilha, opcao=1)
            # Se o topo da pilha for <declaracao>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao>')):
              pilha.pop()
              regra_declaracao(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<tipo>')):
              pilha.pop()
              regra_tipo(pilha, opcao=4)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for TIPO_CARACTER
          elif (entrada_traduzida[0] == tabelaTraducao.get('TIPO_CARACTER')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <corpo_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<corpo_do_programa>')):
              pilha.pop()
              regra_corpo_do_programa(pilha, opcao=1)
            # Se o topo da pilha for <declaracao>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao>')):
              pilha.pop()
              regra_declaracao(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<tipo>')):
              pilha.pop()
              regra_tipo(pilha, opcao=3)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for TIPO_INTEIRO
          elif (entrada_traduzida[0] == tabelaTraducao.get('TIPO_INTEIRO')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <corpo_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<corpo_do_programa>')):
              pilha.pop()
              regra_corpo_do_programa(pilha, opcao=1)
            # Se o topo da pilha for <declaracao>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao>')):
              pilha.pop()
              regra_declaracao(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes>')):
              pilha.pop()
              regra_declaracoes(pilha, opcao=1)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<tipo>')):
              pilha.pop()
              regra_tipo(pilha, opcao=1)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for TIPO_LISTA_INT
          elif (entrada_traduzida[0] == tabelaTraducao.get('TIPO_LISTA_INT')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <corpo_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<corpo_do_programa>')):
              pilha.pop()
              regra_corpo_do_programa(pilha, opcao=1)
            # Se o topo da pilha for <declaracao>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao>')):
              pilha.pop()
              regra_declaracao(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<tipo>')):
              pilha.pop()
              regra_tipo(pilha, opcao=5)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for TIPO_LISTA_REAL
          elif (entrada_traduzida[0] == tabelaTraducao.get('TIPO_LISTA_REAL')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <corpo_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<corpo_do_programa>')):
              pilha.pop()
              regra_corpo_do_programa(pilha, opcao=1)
            # Se o topo da pilha for <declaracao>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao>')):
              pilha.pop()
              regra_declaracao(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<tipo>')):
              pilha.pop()
              regra_tipo(pilha, opcao=6)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for TIPO_REAL
          elif (entrada_traduzida[0] == tabelaTraducao.get('TIPO_REAL')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <corpo_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<corpo_do_programa>')):
              pilha.pop()
              regra_corpo_do_programa(pilha, opcao=1)
            # Se o topo da pilha for <declaracao>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao>')):
              pilha.pop()
              regra_declaracao(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=1)
            # Se o topo da pilha for <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<tipo>')):
              pilha.pop()
              regra_tipo(pilha, opcao=2)
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for VARIAVEL
          elif (entrada_traduzida[0] == tabelaTraducao.get('VARIAVEL')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algoritmo>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo>')):
              pilha.pop()
              regra_algoritmo(pilha, opcao=1)
            # Se o topo da pilha for <algoritmo_aux>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando>
            elif (pilha[-1] == tabelaTraducao.get('<comando>')):
              pilha.pop()
              regra_comando(pilha, opcao=1)
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_atribuicao>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>')):
              pilha.pop()
              regra_comando_atribuicao(pilha, opcao=1)
            # Se o topo da pilha for <comando_atribuicao>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>')):
              pilha.pop()
              regra_comando_atribuicao(pilha, opcao=1)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_aux>')):
              pilha.pop()
              regra_comando_saida_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=2)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>')):
              pilha.pop()
              regra_expressao_aritmetica(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_logica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica>')):
              pilha.pop()
              regra_expressao_logica(pilha, opcao=1)
            # Se o topo da pilha for <expressao_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              pilha.pop()
              regra_expressao_relacional(pilha, opcao=1)
            # Se o topo da pilha for <nome_do_programa>
            elif (pilha[-1] == tabelaTraducao.get('<nome_do_programa>')):
              pilha.pop()
              regra_nome_do_programa(pilha, opcao=1)
            # Se o topo da pilha for <nome_do_programa_aux>
            elif (pilha[-1] == tabelaTraducao.get('<nome_do_programa_aux>')):
              pilha.pop()
              regra_nome_do_programa_aux(pilha, opcao=1)
            # Se o topo da pilha for <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<variavel>')):
              pilha.pop()
              regra_variavel(pilha, opcao=1)
            # Se o topo da pilha for <comando_entrada> ou <comando_repeticao> ou <comando_saida> ou
            # <comando_selecao> ou <declaracoes> ou <operador_aritmetico> ou
            # <operador_logico> ou <operador_relacional> ou <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada>') or pilha[-1] == tabelaTraducao.get('<comando_repeticao>') or pilha[-1] == tabelaTraducao.get('<comando_saida>') or
                  pilha[-1] == tabelaTraducao.get('<comando_selecao>') or pilha[-1] == tabelaTraducao.get('<declaracoes>') or pilha[-1] == tabelaTraducao.get('<operador_aritmetico>') or
                  pilha[-1] == tabelaTraducao.get('<operador_logico>') or pilha[-1] == tabelaTraducao.get('<operador_relacional>') or pilha[-1] == tabelaTraducao.get('<tipo>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for VARIAVEL_LISTA
          elif (entrada_traduzida[0] == tabelaTraducao.get('VARIAVEL_LISTA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <algoritmo>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo>')):
              pilha.pop()
              regra_algoritmo(pilha, opcao=1)
            # Se o topo da pilha for <algoritmo_aux>
            elif (pilha[-1] == tabelaTraducao.get('<algoritmo_aux>')):
              pilha.pop()
              regra_algoritmo_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando>
            elif (pilha[-1] == tabelaTraducao.get('<comando>')):
              pilha.pop()
              regra_comando(pilha, opcao=1)
            # Se o topo da pilha for <comando_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_aux>')):
              pilha.pop()
              regra_comando_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_atribuicao>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>')):
              pilha.pop()
              regra_comando_atribuicao(pilha, opcao=1)
            # Se o topo da pilha for <comando_atribuicao>
            elif (pilha[-1] == tabelaTraducao.get('<comando_atribuicao>')):
              pilha.pop()
              regra_comando_atribuicao(pilha, opcao=1)
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_aux>')):
              pilha.pop()
              regra_comando_saida_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=2)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=2)
            # Se o topo da pilha for <declaracoes_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracoes_aux>')):
              pilha.pop()
              regra_declaracoes_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_aritmetica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>')):
              pilha.pop()
              regra_expressao_aritmetica(pilha, opcao=1)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <expressao_logica>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_logica>')):
              pilha.pop()
              regra_expressao_logica(pilha, opcao=1)
            # Se o topo da pilha for <expressao_relacional>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_relacional>')):
              pilha.pop()
              regra_expressao_relacional(pilha, opcao=1)
            # Se o topo da pilha for <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<variavel>')):
              pilha.pop()
              regra_variavel(pilha, opcao=2)
            # Se o topo da pilha for <comando_entrada> ou <comando_repeticao> ou <comando_saida> ou
            # <comando_selecao> ou <declaracoes> ou <operador_aritmetico> ou
            # <operador_logico> ou <operador_relacional> ou <tipo>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada>') or pilha[-1] == tabelaTraducao.get('<comando_repeticao>') or pilha[-1] == tabelaTraducao.get('<comando_saida>') or
                  pilha[-1] == tabelaTraducao.get('<comando_selecao>') or pilha[-1] == tabelaTraducao.get('<declaracoes>') or pilha[-1] == tabelaTraducao.get('<operador_aritmetico>') or
                  pilha[-1] == tabelaTraducao.get('<operador_logico>') or pilha[-1] == tabelaTraducao.get('<operador_relacional>') or pilha[-1] == tabelaTraducao.get('<tipo>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

          # Se a entrada atual for VIRGULA
          elif (entrada_traduzida[0] == tabelaTraducao.get('VIRGULA')):
            # Se o topo da pilha for igual a entrada
            if (pilha[-1] == entrada_traduzida[0]):
              # Match do não-terminal
              pilha.pop() # Desempilha o não-terminal
              entrada_traduzida.pop(0) # Remove a entrada atual e segue pra próxima
            # Se o topo da pilha for <comando_entrada_aux>
            elif (pilha[-1] == tabelaTraducao.get('<comando_entrada_aux>')):
              pilha.pop()
              regra_comando_entrada_aux(pilha, opcao=1)
            # Se o topo da pilha for <comando_saida_cadeia_variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_cadeia_variavel>')):
              pilha.pop()
              regra_comando_saida_cadeia_variavel(pilha, opcao=1)
            # Se o topo da pilha for <comando_saida_variavel_cadeia>
            elif (pilha[-1] == tabelaTraducao.get('<comando_saida_variavel_cadeia>')):
              pilha.pop()
              regra_comando_saida_variavel_cadeia(pilha, opcao=1)
            # Se o topo da pilha for <declaracao_aux>
            elif (pilha[-1] == tabelaTraducao.get('<declaracao_aux>')):
              pilha.pop()
              regra_declaracao_aux(pilha, opcao=1)
            # Se o topo da pilha for <expressao_aritmetica_aux>
            elif (pilha[-1] == tabelaTraducao.get('<expressao_aritmetica_aux>')):
              pilha.pop()
              regra_expressao_aritmetica_aux(pilha, opcao=2)
            # Se o topo da pilha for <comando_repeticao> ou <comando_selecao> ou
            # <expressao_aritmetica> ou <variavel>
            elif (pilha[-1] == tabelaTraducao.get('<comando_repeticao>') or pilha[-1] == tabelaTraducao.get('<comando_selecao>') or
                  pilha[-1] == tabelaTraducao.get('<expressao_aritmetica>') or pilha[-1] == tabelaTraducao.get('<variavel>')):
              erro_sai(pilha)
              tentativa += 1
            # Qualquer outro caso
            else:
              erro_varre(entrada_traduzida)
              tentativa += 1

        if (tentativa <= tolerancia):
          print("Reconhece")
        else:
          print("Não reconhece")
  except FileNotFoundError:
    print(f"O arquivo '{arquivo}' não foi encontrado. Tente o caminho completo.")


# Main

# Para simplificar a implementação, o código irá identificar os terminais e não-terminais pelos seus respectivos IDs numéricos
# A escolha dos IDs foi feita por ordem alfabética de não-terminal e terminal, sendo 0 o símbolo $ de final de cadeia,
# os valores de 1 a 31 os não-terminais e de 50 a 83 os terminais.
tabelaTraducao = {
  "$": 0,
  "<algoritmo>": 1,
  "<algoritmo_aux>": 2,
  "<algox>": 3,
  "<comando>": 4,
  "<comando_aux>": 5,
  "<comando_atribuicao>": 6,
  "<comando_entrada>": 7,
  "<comando_entrada_aux>": 8,
  "<comando_repeticao>": 9,
  "<comando_saida>": 10,
  "<comando_saida_aux>": 11,
  "<comando_saida_cadeia_variavel>": 12,
  "<comando_saida_variavel_cadeia>": 13,
  "<comando_selecao>": 14,
  "<constante>": 15,
  "<corpo_do_programa>": 16,
  "<declaracao>": 17,
  "<declaracao_aux>": 18,
  "<declaracoes>": 19,
  "<declaracoes_aux>": 20,
  "<expressao_aritmetica>": 21,
  "<expressao_aritmetica_aux>": 22,
  "<expressao_logica>": 23,
  "<expressao_logica_aux>": 24,
  "<expressao_relacional>": 25,
  "<nome_do_programa>": 26,
  "<nome_do_programa_aux>": 27,
  "<operador_aritmetico>": 28,
  "<operador_logico>": 29,
  "<operador_relacional>": 30,
  "<tipo>": 31,
  "<variavel>": 32,
  "ABRE": 50,
  "CADEIA": 51,
  "CONSTANTE_INTEIRA": 52,
  "CONSTANTE_REAL": 53,
  "ENQUANTO": 54,
  "ENTAO": 55,
  "ESCREVA": 56,
  "FECHA": 57,
  "FIM": 58,
  "FIM_ENQUANTO": 59,
  "FIM_SE": 60,
  "INICIO": 61,
  "LEIA": 62,
  "OPERADOR_ADICAO": 63,
  "OPERADOR_AND": 64,
  "OPERADOR_ATRIBUICAO": 65,
  "OPERADOR_DIVISAO": 66,
  "OPERADOR_IGUAL": 67,
  "OPERADOR_MENOR_IGUAL": 68,
  "OPERADOR_NOT": 69,
  "OPERADOR_OR": 70,
  "OPERADOR_PRODUTO": 71,
  "OPERADOR_SUBTRACAO": 72,
  "PROGRAMA": 73,
  "SE": 74,
  "TIPO_CADEIA": 75,
  "TIPO_CARACTER": 76,
  "TIPO_INTEIRO": 77,
  "TIPO_LISTA_INT": 78,
  "TIPO_LISTA_REAL": 79,
  "TIPO_REAL": 80,
  "VARIAVEL": 81,
  "VARIAVEL_LISTA": 82,
  "VIRGULA": 83
}

arquivo = input("Endereço do arquivo de entrada (com a extensão): ")
analisador_sintatico(arquivo, tabelaTraducao)