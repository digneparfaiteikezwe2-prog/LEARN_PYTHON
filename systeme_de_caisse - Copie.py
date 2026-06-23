riz=2000
sucre=1500
huile=5000

produit=input("entrer le produit:")
quantite=float(input("entrer la quantite:"))
if produit=='riz':
    total=2000*quantite
    print(f"total={2000*quantite}")
    if total>10000:
        print(f"total devient{2000*quantite*10/100}")
elif produit=='sucre':
    total=1500*quantite
    print(f"total={1500*quantite}")
    if total>10000:
       print(f"total devient{1500*quantite*10/100}")
elif produit=='huile':
    total=5000*quantite
    print(f"total={5000*quantite}")
    if total>10000:
       print(f"total devient{5000*quantite*10/100}")