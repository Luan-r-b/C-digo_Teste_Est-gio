def isInt(value):
    try:
        int(value)
        return True
    except:
        return False
    
def fibonaccilinear(x):
    
    fib0 = 0
    fib1 = 1
    
    if isInt(x) == False:
        return "Digite apenas números inteiros maiores ou iguais a 0"    
    elif int(x) < 0:
        return "Digite apenas números inteiros maiores ou iguais a 0"
    else:
        x = int(x)
        if x == 0:
            return fib0
        elif x == 1:
            return fib1
        else:
            for k in range(1,x):
                
                "É utilizado variável auxiliar para troca de valores"
                
                fibtemp = fib0 + fib1
                fib0 = fib1
                fib1 = fibtemp
                
            return fib1
               
while True:
    print(fibonaccilinear(input("Insira o número: ")))