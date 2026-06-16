# Créé par lazimsar, le 29/08/2024 en Python 3.7
# Nous allons créer une calculatrice dans le terminal avec Edupython.

# Avant de commencer à créer les variables, occupons-nous de la gestion d'erreur.

while True:

     # Ceci est la première façon de faire

    # Affichage du menu
        print("\nChoisissez parmi les modes d'opérations suivants :")
        print("1: Addition")
        print("2: Soustraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Quitter")

        try:
            utilisateur_choice = int(input("Entrez le numéro du mode d'opération voulu : "))
            if utilisateur_choice not in [1, 2, 3, 4, 5]:
                print("Saisissez un numéro valide.")
                continue
        except ValueError:
            print("Saisissez une opération valide.")
            continue

        if utilisateur_choice == 5:
            print("Arrêt du programme...")
            break

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

    # Effectuer l'opération choisie
        if utilisateur_choice == 1:
            print(f"\nLe résultat de l'addition de {a} avec {b} est égal à {a + b}")
        elif utilisateur_choice == 2:
            print(f"\nLe résultat de la soustraction de {a} avec {b} est égal à {a - b}")
        elif utilisateur_choice == 3:
            print(f"\nLe résultat de la multiplication de {a} avec {b} est égal à {a * b}")
        elif utilisateur_choice == 4:
            try:
                print(f"\nLe résultat de la division de {a} avec {b} est égal à {a / b}")
            except ZeroDivisionError:
                print("\nErreur : Division par zéro impossible.")
        print("-" * 50)


        continuer= input("Voulez vous continuer ? o/n ")
        if continuer!="o"and continuer !="O"and continuer !="Oui"and continuer !="oui":
            print("\nArret du programme...")
            break

    # Espacer les différentes opérations pour plus de lisibilité

