# Créé par lazimsar, le 28/08/2024 en Python 3.7
# Nous allons créer une calculatrice dans le terminal avec Edupython.

# Avant de commencer à créer les variables, occupons nous de la gestion d'erreur.
# Commençons à rentrer les données:

while True:
       # Demander le premier nombre à l'utilisateur avec une boucle pour réessayer en cas d'erreur
        while True:
            try:
                a = int(input("Entrez le premier nombre : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    # Demander le second nombre à l'utilisateur avec une boucle pour réessayer en cas d'erreur
        while True:
            try:
                b = int(input("Entrez le second nombre : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
# Pour complexifier la calculatrice, nous allons permettre à l'utilisateur de choisir l'opération qu'il souhaite.
        while True:
            try:
        # Affichage du menu
                print("\nChoisissez parmi les modes d'opérations suivants :")
                print("1: Addition")
                print("2: Soustraction")
                print("3: Multiplication")
                print("4: Division")
                print("5: Quitter")
                utilisateur_choice =int(input("Entrez le numéro du mode d'opération voulu : "))
                if utilisateur_choice in [1,2,3,4,5]:
                    break
                else :
                    print("Choissisez un numéro valide.")

            except ValueError :
                print("Saisissez une opération valide.")


    # Option 1 : Addition
        if utilisateur_choice == 1:
            print(f"\nLe résultat de l'addition de {a} avec {b} est égal à {a + b}")
    # Option 2: Soustraction
        elif utilisateur_choice == 2:
            print(f"\nLe résultat de la soustraction de {a} avec {b} est égal à {a - b}")
    # Option 3: Multiplication
        elif utilisateur_choice == 3:
            print(f"\nLe résultat de la multiplication de {a} avec {b} est égal à {a * b}")
    # Option 4: Division
        elif utilisateur_choice == 4:
            try:
                print(f"\nLe résultat de la division de {a} avec {b} est égal à {a / b}")
            except ZeroDivisionError:
                print("\nErreur : Division par zéro impossible.")
    # Option 5: Quitter
        elif utilisateur_choice == 5:
            print("Arrêt forcé du programme...")
            break

    # Pour espacer les différentes lignes de codes et rendre le programme plus lisible
        print("-" * 50)

        continuer= input("Voulez vous continuer ? o/n ")
        if continuer!="o"and continuer !="O"and continuer !="Oui"and continuer !="oui":
            print("\nArret du programme...")
            break
