def isInt(value):
    try:
        int(value)
        return True
    except:
        return False

def primoslinear(x):
    
    if isInt(x) == False:
        return "Digite apenas números inteiros maiores a 1"    
    elif int(x) <= 1:
        return "Digite apenas números inteiros maiores a 1"
    else:
        
        "Usando crivo de Erastóstenes como base"
        
        x = int(x)
        primos = list(range(2, x))
        for j in range(2, x+1):
            for k in primos:
                if k%j == 0  and j != k:
                    primos.remove(k)
                    
        return primos

while True:
    print(primoslinear(input("Insira o número: ")))