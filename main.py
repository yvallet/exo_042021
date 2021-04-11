"""
  EXO  2021         sequence de commentaires avec triple quote 12H00

type(var) ==> type de la variable
  str, int, float, boolean
var_alpha = str(var_num)
var_num = int(var_alpha)

###### local et global ##################
var=1

def my_fonction()
global var
var += 1
## pas besoin de return

my_fonction()
## ==> var = 2

"""

import turtle
import random


# =================================================== exo 1   test age ==============================================

def saisie_age(v_nom):
    v_num = 0
    while v_num == 0:
        v_alf = input("quel est l'age de " + v_nom + "? : ")
        try:
            v_num = int(v_alf)
        except:
            print("l age doit etre numerique !!")

    return v_num


def saisie_nom(mini, maxi):
    long = 0
    alpha = ""
    while long == 0:
        alpha = input("quel est ton nom ? ")
        long = len(alpha)
        if (mini == 0) and (long == 0):
            break
        if mini > 0:
            if long < mini:
                print("zone oblogatoire")
                long = 0
        if long > maxi:
            print("Trop long : " + str(maxi) + " maximum")
            long = 0

        if long < mini:
            print("il faut informer un nom avec " + str(mini) + " car minimum!)")
            long = 0
    return alpha

#                         Param optionnel , si pas garni ==> 0,  si garni=> normal
def afficher( xnom, xage, taille=0):
    print("je suis " + xnom + " et j'ai l'age canonique de " + str(xage) + " ans")
    print("l annee prochaine vous aurez : " + str(xage+1))
    print()
    majeur = xage >= 18
    print("variable majeur : ", majeur)
    if xage == 1 or xage == 2:
        print("vous etes BEBE")
    elif 10 < xage < 15:
        print("Adolecent")
    elif xage <=10:
        print("un enfant !!!")
    elif xage == 17:
        print("bientot majeur")
    elif xage == 18:
        print("majorite atteinte")
    elif xage > 60:
        print("vous etes SENIOR")
    elif majeur:
        print("zetes un vieux Majeur")
    else:
        print("vous etes un Minot")

    if not taille == 0:
        print("taille : " + str(taille))

"""
nom1 = saisie_nom(0, 10)
age_num1 = saisie_age()
afficher(nom1, age_num1)

nom2 = saisie_nom(0, 10)
age_num2 = saisie_age()
afficher(nom2, age_num2)
"""

NB_PERSONNE = 3                    ## convention : constante immuable en MAJ

for i in range(0, NB_PERSONNE):    ## 0 Inclus  NB Exclus
    nom = "personne No " + str(i+1)
    age = saisie_age(nom)
    afficher(nom, age)

## avec une taille

afficher(nom, age, 1.72)

## Chaine formatée
print ("************* formattage ***********")
print("je suis " + nom + " et j'ai l'age de " + str(age) + " ans")

print (f"je suis {nom} et j'ai l'age de {age} ans")
print ("je suis %s et j'ai L'age de %s ans" % (nom, age))

##texte multi-ligne
print("""
ligne 1
        ligne 2
               ligne 3
""")

print("fin test1  age ")
# =====================================================================================================================
#    exo tortue
#import turtle

rep = input ("executer turtle O/N ")

if rep == "O" or rep == "o":

    t = turtle.Turtle()

    """"
    t.forward(30)
    t.left(45)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.forward(30)
    t.left(90)
    t.forward(30)
    """


    def escalier(long, nb):
        for i in range(0, nb):
            t.forward(long)
            t.left(90)
            t.forward(long)
            t.right(90)

        t.forward(long)


    # escalier(40, 6)

    def carre(cote):
        for i in range(0, 4):
            t.forward(cote)
            t.left(90)


    def carre_multiple(taille, nbr):
        for i in range(0, nbr):
            cote = (i + 1) * taille
            carre(cote)


    # carre(100)

    carre_multiple(30, 5)

    turtle.done()

print ("fin turtle")

# ==================================================================================================================
#     nombre magique a deviner
# exercice nbre_magique   maj pour test git 17 hres

# import random
rep = input ("executer Nbre magique O/N ")
if rep == "O" or rep == "o":

    MINI = 1
    MAXI = 20
    ESSAI = 5
    NBR_CHERCHE = random.randint(MINI, MAXI)


    def saisie(mini, maxi):
        nb = 0
        while nb == 0:
            # nbre = input ("saisir un nbre entre " + str(mini) + " et " + str(maxi) + " : ")
            nbre = input(f"saisir un nbre entre {mini}  et {maxi}  : ")

            try:
                nb = int(nbre)
            except ValueError:
                print("valeur invalide")
                nb = 0

            if nb < mini or nb > maxi:
                # print("SVP un nbre entre " + str(mini) + " et " + str(maxi) + " : ")
                print(f"SVP un nbre entre {mini} et {maxi} : ")

                continue
            break
        return nb


    print(f"Nbre magique , vous avez droit a  {ESSAI} essais")

    essai = 1

    while True:
        print(f"essai numero {essai}/{ESSAI}")
        nbre_saisi = saisie(MINI, MAXI)
        # print ("saisi: " + str(nbre_saisi) + "cherchÃ©: " + str(NBR_CHERCHE))

        if nbre_saisi == NBR_CHERCHE:
            print("Gagne !!!!!!!!!!!!")
            break

        essai += 1
        if essai > ESSAI:
            print("Perdu !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"il fallait trouver {NBR_CHERCHE}")
            break
        else:
            if nbre_saisi > NBR_CHERCHE:
                print("Trop Grand")
            else:
                print("Trop petit")

    # Le meme avec boucle FOR
    print("=============== BOUCLE =================")
    gagne = False
    essai = 1

    for i in range(0, ESSAI):
        print(f"essai numero {essai}/{ESSAI}")
        nbre_saisi = saisie(MINI, MAXI)
        if nbre_saisi == NBR_CHERCHE:
            gagne = True
            break

        essai += 1
        if nbre_saisi > NBR_CHERCHE:
            print("Trop Grand")
        else:
            print("Trop petit")

    if gagne:
        print("Gagne !!!!!!!!!!!!")
    else:
        print("Perdu !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"il fallait trouver {NBR_CHERCHE}")

print ("FIN nbre magique")




