import re


#Definição que comporta a expressão regular -raw string- acerca da forma como queremos apanhar/capturar o conteúdo de uma linha
expressao_regular = r'[Hh][Ee][Ll]{2}[Oo]'
#expressao_regular = r'(?i:hello)'


#Main
if __name__ == '__main__':

  #Lêr uma linha -stdin- e guardá-la num buffer -string-
  buffer_stdin = input(">> ")
  
  #Parar o ciclo se a linha fôr vazia
  while buffer_stdin != "":

    #Pesquisar todas as ocorrências, na linha, relativas à expressão regular e guardá-las numa lista
    lista_resultados = re.findall(expressao_regular, buffer_stdin) #[heLlO, hello, ...]
    
    #Encontrei a expressão regular na linha
    if(lista_resultados):
      
      #Extraír o número de expressões capturadas na linha
      len(lista_resultados)


    #-stdout-: Resultado que foi instanciado através da tentativa de captura
    print (lista_resultados)

    
    #Lêr uma linha -stdin- e guardá-la num buffer -string-
    buffer_stdin = input(">> ")
