%option noyywrap

%{
  #include <stdio.h>
%}

ABRE                     "("
ENQUANTO                 "ENQUANTO"
ENTAO                    "ENTAO"
ESCREVA                  "ESCREVA"
FECHA                    ")"
FIM                      "FIM"
FIM_ENQUANTO             "FIM_ENQUANTO"
FIM_SE                   "FIM_SE"
INICIO                   "INICIO"
LEIA                     "LEIA"
OPERADOR_ADICAO          "+"
OPERADOR_AND             ".E."
OPERADOR_ATRIBUICAO      ":="
OPERADOR_DIVISAO         "\\"
OPERADOR_IGUAL           ".I."
OPERADOR_MENOR_IGUAL     ".M."
OPERADOR_NOT             ".N."
OPERADOR_OR              ".OU."
OPERADOR_PRODUTO         "*"
OPERADOR_SUBTRACAO       "-"
PROGRAMA                 "PROGRAMA"
SE                       "SE"
TIPO_CADEIA              "CADEIA"
TIPO_CARACTER            "CARACTER"
TIPO_INTEIRO             "INTEIRO"
TIPO_LISTA_INT           "LISTA_INT"
TIPO_LISTA_REAL          "LISTA_REAL"
TIPO_REAL                "REAL"
VIRGULA                  ","
DIGITO                   ([0-9])
CONSTANTE_INTEIRA        ({DIGITO}+)
CONSTANTE_REAL           ({DIGITO}+","%{DIGITO}+)
LETRA                    ([a-zA-Z])
PALAVRA                  ([a-zA-Z_-])
VARIAVEL                 ({LETRA}({PALAVRA}|{CONSTANTE_INTEIRA})*)
VARIAVEL_LISTA           ({VARIAVEL}"["({VARIAVEL}|{CONSTANTE_INTEIRA})"]")
CADEIA                   (\'[^'\r\n]+\')
COMENTARIO               (\{.*\})

%%

{ABRE}                     { printf("ABRE\n"); }
{ENQUANTO}                 { printf("ENQUANTO\n"); }
{ENTAO}                    { printf("ENTAO\n"); }
{ESCREVA}                  { printf("ESCREVA\n"); }
{FECHA}                    { printf("FECHA\n"); }
{FIM_ENQUANTO}             { printf("FIM_ENQUANTO\n"); }
{FIM_SE}                   { printf("FIM_SE\n"); }
{FIM}                      { printf("FIM\n"); }
{INICIO}                   { printf("INICIO\n"); }
{LEIA}                     { printf("LEIA\n"); }
{OPERADOR_ADICAO}          { printf("OPERADOR_ADICAO\n"); }
{OPERADOR_AND}             { printf("OPERADOR_AND\n"); }
{OPERADOR_ATRIBUICAO}      { printf("OPERADOR_ATRIBUICAO\n"); }
{OPERADOR_DIVISAO}         { printf("OPERADOR_DIVISAO\n"); }
{OPERADOR_IGUAL}           { printf("OPERADOR_IGUAL\n"); }
{OPERADOR_MENOR_IGUAL}     { printf("OPERADOR_MENOR_IGUAL\n"); }
{OPERADOR_NOT}             { printf("OPERADOR_NOT\n"); }
{OPERADOR_OR}              { printf("OPERADOR_OR\n"); }
{OPERADOR_PRODUTO}         { printf("OPERADOR_PRODUTO\n"); }
{OPERADOR_SUBTRACAO}       { printf("OPERADOR_SUBTRACAO\n"); }
{PROGRAMA}                 { printf("PROGRAMA\n"); }
{SE}                       { printf("SE\n"); }
{TIPO_CADEIA}              { printf("TIPO_CADEIA\n"); }
{TIPO_CARACTER}            { printf("TIPO_CARACTER\n"); }
{TIPO_INTEIRO}             { printf("TIPO_INTEIRO\n"); }
{TIPO_LISTA_INT}           { printf("TIPO_LISTA_INT\n"); }
{TIPO_LISTA_REAL}          { printf("TIPO_LISTA_REAL\n"); }
{TIPO_REAL}                { printf("TIPO_REAL\n"); }
{VIRGULA}                  { printf("VIRGULA\n"); }
{CONSTANTE_INTEIRA}        { printf("CONSTANTE_INTEIRA\n"); }
{CONSTANTE_REAL}           { printf("CONSTANTE_REAL\n"); }
{VARIAVEL}                 { printf("VARIAVEL\n"); }
{VARIAVEL_LISTA}           { printf("VARIAVEL_LISTA\n"); }
{CADEIA}                   { printf("CADEIA\n"); }
{COMENTARIO}               // Pula os trechos comentados
[ \t\r\n]+                 // Ignora espacos em branco, tabulações e quebras de linha
.                          { printf("ERRO\n"); } // Entrada não reconhecida
<<EOF>>                    { printf("$"); return 0; } // $ para indica o final da entrada

%%

int main() {
  yylex();
  return 0;
}