def demander_nombre(message):
    """Demande un nombre entier strictement supérieur à 0."""
    while True:
        try:
            n = int(input(message))
            if n <= 0:
                print("\nCe nombre n'est pas accepté. Mets un vrai nombre chef.")
                continue
            return n
        except ValueError:
            print("\nVasy mets un vrai nombre chef et arrête de me faire perdre du temps avec tes lettres.")

def boucle_multiplication(i, multiplicateur):
    """Multiplie i par le multiplicateur jusqu'à dépasser 1000, et compte les répétitions."""
    n = 0
    print(f"\nPour rappel, vous avez opté pour le nombre {i}")
    print(f"Voyons voir jusqu'à ce que la boucle atteigne 1000 avec un multiplicateur choisi !")

    while i < 1000:
        i *= multiplicateur
        n += 1
        print(f"\ni = {i}, n = {n} → Continuons !")

    print(f"\nLa boucle s'est répétée {n} fois pour arriver à plus de 1000.")

# --- Programme principal ---
i = demander_nombre("Entrez un nombre i supérieur à 0 : ")
multiplicateur = demander_nombre("Choisissez maintenant un multiplicateur strictement supérieur à 0 : ")
boucle_multiplication(i, multiplicateur)
