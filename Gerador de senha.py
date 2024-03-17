import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem Vindo(a) ao Gerador de Senha Segura!")
nr_letras= int(input("\nQuantas letras você deseja em sua senha ? ")) 
nr_simbolos = int(input("\nQuantos símbolos você deseja em sua senha ? "))
nr_numeros = int(input("\nQuantos números você deseja em sua senha ? "))

tamanho = nr_letras + nr_simbolos + nr_numeros
senha = ""

while len(senha) < tamanho:
    sorteio = random.randint(0, 2)
  
    if nr_letras > 0 and sorteio == 0:
      senha += random.choice(letras)
      nr_letras -= 1
      continue
        
    elif nr_simbolos > 0 and sorteio == 1:
      senha += random.choice(simbolos)
      nr_simbolos -= 1
      continue
           
    elif nr_numeros > 0 and sorteio == 2:
      senha += random.choice(numeros)
      nr_numeros -= 1
      continue
  

print(f"\nSua senha é: {senha}")


