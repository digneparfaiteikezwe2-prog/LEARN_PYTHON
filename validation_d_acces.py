username='admin'
password=1234
username=input("entrer le nom de l'utilisateur:")
password=int(input("entrer mot de passe:"))
if username=='admin':
    print("le compte t'appartient")
else:
    print("tu n'es pas admin")
if password==1234:
    print("mot de passe correct")
else:
    print("mot de passe incorrect")

