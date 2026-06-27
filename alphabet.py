consonnes='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
voyelles="aiuoeAIUOE"
nb_consonnes=0
nb_voyelles=0
lettre='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZaiuoeAIUOE'
nom=(input("entrer le nom:"))
#while lettre in consonnes:
for lettre in nom:
  if lettre in consonnes:
    nb_consonnes+=1
    #print(len(f"{consonnes}"))
    #print("le nombre total de consonnes est:",nb_consonnes)
  elif lettre in voyelles:
    nb_voyelles+=1
print("le nombre total de voyelles est:",nb_voyelles)
print("le nombre total de consonnes est:",nb_consonnes)
    #print(len(f"{voyelles}"))


