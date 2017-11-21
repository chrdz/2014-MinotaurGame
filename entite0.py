class perso (object):
    def __init__(self,code="",pos_lig=0,pos_col=0,pos_deb_lig=0,pos_deb_col=0,pos_0_lig=0,pos_0_col=0):
        self.code=code #str
        self.pos_lig=pos_lig #int
        self.pos_col=pos_col #int
        self.pos_deb_col=pos_deb_lig #int
        self.pos_deb_col=pos_deb_col #int
        self.pos_0_lig=pos_0_lig #int
        self.pos_0_col=pos_0_col #int

class joueur (object):
    def __init__(self,nom="",nb_au_temple=0,hero_1=perso(),hero_2=perso(),hero_3=perso()):
        self.nom=nom #str
        self.nb_au_temple=nb_au_temple #int
        self.hero_1=hero_1 #perso
        self.hero_2=hero_2 #perso
        self.hero_3=hero_3 #perso

class liste_joueur(object):
    def __init__(self,joueur_1=joueur(),joueur_2=joueur(),joueur_3=joueur(),joueur_4=joueur()):
        self.joueur_1=joueur_1 #joueur
        self.joueur_2=joueur_2 #joueur
        self.joueur_3=joueur_3 #joueur
        self.joueur_4=joueur_4 #joueur

class wall(object):
    def __init__(self,centre=perso(),periph=perso()):
        self.centre=centre #perso
        self.periph=periph #perso

##class tableau_0(object):
##    def __init__(self):
##        self.tab_0=[["" for c in range(36)]for l in range(36)]
##    def libre(self,ligne,colonne) :
##        """ Renvoie vrai si le code a un deplacemeent possible (ie au moins une case vide adjacente  """
##        #assert isinstance(ligne, int), "Type ligne incorrect"    # controle des types
##        #assert isinstance(colonne, int), "Type colonne incorrect"    # des arguments 
##        #begin
##        return(((self.tab_0[ligne-1][colonne])==" ") or ((self.tab_0[ligne+1][colonne])==" ") or ((self.tab_0[ligne][colonne-1])==" ") or ((self.tab_0[ligne][colonne+1])==" "))
####            return False
####        else:
####            return True
##        #end

class temple_0(object):
    def __init__(self,un_0=0,deux_0=0,trois_0=0,quatre_0=0):
        self.un_0=un_0 #int
        self.deux_0=deux_0 #int
        self.trois_0=trois_0 #int
        self.quatre_0=quatre_0 #int
        
class labyrinthe_0(object):
    def __init__(self):
        self.tab_0=[["" for c in range(36)]for l in range(36)] #list
        self.tem_0=temple_0() #temple_0()
        # abandonnee:
##    def fini(self,nb_joueur):
##        """ Dit si la partie est terminee en fonction du nombre de joueurs """
##        #begin
##        if nb_joueur>=3:
##            if self.tem_0.un_0>=1 or self.tem_0.deux_0>=1 or self.tem_0.trois_0>=1 or self.tem_0.quatre_0>=1 :
##                return True
##            else:
##                return False
##        if nb_joueur=2:
##            if self.tem_0.un_0>=2 or self.tem_0.deux_0>=2 or self.tem_0.trois_0>=2 or self.tem_0.quatre_0>=2 :
##                return True
##            else:
##                return False
##        #end
            
        

