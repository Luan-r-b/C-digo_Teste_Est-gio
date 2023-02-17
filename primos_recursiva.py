def isInt(value):
    try:
        int(value)
        return True
    except:
        return False

def primosrecursiva(x):
    
    if isInt(x) == False:
        return "Digite apenas números inteiros maiores a 1"
    
    elif int(x) <= 1:
        return "Digite apenas números inteiros maiores a 1"
    
    elif int(x) == 2:
        if x == 2:
            return [2]
    else:
        
        x = int(x)
        
        primos = primosrecursiva(x-1)
        
        "Recursividade vai gerar primos retroativamente até o 2"
        
        if all(x % k != 0 for k in primos):
        
        "Verificação de cada função desencadeada se é divisível por algum primo gerado anteriormente"
        
            primos.append(x)
        
        return primos
                    
while True:
    print(primosrecursiva(input("Insira o número: ")))