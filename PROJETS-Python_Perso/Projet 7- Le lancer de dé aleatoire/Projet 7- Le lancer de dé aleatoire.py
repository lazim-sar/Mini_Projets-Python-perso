from random import randint


def lancer_dé_aléatoire():
    dé1=randint(1,6)
    dé2=randint(1,6)
    n=0
    while dé1!=dé2:
        dé1=randint(1,6)
        dé2=randint(1,6)
        n+=1
        print(f"Le premier dé tombe sur {dé1} ")
        print(f"Le deuxième dé tombe sur {dé2}")
        print("-"*50)
        if dé1==dé2:
            print(f"Bien ouej,les dé 1 et 2 sont tombés sur {dé1}")
            print(f"Vous avez lancé {n} fois les dé 1 et 2")
            break       
        
        continuer=input("Voulez vous continuer ? (o/n)\nVotre choix 👉: ")
        if continuer!="o"and continuer !="O"and continuer !="Oui"and continuer !="oui":
            print("Vous avez decidé d'arrêter de lancer les 2 dé. ")
            print(f"Vous avez lancé {n} fois les dé 1 et 2")
            break
        else:
            print("-"*50)
    
    return(lancer_dé_aléatoire)

    
fonction_dé= lancer_dé_aléatoire()
print(fonction_dé)   

while True:
    try:
        print("-"*50) 
        choix_réessayer=int(input("Souhaitez vous réeesayer le programme ?\n1.Réessayer\n2.Quitter \nVotre choix 👉 : "))
        if choix_réessayer==1:
            lancer_dé_aléatoire()
        elif choix_réessayer==2:
            print("Vous avez decidé de quitter.\vArrêt du programme...")
            break
        else: 
            print("Choissisez un nombre valide.")
            continue
    except ValueError: 
        print("Arrête de faire le con et entre un nombre valide...")
        continue
    
    
    
