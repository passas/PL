import re


#Definição que comporta a expressão regular -raw string- acerca da forma como queremos apanhar/capturar o conteúdo de uma linha
expressao_regular = r','


#Main
if __name__ == '__main__':

  #Lêr uma linha -stdin- e guardá-la num buffer -string-
  buffer_stdin = input(">> ")
  
  #Parar o ciclo se a linha fôr vazia
  while buffer_stdin != "":

    #Procurar, e partir, a linha, no local onde a expressão regular é encontrada e guardar o resultado numa lista -string-
    lista_resultado = re.split(expressao_regular, buffer_stdin)
    
    #Percorrer a lista de resultados obtidos
    for string in lista_resultado:      
      #-stdout-: Resultado -string- de partir a linha nas expressões regulares encontradas
      print (string)


    #Lêr uma linha -stdin- e guardá-la num buffer -string-
    buffer_stdin = input(">> ")
