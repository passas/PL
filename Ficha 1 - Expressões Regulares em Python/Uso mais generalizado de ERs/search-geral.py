import re


#Definição que comporta a expressão regular -raw string- acerca da forma como queremos apanhar/capturar o conteúdo de uma linha
expressao_regular_1 = r'padrão'
expressao_regular_2 = r'^(PRH|JCR)'
expressao_regular_3 = r'^[0-9]+' #r'^\d+'
expressao_regular_4 = r''
expressao_regular_5 = r''
expressao_regular_6 = r''
expressao_regular_7 = r''
expressao_regular_8 = r''
expressao_regular_9 = r''
expressao_regular_9_a = r''
expressao_regular_9_b = r''
expressao_regular_10 = r''
expressao_regular_11 = r''
expressao_regular_12 = r''



#Função que analisa um texto, linha a linha, à procura do primeiro padrão -re.search- que corresponda à expressão regular passada como parâmetro
def pesquisa(ER):

  #Lêr uma linha -stdin- e guardá-la num buffer -string-
  buffer_stdin = input(">> ")
  
  #Parar o ciclo se a linha fôr vazia
  while buffer_stdin != "":

    #Procurar, na linha, a primeira ocorrência -re.search-, do(s) padrão(ões) definido(s) pela expressão regular (passada como parâmetro)
    resultado = re.search(ER, buffer_stdin)

    #-stdout-: Resultado da procura na linha
    print (resultado)

    #Lêr uma linha -stdin- e guardá-la num buffer -string-
    buffer_stdin = input(">> ")



#Main
if __name__ == '__main__':
  
  pesquisa (expressao_regular_3)
