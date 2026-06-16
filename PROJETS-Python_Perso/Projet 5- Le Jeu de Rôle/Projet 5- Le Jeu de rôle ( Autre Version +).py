# Le Jeu de rôle ( Autre Version )
# Ce code est plutôt réalisé sur la chronologie du jeu de rôle.
import random

# On commence à saisir les élements qui servent de base au code:
ENEMY_HEALTH=50
PLAYER_HEALTH=50
NUMBER_POTIONS=3
SKIP_TURN= False

while True:
    # Jeu du joueur 
    if SKIP_TURN:
        print("Vous passez votre tour...")
        SKIP_TURN= False
    
    else:
        user_choice="" # Pour définir la variable au préalable et permettre à l'utilisateur d'entrer quelque chose.
        while user_choice not in ["1","2"]: # Pour s'assurer que l'utilisateur choissise bien entre l'option 1 ou 2.
            user_choice= input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")

        if user_choice=="1":# Attaque 
            your_attack=random.randint(5,10)
            ENEMY_HEALTH-=your_attack # Ce qui signifie en autre terme: ENEMY_HEALTH=ENEMY_HEALTH-your_attack
            print(f"Vous avez infligé {your_attack} points de dégats à l'ennemi ⚔️")

        elif user_choice=="2": # Potion  
            if NUMBER_POTIONS>0:
                potion_health=random.randint(15,50)
                PLAYER_HEALTH+=potion_health
                NUMBER_POTIONS-= 1
                SKIP_TURN= True
                print(f"Vous récupérez {potion_health} points de vie ❤️  ( {NUMBER_POTIONS} 🍹 restantes)")

            else: 
                print("Vous n'avez plus de potion...")
                continue

    if ENEMY_HEALTH <=0:
        print("Tu as gagné 💪")
        break

    # Attaque de l'ennemi 
    enemy_attack=random.randint(5,15)
    PLAYER_HEALTH-= enemy_attack
    print(f"L'ennemi vous a infligé {enemy_attack} points de dégats ⚔️")

    if PLAYER_HEALTH<=0:
        print("Tu as perdu 😭")
        break

# STATS:
    print(f"Il vous reste {PLAYER_HEALTH} points de vie.")
    print(f"Il reste {ENEMY_HEALTH} points de vie à l'ennemi.")
    print("-"*50)

print("Fin du jeu.")