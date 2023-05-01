def is_prime(num):#função para testar se o número é primo
    cont=0
    for i in range(1,100):
        if num%i==0:
            cont+=1
          
    if cont==2:
        return True
    else:
        return False

print("Os numeros primos no intervalo de 1 à 100 são:\n")#mostrando       
for i in range(1, 100):
	if is_prime(i):
	    print(i, end=" ")
