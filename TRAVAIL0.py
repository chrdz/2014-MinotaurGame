# ==============================================================================
# SQUELETTE : squelette de programmame Python, à utiliser quand vous créez un
#             nouveau programme
# ==============================================================================
from random import *
from plateauechec0 import *
from entite0 import *
from deplacement0 import *
from utile_main0 import *

# ==============================================================================
# ==============================================================================
def exemple(a, b,c) :
    """ Explication de ce que fait la fonction """
    assert isinstance(a, int), "Type a incorrect"    # controle des types
    assert isinstance(b, str), "Type b incorrect"    # des arguments 
    assert isinstance(b, bool), "Type c incorrect"
    
    #var
    # declarion des variales ici

    #begin

    # ici, vous mettez le code de votre fonction
    
    #end

# ==============================================================================
##def code_ok(tab,ligne,colonne,code) :
##    """ Retourne Vrai si la lettre contenue dans le tableau au coordonnees donnees est bien le code souhaite """
##    assert isinstance(tab, list), "Type tab incorrect"    # controle des types
##    assert isinstance(ligne, int), "Type ligne incorrect"    # des arguments 
##    assert isinstance(colonne, int), "Type colonne incorrect"
##    assert isinstance(code, str), "Type code incorrect"
##    
##    #var
##
##    #begin
##    if tab[ligne][colonne] == code:
##        return True
##    else:
##        return False
##    #end
##
    
# ==============================================================================
##
##def case_vide(lig, col,tab) :
##    """ Renvoie Vrai si la case du tableau2D de coordonnées lig et col contient " " """
##    assert isinstance(lig, int), "Type lig incorrect"    # controle des types
##    assert isinstance(col, str), "Type col incorrect"    # des arguments 
##    assert isinstance(tab,list), "Type tab incorrect"
##    
##    #var
##
##    #begin
##    if tab[lig][col]== " ":
##        return True
##    else:
##        return False
##    #end
##

# ==============================================================================
# ==============================================================================
def sauvegarde_temple(temple,tab) :
    """ Pour la recuperation d'une partie sauvegardee, remplit la variable qui decompte le nombre de heros dans les temples. """
    assert isinstance(temple, temple_0), "Type temple incorrect"    # controle des types
    assert isinstance (tab, list), "Type tab incorrect"
    
    #var
    car="" #str
    tem=temple_0() #temple_0()
    lab=[[""for c in range(36)] for l in range(36)] #list : c'est le tableau de depart

    #begin
    lab=lit_plateau("labye.txt")
    for car in "ABC":
        if hero_au_temple((retrouve_position(car,tab)).pos_lig, (retrouve_position(car,tab)).pos_col, car, lab)==True:
            tem.un_0+=1
    for car in "IJK":
        if hero_au_temple((retrouve_position(car,tab)).pos_lig, (retrouve_position(car,tab)).pos_col, car, lab)==True:
            tem.deux_0+=1
    for car in "TUV":
        if hero_au_temple((retrouve_position(car,tab)).pos_lig, (retrouve_position(car,tab)).pos_col, car, lab)==True:
            tem.trois_0+=1
    for car in "XYZ":
        if hero_au_temple((retrouve_position(car,tab)).pos_lig, (retrouve_position(car,tab)).pos_col, car, lab)==True:
            tem.quatre_0+=1
    return tem            
    #end

# ==============================================================================
def main() :
    """ Explication de ce que fait le programme """
    
    #var
    nb_jou=0 #int
    nom_fic="" #str
    fic_save="" #str
    labyrinthe=labyrinthe_0() #labyrinthe_0()
    joueur="" #str
    compteur=0 #int
    nb_jou=0 #int : 2, 3 ou 4
    pertie="" #str

    #begin
    nb_jou=int(input("Veuillez ecrire le nombre de joueurs (2,3 ou 4). Puis appuyez sur la touche Entree : "))
    while (nb_jou!=2 and nb_jou!=3 and nb_jou!=4):
        #begin
        print("Vous devez entrer le chiffre 2, 3 ou 4. Il faut recommencer.")
        nb_jou=int(input("Veuillez ecrire le nombre de joueurs (2,3 ou 4). Puis appuyez sur la touche Entree : "))
        #end
    partie=input("Voulez-vous charger une nouvelle partie? (ecrire 'oui' ou non', puis appuyer sur la touche Entree) : ")
    if partie=="oui":
        nom_fic="labye.txt"
        labyrinthe.tab_0=lit_plateau(nom_fic)
        labyrinthe.tem_0=sauvegarde_temple(labyrinthe.tem_0,labyrinthe.tab_0)
    else:
        nom_fic=input("Veuillez entrer le nom du fichier que vous avez sauvegarde dans une partie precedente. puis appuyez sur la touche Entree : ")+".txt"
        labyrinthe.tab_0=lit_plateau(nom_fic)
    fic_save=input("Veuillez entrer le nom sous lequel vous souhaitez enregistrer la partie. Puis appuyez sur la touche Entree : ")+".txt"
    print("Votre partie sera enregistree sous le nom '",fic_save,"'.")
    affiche_plateau(labyrinthe.tab_0)
    while partie_terminee(nb_jou,labyrinthe.tem_0)==False:
        joueur="joueur"+str((compteur % nb_jou)+1)
        print(joueur,"c'est a vous de jouer")
        labyrinthe=tour(labyrinthe)
        compteur+=1
        sauve_plateau(labyrinthe.tab_0,fic_save)
        #end


#-----------------------------------------------------------------------------------
if __name__ == "__main__" :
    main()
