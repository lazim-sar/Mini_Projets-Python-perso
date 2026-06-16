# Le jeu de rôle (textuel) :

#Le but de ce projet est de créer un jeu de rôle
# Il y a un joueur et un ennemi.
# On commence tous les deux avec 50 PV
# Le joueur a 3 potions de vie et l'ennemi 0
# Chaque potion = aléatoire [15:50]
# Chaque tour, le joueur peux attaquer ou prendre une potion tandis que l'ennemi attaque automatiquement
# Le joueur_degat=aléatoire[5:10] || Ennemi= aléatoire[5:15]
# Lors qu'on utilise une potion , on passe le tour 

# Code du jeu de rôle si on veut alors respecter la consigne : 


from random import randint 

# On commence par inscrire les données qui serviront de base au jeu :
joueur_pv=50
ennemi_pv= 50 
joueur_potion=3
n=1
tour= n+1
print("*** Le Jeu de Rôle ***")
while True: 

# Et on va inscire le reste qui représente les données aléatoires qui seront à chaque fois différents à chaque tour :

    potion= randint(15,50)
    joueur_attaque= randint(5,10)
    ennemi_attaque= randint(5,15)

# On commence par directement tester la boucle selon le point de vie des 2 joueurs. Si ce cas est vrai alors la boucle s'arrête instantement.
    if ennemi_pv<=0:
        print("Tu as gagné 💪")
        print("Fin du jeu.")
        break
    elif joueur_pv<=0:
        print("Tu as perdu 😭")
        print("Fin du jeu.")
        break
     
     # Boucle pour s'assurer que l'utilisateur saisisse un nombre valide
    while True:
        try:
            choix_joueur=int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "))
            break
        except ValueError :
            continue
    
    # Maintenant, nous allons commencer par si l'utilisateur choisit l'option 1 

# Option 1- l'ATTAQUE:
    if choix_joueur==1:
        ennemi_pv= ennemi_pv-joueur_attaque
        joueur_pv= joueur_pv-ennemi_attaque
        
        if ennemi_pv >0 and joueur_pv >0:
            print(f"Vous avez infligé {joueur_attaque} points de dégats à l'ennemi ⚔️")
            print(f"L'ennemi vous a infligé {ennemi_attaque} points de dégats ⚔️ ")
            print(f"Il vous reste {joueur_pv} points de vie.")
            print(f"Il reste {ennemi_pv} points de vie à l'ennemi.")
        elif ennemi_pv <=0:
            print(f"Vous avez infligé {joueur_attaque} points de dégats à l'ennemi ⚔️")
        
        elif joueur_pv<=0:
             print(f"L'ennemi vous a infligé {ennemi_attaque} points de dégats ⚔️ ")
            
# L'option 2-Potion:

    elif choix_joueur ==2:
        if joueur_potion >0:
            ennemi_pv=ennemi_pv-0
            joueur_pv=joueur_pv + potion
            joueur_pv=joueur_pv-ennemi_attaque
            joueur_potion=joueur_potion-1
            print(f"Vous récupérez {potion} points de vie ❤️  ({joueur_potion}🍹restantes)")
            print(f"L'ennemi vous a infligé {ennemi_attaque} points de dégats ⚔️")
            print(f"Il vous reste {joueur_pv} points de vie.")
            print(f"Il reste {ennemi_pv} points de vie à l'ennemi.")
            print("-"*50)
            print("Vous passez votre tour...")
            ennemi_pv=ennemi_pv-0
            joueur_pv=joueur_pv-ennemi_attaque
            print(f"L'ennemi vous a infligé {ennemi_attaque} points de dégats ⚔️")
            print(f"Il vous reste {joueur_pv} points de vie.")
            print(f"Il reste {ennemi_pv} points de vie à l'ennemi.")
        
        else: # Quand il y a plus de potion
            print("Vous n'avez plus de potions... ")
            continue
    
    # Gestion des choix invalides
    else: 
        continue

    
    
    
    print("-"*50)



