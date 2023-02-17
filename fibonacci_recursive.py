def isInt(value):
    try:
        int(value)
        return True
    except:
        return False

def fibonacci(x):
    if isInt(x) == False:
        return "Digite apenas números inteiros maiores ou iguais a 0"    
    elif int(x) < 0:
        return "Digite apenas números inteiros maiores ou iguais a 0"
    else:
        x = int(x)
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            
            "Definição da função recursiva de fibonacci"
            
            return (fibonacci(x-1)+fibonacci(x-2))

while True:
    print(fibonacci(input("Insira o número: ")))