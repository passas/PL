#Número de Aluno;Nome completo do Aluno;N1;N2;...;Nn

import re


#Definição que comporta a expressão regular -raw string- acerca da forma como queremos apanhar/capturar o conteúdo de uma linha
separador_csv = r';'


#Main
if __name__ == '__main__':

  #Lêr uma linha -stdin- e guardá-la num buffer -string-
  buffer_stdin = input(">> ")
  
  #Parar o ciclo se a linha fôr vazia
  while buffer_stdin != "":

    #Procurar o caractér delimitador de csv -;-, e partir, a linha, no máximo -2- vezes aquando do encontro da expressão regular do delimitador -;- da linha CSV
    campos_aluno = re.split(separador_csv, buffer_stdin, maxsplit=2)
    #Individualizar as notas do aluno numa lista
    notas_aluno = re.split(separador_csv, campos_aluno[2])

    '''Tratar da média do aluno'''
    #Iniciar a soma a zero
    soma = 0
    #Percorrer as notas do aluno
    for nota in notas_aluno:
      #Somar a nota ao valor total das notas do aluno
      soma += float (nota)
    #Fazêr a média ponderada do aluno
    media = soma / len (notas_aluno)


    #-stdout-: Resultado de processar a linha do Aluno
    print (f"Número de Aluno: {campos_aluno[0]}")
    print (f"Nome do Aluno: {campos_aluno[1]}")
    print (f"Média do Aluno: {media:.2f}") #formatar float: duas casas decimais


    #Lêr uma linha -stdin- e guardá-la num buffer -string-
    buffer_stdin = input(">> ")
