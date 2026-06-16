# Le nombre mystère: Générons un nombre aléatoire entre 0 et 100.

import random as r
nombre_mystère= r.randint(0,100)
print("*** Le jeu du nombre mystère ***")

# Pour faire un compte à rebours de 5 à 0, tu peux utiliser range(5, -1, -1).

for k in range(5, -1, -1):
# Le premier argument (5) est la valeur de départ.
# Le second argument (-1) indique jusqu'où aller (exclu de la séquence).
# Le troisième argument (-1) indique qu'on veut descendre par pas de -1 (décroissant).
    
    # Vérification si les essais sont épuisés avant de demander un nouveau nombre
    if k==0:
        print(f"Dommage ! Le nombre mystère était {nombre_mystère}")
        print("Fin du jeu.")
        break
    


        
# L'affichage du jeu 
    print(f"Il te reste {k} essais")
    
    # Boucle pour s'assurer que l'utilisateur saisisse un nombre valide
    while True:
        try:
            nombre_choisi = int(input("Devine le nombre : "))
            break  # Si la saisie est correcte, on sort de la boucle while
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            print(f"Il te reste {k} essais")
            # Ne pas diminuer k, simplement redemander la saisie

    if nombre_choisi < nombre_mystère :
        print(f"Le nombre mystère est plus grand que {nombre_choisi}")
    elif nombre_choisi> nombre_mystère:
        print(f"Le nombre mystère est plus petit que {nombre_choisi}")
    elif nombre_choisi==nombre_mystère:
        print(f"Bravo ! Le nombre mystère était bien {nombre_mystère} !")
        print(f"Tu as trouvé le nombre en {5-k+1} essai(s) ") # utilisation du compteur 5 - k + 1 pour afficher le nombre d'essais restants lors de la victoire :
        # Cette formule calcule le nombre d'essais qu'il a fallu à l'utilisateur pour trouver le nombre mystère.
        print("Fin du jeu.")
        break
    
        
    print("-"*50) # = Séparer les differentes iterations de la boucles    






