
notes=float(input("veuillez saisir le note:"))
if notes>100:
    print("notes invalide")
elif notes<=50:
    print("echec")
elif notes<=60:
    print("passable")
elif notes<=70:
    print(" assez bien")
elif notes<=80:
    print("bien")
elif notes>80:
    print("excellent")
