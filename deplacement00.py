" Ce module contient les fonctions necessaires au deplacement des murs, des heros, du minotaure."
" Il contient les fonctions: deplacement_mur, deplacement_hero, alea, temple_interdit_au_minotaure, saut, cote, deplacement_minotaure"

from random import *
from plateauechec0 import *
from entite0 import *
from utilitaire0 import *
# ==============================================================================
#cette fonction fonctionne:

def out_of_range(texte) :
    """ Demande d'entrer un entier suivant les consignes de texte et verifie que cet entier est compris entre 0 et 36 (donc correspond a un indice du tableau) """
    assert isinstance(texte, str), "Type texte incorrect"    # des arguments 
    
    #var
    booleen=True #bool
    resultat=0 #int
    
    #begin
    try:
        resultat=int(input(texte))
    except ValueError:
        print("Il faut un entier.")
    booleen=resultat not in range(34)
    while booleen==True:
        print("Attention, l'entier doit etre compris entre 0 et 31. Il faut recommencer.")
        try:
            resultat=int(input(texte))
            break
        except ValueError:
            print("Il faut un entier.")
        booleen=resultat not in range(34)
    return (resultat+2)
    #end

# ==============================================================================
#cette fonction fonctionne:

def deplacement_mur(tab) :
    """ Permet au joueur de deplacer un mur deplacable """
    assert isinstance(tab, list), "Type tab incorrect"    # controle des types
    
    #var
    mur_save=wall() #wall()
    mur=wall() #wall()
    phase1=False #bool
    phase2=False #bool
    phase3=False #bool
    orientation="" #str: 'v' ou 'h'
    change="" #str: 'oui' ou 'non'
    
    #begin
    print("Un mur déplacable est caracterise par la lettre W, il occupe deux cases")
    print("Quel mur voulez-vous deplacer?")
    while phase1 == False:
        mur.centre.pos_deb_lig=out_of_range("Entrez la position en ligne (entier) d'une case occupee par le mur, puis appuyez sur la touche Entree :  ")
        mur.centre.pos_deb_col=out_of_range("Entrez la position en colonne (entier) d'une case occupee par le mur, puis appuyez sur la touche Entree :  ")
        mur.periph.pos_deb_lig=out_of_range("Entrez la position en ligne (entier) de l'autre case occupee par le mur, puis appuyez sur la touche Entree :  ")
        mur.periph.pos_deb_col=out_of_range("Entrez la position en colonne (entier) de l'autre case occupee par le mur, puis appuyez sur la touche Entree :  ")
        mur_save.centre.pos_lig=mur.centre.pos_deb_lig
        mur_save.centre.pos_col=mur.centre.pos_deb_col
        if (mur.centre.pos_deb_lig > mur.periph.pos_deb_lig) or (mur.centre.pos_deb_col > mur.periph.pos_deb_col) :
            mur.centre.pos_deb_lig=mur.periph.pos_deb_lig
            mur.centre.pos_deb_col=mur.periph.pos_deb_col
            mur.periph.pos_deb_lig=mur_save.centre.pos_lig
            mur.periph.pos_deb_col=mur_save.centre.pos_col
        if (tab[mur.centre.pos_deb_lig][mur.centre.pos_deb_col] == "W") and (tab[mur.periph.pos_deb_lig][mur.periph.pos_deb_col] == "W"):
            phase1=True
        else:
            print("Les une ou les deux cases que vous avez choisie(s) ne contien(nen)t pas de mur deplacable")
            print("Ils faut recommencer le choix du mur deplacable.")
    print("Un mur est caracterise par une case dit 'centre' et une case dite 'peripherie'")
    print("Si le mur est disposé horizontalement, alors la case peripherie se trouve a gauche de la case centre")
    print("Si le mur est disposé verticalement, alors la case peripherie se trouve au-dessous de la case centre")
    print("Pour choisir le mur que vous souhaitez deplacer, vous devrez indiquer la position du centre, puis celle de la perpherie")
    while ((phase2 == False) or (phase3 == False)):
        if ((phase2==False) and (phase3==False)):
            print("Ou souhaitez vous placer le centre?")
            mur.centre.pos_lig=int(input("Entrez la position en ligne du centre (entier), puis appuyez sur la touche Entree :  "))+2
            mur.centre.pos_col=int(input("Entrez la position en colonne du centre (entier), puis appuyez sur la touche Entree :  "))+2
            if tab[mur.centre.pos_lig][mur.centre.pos_col]==" ":
                phase2=True
            else:
                print("Vous ne pouvez pas placer le centre ici. Vous devez recommencer.")
        if ((phase2==True) and (phase3==False)):
            orientation=input("Ecrivez 'v' si vous souhaitez orienter le mur verticalement, 'h' si vous souhaitez orienter le mur horizontalement, puis appuyez sur la touche Entree : ")
            if orientation == "v":
                mur.periph.pos_col=mur.centre.pos_col
                mur.periph.pos_lig=mur.centre.pos_lig + 1
            else:
                mur.periph.pos_lig=mur.centre.pos_lig
                mur.periph.pos_col=mur.centre.pos_col + 1
            if tab[mur.periph.pos_lig][mur.periph.pos_col]==" ":
                phase3=True
            else:
                print("Vous ne pouvez pas orienter le mur ainsi.")
                print("Souhaitez-vous changer la position du centre du mur? (repondre par 'oui' ou 'non')")
                if change == "oui":
                    phase2=False
    tab[mur.centre.pos_deb_lig][mur.centre.pos_deb_col]=" " 
    tab[mur.periph.pos_deb_lig][mur.periph.pos_deb_col]=" " 
    tab[mur.centre.pos_lig][mur.centre.pos_col]="W"
    tab[mur.periph.pos_lig][mur.periph.pos_col]="W"
    return tab
    #end


# ==============================================================================

def main() :
    """ Explication de ce que fait le programme """
    #var
    nom_fichier1="" #str
    nom_fichier2="" #str
    plateau_tableau1=[["" for c in range(36)] for l in range(36)]
    plateau_tableau2=[["" for c in range(36)] for l in range(36)]

    #begin
    nom_fichier1=input("entrez nom du fichier1")
    plateau_tableau1=lit_plateau(nom_fichier1)
    affiche_plateau(plateau_tableau1)
    plateau_tableau1=deplacement_mur(plateau_tableau1)
    nom_fichier2=input("entrez nom du fichier2")
    sauve_plateau(plateau_tableau1,nom_fichier2)
    plateau_tableau2=lit_plateau(nom_fichier2)
    affiche_plateau(plateau_tableau2)
    #end

#-----------------------------------------------------------------------------------
if __name__ == "__main__" :
    main()


# ==============================================================================
####def trouve_hero(indiv,tab) :
####    """ Explication de ce que fait la fonction """
####    assert isinstance(indiv, perso), "Type indiv incorrect"    # controle des types
####    assert isinstance(tab, list), "Type tab incorrect"    # des arguments 
####    
####    #var
####    indiv=perso()
####    plateau=[["" for c in range (36)] for l in range(36)]
####    position_car=perso()
####    code=""
####    
####    #begin
####    print("Quel heros souhaitez-vous deplacer?")
####    code=input("Ecrivez A, B, C, I, J, K, T, U, V, X, Y ou Z. Puis appuyez sur la touche Entree : ")
####    position_car=retrouve_position(code,plateau)
####    indiv.pos_lig=position_car.pos_lig
####    indiv.pos_col=position_car.pos_col
####    while code not in "ABCIJKTUVXYZ":
####        #begin
####        print("Vous devez entrer une des lettre suivantes : A,B,C,I,J,K,T,U,V,X,Y,Z. Il faut recommencer.")
####        code=input("Ecrivez A, B, C, I, J, K, T, U, V, X, Y ou Z. Puis appuyez sur la touche Entree : ")
####        position_car=retrouve_position(code,plateau)
####        indiv.pos_lig=position_car.pos_lig
####        indiv.pos_col=position_car.pos_col
####        #end
####    return indiv
####    #end

# ==============================================================================
# ==============================================================================
#cette fonction fonctionne:

def hero_au_temple(ligne, colonne, code, tab) :
    """ Renvoie Vrai si le hero est arrive a son temple. """
    assert isinstance(ligne, int), "Type ligne incorrect"    # controle des types
    assert isinstance(colonne, int), "Type colonne incorrect"    # des arguments 
    assert isinstance(code, str), "Type code incorrect"
    assert isinstance(tab, list),"Type tab incorrect"
    
    #begin
    if (code in "ABC") and tab[ligne][colonne]=="a":
        return True
    elif (code in "IJK") and tab[ligne][colonne]=="b":
        return True
    elif (code in "TUV") and tab[ligne][colonne]=="c":
        return True
    elif (code in "XYZ") and tab[ligne][colonne]=="d":
        return True
    return False    
    #end

# ==============================================================================
#cette fonction semble fonctionner:

def deplacement_hero(labyrinthe,nombre_deplacement) :
    """ Permet au heros d'effectuer le deplacement autorise par le de """
    assert isinstance(labyrinthe, labyrinthe_0), "Type labyrinthe incorrect"
    assert isinstance(nombre_deplacement, int), "Type nombre_deplacement incorrect"    # des arguments 
    
    #var
    indiv=perso() #perso()
    indiv_depart=perso() #perso()
    nb_depl=0 #int
    laby=labyrinthe_0() #labyrinthe_0()
    position_car=perso() #perso()
    code="" #str
    libre=False #bool

    #begin
    nb_depl=nombre_deplacement
    laby.tab_0=labyrinthe.tab_0
    laby.tem_0=labyrinthe.tem_0

    print("Quel heros souhaitez-vous deplacer?")
    code=input("Ecrivez A, B, C, I, J, K, T, U, V, X, Y ou Z. Puis appuyez sur la touche Entree : ")
    while code not in "ABCIJKTUVXYZ":
        #begin
        print("Vous devez entrer une des lettre suivantes : A,B,C,I,J,K,T,U,V,X,Y,Z. Il faut recommencer.")
        code=input("Ecrivez A, B, C, I, J, K, T, U, V, X, Y ou Z. Puis appuyez sur la touche Entree : ")
        #end
    position_car=retrouve_position(code,laby.tab_0)
    indiv.pos_lig=position_car.pos_lig
    indiv.pos_col=position_car.pos_col
    libre=libre_0(indiv.pos_lig,indiv.pos_col,laby.tab_0)
    while libre==False:
            #begin
            print("Vous ne pouvez pas deplacer ce hero, il est encercle. Il faut recommencer.")
            print("Quel heros souhaitez-vous deplacer?")
            code=input("Ecrivez A, B, C, I, J, K, T, U, V, X, Y ou Z. Puis appuyez sur la touche Entree : ")
            while code not in "ABCIJKTUVXYZ":
                #begin
                print("Vous devez entrer une des lettre suivantes : A,B,C,I,J,K,T,U,V,X,Y,Z. Il faut recommencer.")
                code=input("Ecrivez A, B, C, I, J, K, T, U, V, X, Y ou Z. Puis appuyez sur la touche Entree : ")
                #end
            position_car=retrouve_position(code,laby.tab_0)
            indiv.pos_lig=position_car.pos_lig
            indiv.pos_col=position_car.pos_col
            libre=libre_0(indiv.pos_lig,indiv.pos_col,laby.tab_0)
            #end
            
####    indiv.pos_lig=int(input("Entrez la position en ligne du hero : "))+2
####    indiv.pos_col=int(input("Entrez la position en colonne du hero : "))+2
####    code=tab[indiv.pos_lig][indiv.pos_lig]
####    print(tab[indiv.pos_lig][indiv.pos_lig])#
####    while code not in "ABCIJKTUVXYZ":
####        #begin
####        print("La case que vous avez indique ne contient pas de hero. Il faut recommencer.")
####        indiv.pos_lig=int(input("Entrez la position en ligne du hero : "))+2
####        indiv.pos_col=int(input("Entrez la position en colonne du hero : "))+2
####        code=tab[indiv.pos_lig][indiv.pos_lig]
####        print(tab[indiv.pos_lig][indiv.pos_lig])#
####        #end
            
    indiv_0=code_pos(code) #recuperation de la position de depart du hero
    indiv.pos_0_lig=indiv_0.pos_0_lig
    indiv.pos_0_col=indiv_0.pos_0_col
    
    indiv.pos_deb_lig=indiv.pos_lig
    indiv.pos_deb_col=indiv.pos_col

    while nb_depl>=1:
        #begin
        indiv=deplace(indiv) #le hero bouge d'une case
        if laby.tab_0[indiv.pos_lig][indiv.pos_col]=="M": #il rencontre le minotaure
            #begin
            laby.tab_0[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
            laby.tab_0[indiv.pos_0_lig][indiv.pos_0_col]=code
            nb_depl=0
            #end
        elif laby.tab_0[indiv.pos_lig][indiv.pos_col]==" ": #il arrive sur une case vide
            #begin
            laby.tab_0[indiv.pos_lig][indiv.pos_col]=code
            laby.tab_0[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
            nb_depl=nb_depl-1
            #end
        elif hero_au_temple(indiv.pos_lig, indiv.pos_col, code, laby.tab_0)==True: #il arrive a son temple
            #begin
            if code in "ABC":
                laby.tem_0.un_0+=1
            elif code in "IJK":
                laby.tem_0.deux_0+=1
            elif code in "TUV":
                laby.tem_0.trois_0+=1
            else:
                laby.tem_0.quatre_0+=1
            print("Le heros ",code," est arrive a son temple.")
            laby.tab_0[indiv.pos_lig][indiv.pos_col]=code
            laby.tab_0[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
            nb_depl=0
            #end
        else:
            indiv.pos_lig=indiv.pos_deb_lig
            indiv.pos_col=indiv.pos_deb_col
            print("Vous ne pouvez pas vous deplacer sur cette case. Il faut recommencer le deplacement.")
        affiche_plateau(laby.tab_0)
        indiv.pos_deb_lig=indiv.pos_lig
        indiv.pos_deb_col=indiv.pos_col
        #end
    return laby
    #end

# ==============================================================================

##def main() :
##    """ Explication de ce que fait le programme """
##    #var
##    nom_fichier1="" #str
##    nom_fichier2="" #str
##    #plateau_tableau1=[["" for c in range(36)] for l in range(36)]
##    plateau_tableau2=[["" for c in range(36)] for l in range(36)]
##    laby=labyrinthe_0()
##
##    #begin
##    nom_fichier1=input("entrez nom du fichier1")
##    laby.tab_0=lit_plateau(nom_fichier1)
##    affiche_plateau(laby.tab_0)
##
##    laby=deplacement_hero(laby,3)
##    
####    nom_fichier2=input("entrez nom du fichier2")
####    sauve_plateau(plateau_tableau1,nom_fichier2)
####    plateau_tableau2=lit_plateau(nom_fichier2)
####    affiche_plateau(plateau_tableau2)
##    #end
##
###-----------------------------------------------------------------------------------
##if __name__ == "__main__" :
##    main()
##
# ==============================================================================
# ==============================================================================
#cette fonction semble fonctionner:

def alea(individu, tab) :
    """ Place l'individu au hazard dans le tableau, sur une case vide et autorisee """
    assert isinstance(individu, perso), "Type individu incorrect"    # controle des types
    assert isinstance(tab, list), "Type tab incorrect"    # des arguments 
    
    #var
    ligne=0 #int
    colonne=0 #int
    indiv=perso() #perso()
    
    #begin
    #recuperation des infos contenues dans individu:
    indiv.pos_lig=individu.pos_lig
    indiv.pos_col=individu.pos_col
    indiv.pos_deb_lig=individu.pos_deb_lig
    indiv.pos_deb_col=individu.pos_deb_col
    indiv.pos_0_lig=individu.pos_0_lig
    indiv.pos_0_col=individu.pos_0_col
    
    ligne=randint(3,33)
    colonne=randint(3,33)
    if tab[ligne][colonne]==" ":
        indiv.pos_lig=ligne
        indiv.pos_col=colonne
    else:
        alea(individu,tab)
    return indiv
    #end

# ==============================================================================
#cette fonction fonctionne:

def interdit(ligne, colonne,chaine) :
    """ Retourne Vrai si la position en ligne et colonne, dans le plateau de jeu, est une position de point de depart des heros """
    """ ou une position des temples"""
    assert isinstance(ligne, int), "Type ligne incorrect"    # controle des types
    assert isinstance(colonne, int), "Type colonne incorrect"    # des arguments
    assert isinstance (chaine, str), "Type chaine incorrect"
    
    #var
    position=perso() #perso()
    plateau=[["" for c in range(36)]for l in range(36)] #list
    car="" #str
    
    #begin
    plateau=lit_plateau("initial.txt") #lit le plateau de depart
    for car in chaine:
        position=retrouve_position(car,plateau)
        if position.pos_lig==ligne and position.pos_col==colonne:
            return True
    return False
    #end

# ==============================================================================
#cette fonction fonctionne:

def saut(individu):
    """ Fait passer le minotaure par dessus certaines cases (ici ce seront les cases contenant les..."""
    """... lettres abcd qui representent les temples) si la case d'arrivée est vide"""
    assert isinstance (individu,perso), "Type individu incorrect"
    
    #var
    indiv=perso() #perso()
    
    #begin
    indiv.pos_lig=individu.pos_lig
    indiv.pos_col=individu.pos_col
    indiv.pos_deb_lig=individu.pos_deb_lig
    indiv.pos_deb_col=individu.pos_deb_col

    indiv.pos_lig += indiv.pos_lig - indiv.pos_deb_lig
    indiv.pos_col += indiv.pos_col - indiv.pos_deb_col
    return indiv
    #end

# ==============================================================================
#cette fonction semble fonctionner:

def cote(indiv,tab) :
    """ Place le joueur dans une case adajcente a la case ou il doit être place, si cette case ou il doit etre place est occupee """
    assert isinstance(indiv, perso), "Type indiv incorrect"    # controle des types
    assert isinstance(tab,list), "Type tab incorrest"
    
    #var
    pers=perso() #perso()
    choix=0 #int (compris entre 1 et 4)
    plateau=[[""for c in range(36)] for l in range(36)] #list
    
    #begin
    plateau=tab
    #recuperation des infos contenues dans indiv:
    pers.pos_lig=indiv.pos_lig
    pers.pos_col=indiv.pos_col
    pers.pos_deb_lig=indiv.pos_deb_lig
    pers.pos_deb_col=indiv.pos_deb_col
    pers.pos_0_lig=indiv.pos_0_lig
    pers.pos_0_col=indiv.pos_0_col

    if plateau[indiv.pos_0_lig][indiv.pos_0_col+1]==" ":
        pers.pos_0_col+=1
    elif plateau[indiv.pos_0_lig+1][indiv.pos_0_col]==" ":
        pers.pos_0_lig+=1
    elif plateau[indiv.pos_0_lig][indiv.pos_0_col-1]==" ":
        pers.pos_0_lig-=1
    elif plateau[indiv.pos_0_lig-1][indiv.pos_0_col]==" ":
        pers.pos_0_lig-=1
    else:
        #begin
        choix=randint(1,4)
        if choix==1:
            #begin
            pers.pos_0_col+=1
            return cote(pers,plateau)
            #end
        elif choix==2:
            #begin
            pers.pos_0_lig+=1
            return cote(pers,plateau)
            #end
        elif choix==3:
            #begin
            pers.pos_0_col-=1
            return cote(pers,plateau)
            #end
        else:
            #begin
            pers.pos_0_lig-=1
            return cote(pers,plateau)
            #end
        #end
    return pers
    #end

# ==============================================================================
#cette fonction semble fonctionner:

def deplacement_minotaure(tab) :
    """ Permet permet de deplacer le minotaure de huit cases """
    assert isinstance(tab, list), "Type tab incorrect"
    
    #var
    indiv=perso() #perso()
    indiv_depart=perso() #perso()
    indiv_transfert=perso() #perso()
    nb_depl=0 #int
    plateau=[["" for c in range (36)] for l in range(36)] #list
    position_car=perso() #perso()
    car="" #str
    car_bis="" #str
# NB : Il est interdit d'entourer le minotaure de murs deplacables,
# donc on suppose que le minotaure aura toujours des possibilités de deplacement.
# ou alors si le minotaure est encercle (meme à large echelle : d'ailleurs comment le detecter...
#...peut etre ne pas le detecter mais simplement demander au joueur de dire si c'est le cas)...
#...faire une fonction qui place le minotaure aleatoiremeent sur une case vide

    #begin
    nb_depl=8
    plateau=tab
    position_car=retrouve_position("M",plateau)
    indiv.pos_lig=position_car.pos_lig
    indiv.pos_col=position_car.pos_col

    indiv.pos_deb_lig=indiv.pos_lig
    indiv.pos_deb_col=indiv.pos_col
        
##        ##libre=libre_0(indiv.pos_lig,indiv.pos_col,plateau)
####    while libre==False:
####        #begin
####        plateau=tab
####        position_car=retrouve_position("M",plateau)
####        indiv.pos_lig=position_car.pos_lig
####        indiv.pos_col=position_car.pos_col
####        ##libre=libre_0(indiv.pos_lig,indiv.pos_col,plateau)
####        #end

    while nb_depl>=1:
        #begin
        indiv=deplace(indiv) #le minotaure se deplace d'une case
        car=plateau[indiv.pos_lig][indiv.pos_col] #c'est le caractere qui est contenu dans la case ou le minotaure veut aller
        if interdit(indiv.pos_lig,indiv.pos_col,"ABCIJKTUVXYZ")==True: #le minotaure n'a pas le droit d'aller sur les points de depart des joueurs
            indiv=alea(indiv,plateau) #il est renvoye sur une case vide, au hasard, dans le plateau
            plateau[indiv.pos_lig][indiv.pos_col]="M"
            plateau[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
        elif car in "ABCIJKTUVXYZ": #le minotaure arrive sur un joueur
            #begin
            indiv_0=code_pos(car) 
            indiv.pos_0_lig=indiv_0.pos_0_lig
            indiv.pos_0_col=indiv_0.pos_0_col
            if plateau[indiv.pos_0_lig][indiv.pos_0_col]!=" ":
                indiv=cote(indiv,plateau)
            plateau[indiv.pos_0_lig][indiv.pos_0_col]=car
            plateau[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
            plateau[indiv.pos_lig][indiv.pos_col]="M"
            nb_depl -= 1
            #end
        elif car==" ": #le minotaure arrive sur une case vide
            #begin
            plateau[indiv.pos_lig][indiv.pos_col]="M"
            plateau[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
            nb_depl=nb_depl-1
            #end
        elif interdit(indiv.pos_lig,indiv.pos_col,"abcijktuvxyz")==True: # le minotaure veut aller sur un temple
            #begin
            indiv_transfert=saut(indiv) #le minotaure va sauter par dessus le temple
            indiv.pos_lig=indiv_transfert.pos_lig
            indiv.pos_col=indiv_transfert.pos_col
            car_bis=plateau[indiv.pos_lig][indiv.pos_col]
    #Il va maintenant falloir verifier ce qui se trouve derriere le temple pour savoir si le minotaure peut sauter:
##            if interdit(indiv.pos_lig,indiv.pos_col,"ABCIJKTUVXYZ")==True:    #Dans ce plateau, il ne peut pas y avoir de case de depart d'un joueur...
##                indiv=alea(indiv,plateau)                                     #...derriere le temple.
##                plateau[indiv.pos_lig][indiv.pos_col]="M"
##                plateau[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
            if car_bis in "ABCIJKTUVXYZ":
                #begin
                indiv_0=code_pos(car_bis) 
                indiv.pos_0_lig=indiv_0.pos_0_lig
                indiv.pos_0_col=indiv_0.pos_0_col
                if plateau[indiv.pos_0_lig][indiv.pos_0_col]!=" ":
                    indiv=cote(indiv,plateau)
                plateau[indiv.pos_0_lig][indiv.pos_0_col]=car_bis
                plateau[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
                plateau[indiv.pos_lig][indiv.pos_col]="M"
                nb_depl -= 1
                #end
            elif car_bis==" ":
                #begin
                plateau[indiv.pos_lig][indiv.pos_col]="M"
                plateau[indiv.pos_deb_lig][indiv.pos_deb_col]=" "
                nb_depl=nb_depl-1
                #end
            else:
                indiv.pos_lig=indiv.pos_deb_lig
                indiv.pos_col=indiv.pos_deb_col
                print("Vous ne pouvez pas deplacer le minotaure sur cette case. Il faut recommencer le deplacement.")
            #end
        else:
            indiv.pos_lig=indiv.pos_deb_lig
            indiv.pos_col=indiv.pos_deb_col
            print("Vous ne pouvez pas deplacer le minotaure sur cette case. Il faut recommencer le deplacement.")
        affiche_plateau(plateau)
        indiv.pos_deb_lig=indiv.pos_lig
        indiv.pos_deb_col=indiv.pos_col
        #end
    return plateau
    #end

# ==============================================================================

##def main() :
##    """ Explication de ce que fait le programme """
##    #var
##    nom_fichier1="" #str
##    nom_fichier2="" #str
##    plateau_tableau1=[["" for c in range(36)] for l in range(36)]
##    plateau_tableau2=[["" for c in range(36)] for l in range(36)]
##    liste=liste_joueur()
##
##
##    #begin
##    nom_fichier1=input("entrez nom du fichier1")
##    plateau_tableau1=lit_plateau(nom_fichier1)
##    affiche_plateau(plateau_tableau1)
##
##    deplacement_minotaure(plateau_tableau1)
##    
####    nom_fichier2=input("entrez nom du fichier2")
####    sauve_plateau(plateau_tableau1,nom_fichier2)
####    plateau_tableau2=lit_plateau(nom_fichier2)
####    affiche_plateau(plateau_tableau2)
##    #end
##
##
###-----------------------------------------------------------------------------------
##if __name__ == "__main__" :
##    main()

# ==============================================================================
# ==============================================================================

