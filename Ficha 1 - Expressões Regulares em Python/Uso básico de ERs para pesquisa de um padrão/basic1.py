import re


#Definição que comporta a expressão regular -raw string- acerca da forma como queremos apanhar/capturar o conteúdo de uma linha
expressao_regular = r'hello'


#Main
if __name__ == '__main__':

  #Lêr uma linha -stdin- e guardá-la num buffer -string-
  buffer_stdin = input(">> ")
  
  #Parar o ciclo se a frase -linha- fôr vazia
  while buffer_stdin != "":

    #Pesquisar a expressão regular na linha e guardar o resultado numa variável
    resultado = re.search(expressao_regular, buffer_stdin)
    
    #Encontrei a expressão regular na linha
    if(resultado):
      #Extraír a frase -linha- de onde foi encontrada a expressão regular
      resultado.string
      
      #Extraír o grupo capturado na frase -linha- através da expressão regular designada
      resultado.group()

      #Extraír índice, para um tuplo, de início e de fim, da captura da expressão regular na frase -linha-
      (inicio, fim) = resultado.span()
      #Calcular comprimento da captura
      comprimento = fim - inicio
    
    
    #-stdout-: Resultado que foi instanciado através da tentativa de captura
    print (resultado)

    
    #Lêr uma linha -stdin- e guardá-la num buffer -string-
    buffer_stdin = input(">> ")
