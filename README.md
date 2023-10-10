# Projeto-de-Compiladores
Repositório com os arquivos criados para o projeto da matéria de Compiladores da UNIFEI. O projeto visa criar analisadores léxico e sintático para a linguagem hipotética ALGOX, descrita no arquivo `Projeto_Algox.pdf`.

## Requerimentos

- FLEX instalado no computador
- WSL para usuários de Windows

## Analisador Léxico

O analisador léxico retorna a listagem de tokens detectados na entrada.

### Executando o arquivo FLEX

Primeiro geramos o arquivo `lex.yy.c` com o seguinte comando:

`flex "nome_do_arquivo"`

Geramos um arquivo executável `exec` usando o gcc:

`gcc -o exec lex.yy.c`

Por fim, executamos o analisador indicando como argumentos um arquivo de entrada e um de saída.

`./exec < "arquivo_de_entrada" > "arquivo_de_saida"`

## Analisador Sintático

Verifica se a listagem de tokens geradas pelo analisador léxico segue a ordem esperada pela gramática. Pseudo-código disponível no arquivo `Projeto_Algox.pdf`.

> **_NOTA:_**  Devido a falta de tempo, só o pseudocódigo do analisador sintático está disponível.
