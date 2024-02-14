import re


#Definição que comporta a expressão regular -raw string- acerca da forma como queremos apanhar/capturar o conteúdo de uma linha
expressao_regular = r'[Hh][Ee][Ll]{2}[Oo]'
#expressao_regular = r'(?i:hello)'

#Definição que comporta a palavra -string- substituta
string_substituta = '*YEP*'


#Main
if __name__ == '__main__':

  #Lêr uma linha -stdin- e guardá-la num buffer -string-
  buffer_stdin = input(">> ")
  
  #Parar o ciclo se a linha fôr vazia
  while buffer_stdin != "":

    #Procurar, e substituir, todas as ocorrências, na linha, relativas à expressão regular e guardar o resultado numa variável -string-
    string_resultado, n_capturas = re.subn(expressao_regular, string_substituta, buffer_stdin)
    
    #Encontrei, e substituí, a expressão regular na linha
    if(n_capturas > 0):
      
      #-stdout-: Resultado -string- da substituição das expressões encontradas
      print (string_resultado)


    #Lêr uma linha -stdin- e guardá-la num buffer -string-
    buffer_stdin = input(">> ")
