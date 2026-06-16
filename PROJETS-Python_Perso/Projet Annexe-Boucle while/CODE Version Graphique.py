# On importe la bibliothèque tkinter pour créer l'interface graphique
import tkinter as tk
from tkinter import messagebox  # Pour afficher des fenêtres d'erreur

# Fonction pour récupérer et valider le premier nombre
def demander_nombre():
    try:
        # On récupère le texte entré par l'utilisateur et on le convertit en entier
        i = int(entry_nombre.get())

        # Si le nombre est inférieur ou égal à 0, on déclenche une erreur volontairement
        if i <= 0:
            raise ValueError

        # Si tout est bon, on retourne le nombre
        return i
    except ValueError:
        # Si une erreur survient (texte non convertible ou nombre <= 0), on affiche une alerte
        messagebox.showerror("Erreur", "Entrez un nombre entier strictement supérieur à 0.")
        return None  # On retourne None pour indiquer que la saisie est invalide

# Fonction pour récupérer et valider le multiplicateur
def demander_multiplicateur():
    try:
        # On récupère le texte entré et on le convertit en entier
        m = int(entry_multiplicateur.get())

        # On vérifie que le multiplicateur est strictement supérieur à 0
        if m <= 0:
            raise ValueError

        return m
    except ValueError:
        # Si la saisie est invalide, on affiche une alerte
        messagebox.showerror("Erreur", "Entrez un multiplicateur strictement supérieur à 0.")
        return None

# Fonction principale qui lance la boucle de multiplication
def lancer_boucle():
    # On récupère les deux valeurs saisies
    i = demander_nombre()
    m = demander_multiplicateur()

    # Si l'une des deux est invalide, on arrête la fonction
    if i is None or m is None:
        return

    # Initialisation du compteur de répétitions
    n = 0
    resultats = ""  # Chaîne pour stocker les résultats à afficher

    # Boucle : on multiplie i par m jusqu'à ce que i dépasse 1000
    while i < 1000:
        i *= m
        n += 1
        resultats += f"i = {i}, n = {n}\n"  # On ajoute le résultat à la chaîne

    # On ajoute le message final
    resultats += f"\nLa boucle s'est répétée {n} fois pour arriver à plus de 1000."

    # On affiche les résultats dans la zone de texte
    text_resultat.delete("1.0", tk.END)  # On efface le contenu précédent
    text_resultat.insert(tk.END, resultats)  # On insère les nouveaux résultats

# --- Interface graphique ---

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Multiplicateur jusqu'à 1000")  # Titre de la fenêtre

# Champ pour entrer le premier nombre
tk.Label(fenetre, text="Entrez un nombre supérieur à 0 :").pack()
entry_nombre = tk.Entry(fenetre)
entry_nombre.pack()

# Champ pour entrer le multiplicateur
tk.Label(fenetre, text="Entrez un multiplicateur supérieur à 0 :").pack()
entry_multiplicateur = tk.Entry(fenetre)
entry_multiplicateur.pack()

# Bouton pour lancer la boucle
tk.Button(fenetre, text="Lancer la boucle", command=lancer_boucle).pack()

# Zone de texte pour afficher les résultats
text_resultat = tk.Text(fenetre, height=10, width=50)
text_resultat.pack()

# Lancement de la boucle principale de l'interface (affiche la fenêtre)
fenetre.mainloop()
