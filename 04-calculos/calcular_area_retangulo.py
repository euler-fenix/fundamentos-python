'''
Crie um programa que define uma função

calcular_area_retangulo que recebe dois argumentos,
comprimento e largura de um retângulo, e retorna a
área desse retângulo.
Em seguida, o programa deve
solicitar ao usuário que insira o comprimento e a

largura e imprimir a área calculada.
'''



def calcular_area_retangulo (c, l):
    
    return  (c * l)
    # pass
  
   
c = float(input("Digite o comprimento: "))
l = float(input("Digite a largura : "))

area = calcular_area_retangulo(c, l)

print("A area do retangulo é: ",area)