%option noyywrap

%{
  #include <stdio.h>
%}

PROGRAMA             "PROGRAMA"
INICIO               "INICIO"
FIM_SE               "FIM_SE"
FIM_ENQUANTO         "FIM_ENQUANTO"
FIM                  "FIM"
SE                   "SE"
ENTAO                "ENTAO"
ENQUANTO             "ENQUANTO"
LEIA                 "LEIA"
ESCREVA              "ESCREVA"
TIPO_INTEIRO         "INTEIRO"
TIPO_REAL            "REAL"
TIPO_CARACTER        "CARACTER"
TIPO_CADEIA          "CADEIA"
TIPO_LISTA_INT       "LISTA_INT"
TIPO_LISTA_REAL      "LISTA_REAL"
NOT                  ".N."
AND                  ".E."
OR                   ".OU."
IGUAL                ".I."
MENOR_IGUAL          ".M."
ATRIBUICAO           ":="
SOMA                 "+"
SUBTRACAO            "-"
PRODUTO              "*"
DIVISAO              "\\"
VIRGULA              ","
DIGITO               ([0-9])
CONSTANTE_INTEIRA    ({DIGITO}+)
CONSTANTE_REAL       ({DIGITO}+","%{DIGITO}+)
LETRA                ([a-zA-Z])
PALAVRA              ([a-zA-Z_-])
VARIAVEL             ({LETRA}({PALAVRA}|{CONSTANTE_INTEIRA})*)
VARIAVEL_LISTA       ({VARIAVEL}"["({VARIAVEL}|{CONSTANTE_INTEIRA})"]")
CADEIA               (\'[^'\r\n]+\')
COMENTARIO           (\{.*\})

%%

{SOMA}                     { printf("OPERADOR_ADICAO\n"); }
{SUBTRACAO}                { printf("OPERADOR_SUBTRACAO\n"); }
{PRODUTO}                  { printf("OPERADOR_PRODUTO\n"); }
{DIVISAO}                  { printf("OPERADOR_DIVISAO\n"); }
{VIRGULA}                  { printf("VIRGULA\n"); }
{PROGRAMA}                 { printf("PROGRAMA\n"); }
{INICIO}                   { printf("INICIO\n"); }
{FIM_SE}                   { printf("FIM_SE\n"); }
{FIM_ENQUANTO}             { printf("FIM_ENQUANTO\n"); }
{FIM}                      { printf("FIM\n"); }
{SE}                       { printf("SE\n"); }
{ENTAO}                    { printf("ENTAO\n"); }
{ENQUANTO}                 { printf("ENQUANTO\n"); }
{LEIA}                     { printf("LEIA\n"); }
{ESCREVA}                  { printf("ESCREVA\n"); }
{TIPO_INTEIRO}             { printf("TIPO_INTEIRO\n"); }
{TIPO_REAL}                { printf("TIPO_REAL\n"); }
{TIPO_CARACTER}            { printf("TIPO_CARACTER\n"); }
{TIPO_CADEIA}              { printf("TIPO_CADEIA\n"); }
{TIPO_LISTA_INT}           { printf("TIPO_LISTA_INT\n"); }
{TIPO_LISTA_REAL}          { printf("TIPO_LISTA_REAL\n"); }
{NOT}                      { printf("OPERADOR_NOT\n"); }
{AND}                      { printf("OPERADOR_AND\n"); }
{OR}                       { printf("OPERADOR_OR\n"); }
{IGUAL}                    { printf("OPERADOR_IGUAL\n"); }
{MENOR_IGUAL}              { printf("OPERADOR_MENOR_IGUAL\n"); }
{ATRIBUICAO}               { printf("OPERADOR_ATRIBUICAO\n"); }
{CONSTANTE_INTEIRA}        { printf("CONSTANTE_INTEIRA\n"); }
{CONSTANTE_REAL}           { printf("CONSTANTE_REAL\n"); }
{VARIAVEL}                 { printf("VARIAVEL\n"); }
{VARIAVEL_LISTA}           { printf("VARIAVEL_LISTA\n"); }
{CADEIA}                   { printf("CADEIA\n"); }
{COMENTARIO}               { /* Pula os trechos comentados */ }
[ \t\r\n]+                 { /* Ignora espacos em branco, tabulacao e quebras de linha */ }
.                          { printf("ERRO\n"); }
<<EOF>>                    { printf("$"); return 0; } // Adiciona um $ para indicar o final da entrada

%%

int main() {
  yylex();
  return 0;
}