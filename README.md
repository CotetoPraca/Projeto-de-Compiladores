# Projeto-de-Compiladores
Repositório com os arquivos criados para o projeto da matéria de Compiladores da UNIFEI. O projeto visa criar analisadores léxico e sintático para a linguagem hipotética ALGOX, descrita no arquivo `Projeto_Algox.pdf`.

## Requerimentos

- FLEX instalado no computador
- WSL para usuários de Windows
- Compilador para Python 3

## Analisador Léxico

O analisador léxico retorna a listagem de tokens detectados na entrada. Há dois arquivos de exemplo no repositório: entradaFatorial.in e entradaLeituraLista.in. Ambos são exemplos de algoritmos escritos na linguagem hipotética Algox; o primeiro deles representa um algoritmo para cálculo fatorial na linguagem Algox, enquanto o segundo é um algoritmo para leitura de uma lista de valores.

### Executando o arquivo FLEX

Primeiro geramos o arquivo `lex.yy.c` com o seguinte comando:

`flex "nome_do_arquivo"`

Geramos um arquivo executável `exec` usando o gcc:

`gcc -o exec lex.yy.c`

Por fim, executamos o analisador indicando como argumentos um arquivo de entrada e um de saída.

`./exec < "arquivo_de_entrada" > "arquivo_de_saida"`

## Analisador Sintático

Verifica se a listagem de tokens geradas pelo analisador léxico segue a ordem esperada pela gramática. O código foi implementado na linguagem Python para agilizar a implementação.

O código espera como entrada o arquivo de saída gerado pelo analisador léxico e retorna se a gramática reconhece ou não aquela entrada, com uma tolerância máxima de 2 erros. Para executar o código, basta executá-lo como um arquivo Python e digitar o endereço do arquivo de entrada.


