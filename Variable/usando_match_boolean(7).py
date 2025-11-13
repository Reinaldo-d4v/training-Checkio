# Taken from mission Just Fizz!

# Função principal que recebe um número inteiro
def checkio(num: int):
    
    # permite comparar padrões(match)
    # há uma tupla com dois valores booleanos:
    # - O primeiro elemento será True se o número for divisível por 3.
    # - O segundo elemento será True se o número for divisível por 5.
    match (num % 3 == 0, num % 5 == 0):

        case (True, True):
            return 'Fizz Buzz'
  
        case (True, False):
            return 'Fizz'

        case (False, True):
            return 'Buzz'
        # "_" é um curinga que captura qualquer outro padrão
        case _:
            # Retorna o número convertido em string
            return str(num)

# Teste simples: número 7 não é divisível por 3 nem por 5
print(checkio(7))

print("Example:")
# Exemplo: número 15 → divisível por 3 e por 5
print(checkio(15))

# self-checks
assert checkio(15) == "Fizz Buzz"  
assert checkio(6) == "Fizz"        
assert checkio(10) == "Buzz"       
assert checkio(7) == "7"         

print("The mission is done! Click 'Check Solution' to earn rewards!")
