a=b="" # cela signifie : chaine de caractère vides

while not(a.isdigit() and b.isdigit()):
    a=input("\nEntrez un premier nombre : ")
    b=input("Entrez un deuxieme nombre: ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")
else: 
    print(f"\vLe résultat de l'addition de {a} avec {b} est égal à {int(a)+int(b)}")
    
help( True)