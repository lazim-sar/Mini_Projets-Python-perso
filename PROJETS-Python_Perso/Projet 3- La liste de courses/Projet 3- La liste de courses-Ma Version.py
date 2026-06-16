# Je dois rédiger un programme qui pourra faire une liste de course
# En utilisant les listes, l'utilisateur aura plusieurs fonctionnalité parmi 5 options.
# Selon l'option choisi, la liste devra réagir de manière differente.
# La liste de course devra fonctionner tant que la boucle n'est pas fini.
# Initialisation de la liste de courses
liste = []

# Boucle principale du programme
while True:
    # Affichage du menu
    print("\nChoisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")
    
    # Saisie de l'option choisie par l'utilisateur
    try:
        liste2course = int(input("👉 Votre choix : "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue
    
    # Option 1 : Ajouter un élément à la liste
    if liste2course == 1:
        ajouter = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(ajouter)
        print(f"L'élément '{ajouter}' a bien été ajouté à la liste.")

    # Option 2 : Retirer un élément de la liste
    elif liste2course == 2:
        retirer = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if retirer in liste:
            liste.remove(retirer)
            print(f"L'élément '{retirer}' a bien été retiré de la liste.")
        else:
            print(f"L'élément '{retirer}' n'est pas dans la liste.")

    # Option 3 : Afficher la liste
    elif liste2course == 3:
        if liste:
            print("Voici le contenu de votre liste de courses :")
            for i, item in enumerate(liste, 1):
                print(f"{i}. {item}")
        else:
            print("Votre liste est vide.")

    # Option 4 : Vider la liste
    elif liste2course == 4:
        liste.clear()
        print("La liste a été vidée.")

    # Option 5 : Quitter le programme
    elif liste2course == 5:
        print("À bientôt !")
        break

    # Gestion des choix invalides
    else:
        print("Choix invalide, veuillez choisir une option entre 1 et 5.")

    print("-"*50) # = Séparer les differentes iterations de la boucles    