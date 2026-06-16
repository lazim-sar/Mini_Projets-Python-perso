from random import randint

number_to_find=randint(0,100)
remaining_attempts=5

print("***Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attempts>0:
    print(f"Il te reste {remaining_attempts} essai{'s' if remaining_attempts > 1 else ''}")# On a fait une opération ternaire ( On rajoute un "s" si l'essai est > 1.)

    # Saisie de l'utilisateur
    user_choice=input("Devine le nombre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide.")
        continue
    
    # Convertir le nombre !!
    user_choice=int(user_choice) # Pour comparer des nombres, il faut qu'il soit du même type !
    
    if number_to_find>user_choice: # Plus grand
        print(f"Le nombre mystère est plus grand que {user_choice}")
    
    elif number_to_find<user_choice: # Plus petit
        print(f"Le nombre mystère est plus petit que {user_choice}")

    else: # Egal (succès)
        break
    
    remaining_attempts= remaining_attempts-1 # Ou on peut écrire remaining_attempts -=1

# Gagné ou perdu 
if remaining_attempts ==0:
    print(f"Dommage ! Le nombre mystère était {number_to_find} !")
else: 
    print(f"Bravo ! Le nombre mystère était bien {number_to_find} !")
    print(f"Tu as trouvé le nombre en {6-remaining_attempts} essai{'s'if remaining_attempts>1 else ''}")
print("Fin du jeu")