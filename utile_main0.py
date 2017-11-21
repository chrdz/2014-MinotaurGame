" Ce module contient les fontions : partie_terminee, tour"
# ==============================================================================
# ==============================================================================
from entite0 import *
from random import *
from deplacement0 import *

# ==============================================================================
# ==============================================================================
# cette fonction n'a pas ete testee:

def partie_terminee(nb_joueur, temple) :
    """ Retourne vrai si la partie est terminee, Faux sinon. """
    assert isinstance(nb_joueur, int), "Type nb_joueur incorrect"    # controle des types
    assert isinstance(temple, temple_0), "Type temple incorrect"    # des arguments 

    #begin
    #print("temple.un_0",temple.un_0)#
    if nb_joueur==2:
        if temple.un_0>=2:
            print("Le joueur 1 a gagne la partie.")
            return True
        elif temple.deux_0>=2:
            print("Le joueur 2 a gagne la partie.")
            return True
        elif temple.trois_0>=2:
            print("Le joueur 3 a gagne la partie.")
            return True
        elif temple.quatre_0>=2:
            print("Le joueur 4 a gagne la partie.")
            return True
        else:
            return False
    else:
        if temple.un_0>=1:
            print("Le joueur 1 a gagne la partie.")
            return True
        elif temple.deux_0>=1:
            print("Le joueur 2 a gagne la partie.")
            return True
        elif temple.trois_0>=1:
            print("Le joueur 3 a gagne la partie.")
            return True
        elif temple.quatre_0>=1:
            print("Le joueur 4 a gagne la partie.")
            return True
        else:
            return False   
    #end
        
# ==============================================================================
# ==============================================================================

def tour(labyrinthe) :
    """ Explication de ce que fait la fonction """
    assert isinstance(labyrinthe, labyrinthe_0), "Type labyrinthe incorrect"    # controle des types
    
    #var
    de=0 #int
    nv_laby=labyrinthe_0() #labyrinthe_0()
    
    #begin
    #recuperation des infos de laby:
    nv_laby.tab_0=labyrinthe.tab_0
    nv_laby.tem_0=labyrinthe.tem_0
    
    de=randint(1,6)
    print("Vous avez obtenu ",de," au de.")
    if de==1:
        print("Vous pouvez donc deplacer un mur.")
        nv_laby.tab_0=deplacement_mur(nv_laby.tab_0)
    elif str(de) in "2345":
        print("Vous pouvez donc deplacer un de vos heros.")
        nv_laby=deplacement_hero(nv_laby,de)
    else:
        print("Vous pouvez donc deplacer le minotaure.")
        nv_laby.tab_0=deplacement_minotaure(nv_laby.tab_0)
    return nv_laby
    #end
# ==============================================================================
# ==============================================================================

