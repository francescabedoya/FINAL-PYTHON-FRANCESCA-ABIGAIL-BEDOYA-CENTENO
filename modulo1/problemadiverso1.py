p_2 = float(input("Ingrese la cantidad depositada en la cuenta de ahorros: ")) 
i = 0.04

for o in range(1,4):
    m = m * (1+i)
    print(f"El monto al final del año {o} es :{round(p_2,2)}")
    
