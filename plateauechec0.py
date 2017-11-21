"""module plateau contenant les fonctions lit_plateau, affiche_plateau et sauve_plateau"""
from entite0 import *
# ==============================================================================
# ==============================================================================
def lit_plateau(nom_fichier1) :
    """ Lit le fichier plateau de début de partie et place les caracteres dans un tableau"""
    assert isinstance(nom_fichier1, str), "Type nom_fichier incorrect, il faut un str"    # controle des types
    
    #var
    tableau_plateau=[["" for c in range(36)] for l in range(36)]
    #tableau_plateau=tableau_0()
    caractere="" #str
    indice_colonne=0 #int
    indice_ligne=0 #int
    #fichier_plateau_depart =   #fichier de str??? comment le déclarer
    
    #begin
    fichier_plateau_depart = open(nom_fichier1,"r") #read
    caractere=str(fichier_plateau_depart.read(1).strip("\n"))
    while caractere!="":
        #begin
        for indice_colonne in range(36) :
            #begin
            tableau_plateau[indice_ligne][indice_colonne]=caractere
            caractere=str(fichier_plateau_depart.read(1).strip("\n"))
            #end
        indice_colonne=0
        indice_ligne+=1
        caractere=str(fichier_plateau_depart.read(1).strip("\n"))
        #end
    fichier_plateau_depart.close()
    return(tableau_plateau)
    #end
# ==============================================================================
def affiche_plateau(tab) :
    """ Permet d'afficher à l'écran le tab"""
    assert isinstance(tab, list), "Type tab incorrect"
    
    #var
    ligne=0   #int
    colonne=0   #int
    i=0 #int
    j=0 #int
    
    #begin
    for ligne in range(36):
        #begin
        for colonne in range(36):
            print(tab[ligne][colonne],end="")
        print("\n",end="")
        j+=1
        #end
    #end
        
# ==============================================================================
def sauve_plateau(nv_tab, nom_fichier2) :
    """ Explication de ce que fait la fonction """
    assert isinstance(nv_tab, list), "Type nv_tab incorrect"    # controle des types
    assert isinstance(nom_fichier2, str), "Type nom_fichier incorrect"    # des arguments 
    
    #var
    #nv_fic = fichier de caractere
    indice_ligne=0 #int
    indice_colonne=0 #int

    #begin
    nv_fic = open(nom_fichier2,"w") #write
    for indice_ligne in range(36):
        #debut
        for indice_colonne in range(36):
            nv_fic.write(nv_tab[indice_ligne][indice_colonne])
        nv_fic.write("\n")
        indice_colonne=0
        #end    
    #end

# ==============================================================================
##
##def main() :
##    """ Explication de ce que fait le programme """
##    #var
##    nom_fichier1="" #str
##    nom_fichier2="" #str
##    plateau_tableau1=[["" for c in range(32)] for l in range(32)]
##    plateau_tableau2=[["" for c in range(32)] for l in range(32)]
##
##    #begin
##    nom_fichier1=input("entrez nom du fichier1")
##    plateau_tableau1=lit_plateau(nom_fichier1)
##    affiche_plateau(plateau_tableau1)
##    nom_fichier2=input("entrez nom du fichier2")
##    sauve_plateau(plateau_tableau1,nom_fichier2)
##    plateau_tableau2=lit_plateau(nom_fichier2)
##    affiche_plateau(plateau_tableau2)
##    #end
##
###-----------------------------------------------------------------------------------
##if __name__ == "__main__" :
##    main()
