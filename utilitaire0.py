"""Ce module contient les fonctions deplace, code_pos, libre_0, retrouve_position : ces fonctions fonctionnent"""

# ==============================================================================
from plateauechec0 import *
from entite0 import *
# ==============================================================================

def deplace(personnage) :
    """ Permet a perso de se deplacer d'une case """
    assert isinstance(personnage, perso), "Type perso incorrect"    # controle des types
    
    #var
    indiv=perso() #perso()

    #begin
    #Toutes les indormations contenues dans perso sont transferees dans indiv
    #...et donc seront retournees par la fontion.
    indiv.pos_lig=personnage.pos_lig
    indiv.pos_col=personnage.pos_col
    
    indiv.pos_deb_lig=personnage.pos_deb_lig
    indiv.pos_deb_col=personnage.pos_deb_col
    indiv.pos_0_lig=personnage.pos_0_lig
    indiv.pos_0_col=personnage.pos_0_col
    indiv.code=personnage.code
    
    pos=input("Ou vouler-vous deplacer le personnage :en haut(ecrire: h), en bas (ecrire: b), à gauche (ecrire :g), à droite (ecrire: d) ?  Puis appuyez sur la touche Entree. ")
    while pos not in "hbgd":
        #begin
        print("Le caractere que vous avez entré est incorrect...")
        pos=input("Ou vouler-vous deplacer le personnage:en haut(ecrire: h), en bas (ecrire: b), à gauche (ecrire :g), à droite (ecrire: d) ?  ")
        #end
    if pos=="h":
        indiv.pos_lig=indiv.pos_lig - 1
    elif pos=="b":
        indiv.pos_lig=indiv.pos_lig + 1
    elif pos=="d":
        indiv.pos_col=indiv.pos_col + 1
    else:
        indiv.pos_col=indiv.pos_col - 1
    return indiv
    #end

# ==============================================================================
def code_pos(code) :
    """ Donne la position 0 du hero a partir de son code (donc modifie les deux derniers champs de l'entite)"""
    assert isinstance(code, str), "Type code incorrect"

    #var
    indiv=perso() #perso()
    
    #begin
    if code=="A":
        #begin
        indiv.pos_0_lig=3
        indiv.pos_0_col=3
        #end
    elif code=="B":
        #begin
        indiv.pos_0_lig=3
        indiv.pos_0_col=4
        #end
    elif code=="C":
        #begin
        indiv.pos_0_lig=4
        indiv.pos_0_col=3
        #end
    elif code=="I":
        #begin
        indiv.pos_0_lig=3
        indiv.pos_0_col=31
        #end
    elif code=="J":
        #begin
        indiv.pos_0_lig=3
        indiv.pos_0_col=32
        #end
    elif code=="K":
        #begin
        indiv.pos_0_lig=4
        indiv.pos_0_col=32
        #end
    elif code=="T":
        #begin
        indiv.pos_0_lig=29
        indiv.pos_0_col=3
        #end
    elif code=="U":
        #begin
        indiv.pos_0_lig=30
        indiv.pos_0_col=3
        #end
    elif code=="V":
        #begin
        indiv.pos_0_lig=30
        indiv.pos_0_col=4
        #end
    elif code=="X":
        #begin
        indiv.pos_0_lig=29
        indiv.pos_0_col=32
        #end
    elif code=="Y":
        #begin
        indiv.pos_0_lig=30
        indiv.pos_0_col=31
        #end
    elif code=="Z":
        #begin
        indiv.pos_0_lig=30
        indiv.pos_0_col=32
        #end
    return indiv
    #end

# ==============================================================================

def libre_0(ligne,colonne,tab) :
    """ Renvoie vrai si le code a un deplacemeent possible (ie au moins une case vide adjacente  """
    assert isinstance(ligne, int), "Type ligne incorrect"    # controle des types
    assert isinstance(colonne, int), "Type colonne incorrect"    # des arguments 
    assert isinstance(tab, list), "Type c incorrect"
    
    #begin
    return((tab[ligne-1][colonne]==" ") or (tab[ligne+1][colonne]==" ") or (tab[ligne][colonne-1]==" ") or (tab[ligne][colonne+1]==" "))
    #end

# ==============================================================================

##def main() :
##    """ Explication de ce que fait le programme """
##    #var
##    nom_fichier1="" #str
##    #nom_fichier2="" #str
##    #plateau_tableau1=tableau_0()
##    plateau_tableau2=[["" for c in range(36)] for l in range(36)]
##    a=bool
##    b=bool
##
##    #begin
##    nom_fichier1=input("entrez nom du fichier1")
##    plateau_tableau1=lit_plateau(nom_fichier1)
##    affiche_plateau(plateau_tableau1)
##    a=libre_0(3,3,plateau_tableau1)
##    b=libre_0(3,4,plateau_tableau1)
##    print(a)
##    print(b)
####    deplacement_hero(plateau_tableau1,3)
####    
####    nom_fichier2=input("entrez nom du fichier2")
####    sauve_plateau(plateau_tableau1,nom_fichier2)
####    plateau_tableau2=lit_plateau(nom_fichier2)
####    affiche_plateau(plateau_tableau2)
##    #end
##
###-----------------------------------------------------------------------------------
##if __name__ == "__main__" :
##    main()

# ==============================================================================
# ==============================================================================

def retrouve_position(caractere,tab) :
    """ Donne la position de caractere dans le tableaux36*36 tab """
    assert isinstance(caractere, str), "Type caractere incorrect"    # controle des types
    assert isinstance(tab, list), "Type tab incorrect"    # des arguments 
    
    #var
    car="" #str
    i=0 #int
    j=0 #int
    position=perso() #perso()
    
    #begin
    while i<=35:
        #begin
        while j <= 35:
            #begin
            car=str(tab[i][j])
            if car==caractere:
                position.pos_lig=i
                position.pos_col=j
                return position
            j+=1
            #end
        j=0
        i+=1
        #end
    #end

# ==============================================================================

###var
##liste=liste_joueur()
##
###begin
##liste.joueur1.hero1.pos_0_lig=3
##liste.joueur1.hero1.pos_0_col=3
##liste.joueur1.hero2.pos_0_lig=3
##liste.joueur1.hero2.pos_0_col=4
##liste.joueur1.hero3.pos_0_lig=4
##liste.joueur1.hero3.pos_0_col=3
##
##liste.joueur2.hero1.pos_0_lig=3
##liste.joueur2.hero1.pos_0_col=31
##liste.joueur2.hero2.pos_0_lig=3
##liste.joueur2.hero2.pos_0_col=32
##liste.joueur2.hero3.pos_0_lig=4
##liste.joueur2.hero3.pos_0_col=32
##
##liste.joueur3.hero1.pos_0_lig=29
##liste.joueur3.hero1.pos_0_col=3
##liste.joueur3.hero2.pos_0_lig=30
##liste.joueur3.hero2.pos_0_col=3
##liste.joueur3.hero3.pos_0_lig=30
##liste.joueur3.hero3.pos_0_col=4
##
##liste.joueur2.hero1.pos_0_lig=29
##liste.joueur2.hero1.pos_0_col=32
##liste.joueur2.hero2.pos_0_lig=30
##liste.joueur2.hero2.pos_0_col=31
##liste.joueur2.hero3.pos_0_lig=30
##liste.joueur2.hero3.pos_0_col=32
  
# ==============================================================================

##def main() :
##    """ Explication de ce que fait le programme """
##    #var
##    nom_fichier1="" #str
##    plateau_tableau1=[["" for c in range(36)] for l in range(36)]
##    a=perso()
##    b=perso()
##
##    #begin
##    nom_fichier1=input("entrez nom du fichier1")
##    plateau_tableau1=lit_plateau(nom_fichier1)
##    retrouve_position("A",plateau_tableau1)
##    a=retrouve_position("A",plateau_tableau1)
##    print("you1")
##    print(a.pos_lig)
##    print(a.pos_col)
##    print("you2")
##    b=retrouve_position("B",plateau_tableau1)
##    print(b.pos_lig)
##    print(b.pos_col)
##    print("you3")
##    #end
##
###-----------------------------------------------------------------------------------
##if __name__ == "__main__" :
##    main()

# ==============================================================================
# ==============================================================================

