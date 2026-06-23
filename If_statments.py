#if statment
#age=input("entrer l'age del'utilisateur:")
#if age<=20:
#    print(f"tu es mature")
#else:
#    print(f"t'es adulte")
#
#calculatrice
a=float(input("entrer le valeur de a:"))
b=float(input("entrer la valeur de b:"))
op=input("entrer l'operation:")
if op=='+':
    print(f"l'addition de a et b est :{a+b}")
elif op=='-':
    print(f"la soustraction de a et b est:{a-b}")
elif op=='*':
    print(f"la multiplication de a et b est:{a*b}")
elif op=='/':
    if b!=0:
        print(f"la division de a et b est :{a/b}")
    else:
        print("impossible")


