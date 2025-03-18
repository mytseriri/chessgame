# -*- coding: utf-8 -*-
import pygame
from copy import deepcopy


wN = pygame.transform.scale(pygame.image.load("images\\wN.png"),(73,73))
wR = pygame.transform.scale(pygame.image.load("images\\wR.png"),(73,73))
wP = pygame.transform.scale(pygame.image.load("images\\wP.png"),(73,73))
wQ = pygame.transform.scale(pygame.image.load("images\\wQ.png"),(73,73))
wB = pygame.transform.scale(pygame.image.load("images\\wB.png"),(73,73))
wK = pygame.transform.scale(pygame.image.load("images\\wK.png"),(73,73))
bN = pygame.transform.scale(pygame.image.load("images\\bN.png"),(73,73))
bR = pygame.transform.scale(pygame.image.load("images\\bR.png"),(73,73))
bP = pygame.transform.scale(pygame.image.load("images\\bP.png"),(73,73))
bQ = pygame.transform.scale(pygame.image.load("images\\bQ.png"),(73,73))
bB = pygame.transform.scale(pygame.image.load("images\\bB.png"),(73,73))
bK = pygame.transform.scale(pygame.image.load("images\\bK.png"),(73,73))              
                   

                   
                   
def signe(n):
    if n<0:
        return -1
    elif n==0:
        return 0
    else:
        return 1
                   
Plateau0 = [[["Tour","Blanc"],["Cavalier","Blanc"],["Fou","Blanc"],["Dame","Blanc"],\
["Roi","Blanc"],["Fou","Blanc"],["Cavalier","Blanc"],["Tour","Blanc"]],\
[["Pion","Blanc"] for i in range(8)],
[[0,0] for i in range(8)], [[0,0] for i in range(8)], [[0,0] for i in range(8)],\
[[0,0] for i in range(8)],\
[["Pion","Noir"] for i in range(8)],[["Tour","Noir"],["Cavalier","Noir"],["Fou","Noir"],\
["Dame","Noir"],["Roi","Noir"],["Fou","Noir"],["Cavalier","Noir"],["Tour","Noir"]]]
    
Plateau1 = [[["Tour","Blanc"],["Cavalier","Blanc"],["Fou","Blanc"],["Tour","Noir"],\
["Roi","Blanc"],["Fou","Blanc"],["Cavalier","Blanc"],["Tour","Blanc"]],\
[["Pion","Blanc"] for i in range(8)],
[[0,0] for i in range(8)], [[0,0] for i in range(8)], [[0,0] for i in range(8)],\
[[0,0] for i in range(8)],\
[["Pion","Noir"] for i in range(8)],[["Tour","Noir"],["Cavalier","Noir"],["Fou","Noir"],\
["Dame","Noir"],["Roi","Noir"],["Fou","Noir"],["Cavalier","Noir"],["Tour","Noir"]]]


    
def diag_gd(point):  #diagonale de gauche a droite
    coord =[]
    i = 1
    while point[0]+i <=7 and point[1]-i >=0:
        i+=1
    coord = [point[0]+i-1,point[0]-i+1]
    return coord

def diag_dg(point): #diagonale de droite a gauche
    coord =[]
    i = 1
    while point[0]+i <=7 and point[1]+i >=0:
        i+=1
    coord = [point[0]+i-1,point[0]-i-1]
    return coord

def coups_possible(position,plateau):
    nom_piece = plateau[position[0]][position[1]][0]
    couleur = plateau[position[0]][position[1]][1]
    #print(couleur)
    #print(nom_piece)
    L = []
    if couleur == "Blanc":
        if nom_piece == "Tour":
            dep = []                                                             
            for i in range(8):                                                                                                      
                    dep.append([position[0],i])
            for j in range(8):
                    dep.append([j,position[1]])

    
        elif nom_piece == "Pion":
            dep = [[position[0]+1,position[1]],[position[0]+2,position[1]],[position[0]+1,position[1]-1],[position[0]+1,position[1]+1]]

        elif nom_piece== "Roi":
            dep = [[position[0]+1,position[1]],[position[0]+1,position[1]+1],[position[0]+1,position[1]-1],[position[0],position[1]-1],[position[0],position[1]+1],[position[0]-1,position[1]],[position[0]-1,position[1]-1],[position[0]-1,position[1]+1]]
            
        #    for x_1 in range(8):
        #        if dep[x_1][0]<0 or dep[x_1][0]>7 or dep[x_1][1]<0 or dep[x_1][1]>7:
                    
        elif nom_piece == "Dame":
            dep = []
            for i in range(8):
                dep.append([position[0],i])   #horizontal
            for j in range(8):                  #vertical 
                dep.append([j,position[1]])
            for i in range(8):
                #determination des coordonnées du 1ere point de la diagonale de gauche a droite 
                xI = diag_gd(position)[0]         
                yI = diag_gd(position)[1]  
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI+1])    
                #determination des coordonnées du 1ere point de la diagonale de droite a gauche               
            for j in range(8):
                xI = diag_dg(position)[0]         
                yI = diag_dg(position)[1]
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI-1]) 

        elif nom_piece == "Cavalier":
            dep = [[position[0]+3,position[1]+1],[position[0]+3,position[1]-1],[position[0]-3,position[1]-1],[position[0]-3,position[1]+1],[position[0]+1,position[1]+3],[position[0]-1,position[1]+3],[position[0]-3,position[1]+1],[position[0]-3,position[1]-1]]

        elif nom_piece== "Fou": #diagonales (prendre le meme code que pour les diagonales de la reine)
            dep =[]
            for i in range(8):
                #determination des coordonnées du 1ere point de la diagonale de gauche a droite 
                xI = diag_gd(position)[0]         
                yI = diag_gd(position)[1]  
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI+1])    
                #determination des coordonnées du 1ere point de la diagonale de droite a gauche               
            for j in range(8):
                xI = diag_dg(position)[0]         
                yI = diag_dg(position)[1]
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI-1])      
                
    elif couleur == "Noir":
        if nom_piece == "Tour":
            dep = []                                                             
            for i in range(8):                                                                                                      
                    dep.append([position[0],i])
            for j in range(8):
                    dep.append([j,position[1]])

    
        elif nom_piece == "Pion":
            dep = [[position[0]-1,position[1]],[position[0]-2,position[1]],[position[0]-1,position[1]-1],[position[0]-1,position[1]+1]]

        elif nom_piece== "Roi":
            dep = [[position[0]+1,position[1]],[position[0]+1,position[1]+1],[position[0]+1,position[1]-1],[position[0],position[1]-1],[position[0],position[1]+1],[position[0]-1,position[1]],[position[0]-1,position[1]-1],[position[0]-1,position[1]+1]]

        elif nom_piece == "Dame":
            dep = []
            for i in range(8):
                dep.append([position[0],i])   #horizontal
            for j in range(8):                  #vertical 
                dep.append([j,position[1]])
            for i in range(8):
                #determination des coordonnées du 1ere point de la diagonale de droite a gauche 
                xI = diag_gd(position)[0]         #gd par symétrie (la diag de gd pour les blancs est la diag dg pour les noirs)
                yI = diag_gd(position)[1]  
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI+1])    
                #determination des coordonnées du 1ere point de la diagonale de gauche a droite               
            for j in range(8):
                xI = diag_dg(position)[0]         
                yI = diag_dg(position)[1]
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI-1])

        elif nom_piece == "Cavalier":
            dep = [[position[0]+3,position[1]+1],[position[0]+3,position[1]-1],[position[0]-3,position[1]-1],[position[0]-3,position[1]+1],[position[0]+1,position[1]+3],[position[0]-1,position[1]+3],[position[0]-3,position[1]+1],[position[0]-3,position[1]-1]]

        elif nom_piece== "Fou":
            dep =[]      #diagonales (prendre le meme code que pour les diagonales de la reine)
            for i in range(8):
                #determination des coordonnées du 1ere point de la diagonale de droite a gauche 
                xI = diag_gd(position)[0]         #gd par symétrie (la diag de gd pour les blancs est la diag dg pour les noirs)
                yI = diag_gd(position)[1]  
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI+1])    
                #determination des coordonnées du 1ere point de la diagonale de gauche a droite               
            for j in range(8):
                xI = diag_dg(position)[0]         
                yI = diag_dg(position)[1]
                while xI >=0 and yI<=7 and xI <= 7 and yI >=0:
                    dep.append([xI-1,yI-1])
    
    else:
        return []

    try:
        dep.remove(position)                #on retire la position initiale de la piece de la liste dep si elle est présente
    except:
        pass                                #o cas ou ya pas dans la liste
    
    for i in range(len(dep)-1):
        if vérif(position,dep[i],plateau) == True:
            L.append(dep[i])   
    return L



def coup(depart,arrivee,plateau):
    plateau[arrivee[0]][arrivee[1]]=plateau[depart[0]][depart[1]]
    plateau[depart[0]][depart[1]]=[0,0]
        
        
        
def vérif(depart,arrivee,plateau,rock_gauche_blanc=True,rock_droit_blanc=True,rock_gauche_noir=True,rock_droit_noir=True):
    if plateau[depart[0]][depart[1]] == [0,0]:
        return False
    elif depart==arrivee :
        return False
    elif (arrivee[0]<0) or (arrivee[0]>7) or (arrivee[1]<0) or (arrivee[1]>7):
        return False
    elif plateau[arrivee[0]][arrivee[1]][1]==plateau[depart[0]][depart[1]][1]:
        return False

    else:
        piece=plateau[depart[0]][depart[1]]
        deplac=[arrivee[0]-depart[0],arrivee[1]-depart[1]]
        if piece[0]=="Pion":
            if piece[1]=="Blanc":
                if deplac==[1,0] and plateau[arrivee[0]][arrivee[1]][1] == 0:
                    return True
                elif depart[0]==1:
                    if deplac==[2,0] and plateau[arrivee[0]][arrivee[1]][1] == 0:
                        return True
                elif deplac==[1,1] and plateau[arrivee[0]][arrivee[1]][1] == "Noir":
                    return True 
                elif deplac==[1,-1] and plateau[arrivee[0]][arrivee[1]][1] == "Noir":
                    return True 
                      
            elif piece[1]=="Noir":
                if deplac==[-1,0] and plateau[arrivee[0]][arrivee[1]][1] == 0:
                    return True
                elif depart[0]==6:
                    if deplac==[-2,0] and plateau[arrivee[0]][arrivee[1]][1] == 0:
                        return True
                elif deplac==[-1,-1] and plateau[arrivee[0]][arrivee[1]][1] == "Blanc":
                    return True 
                elif deplac==[-1,1] and plateau[arrivee[0]][arrivee[1]][1] == "Blanc":
                    return True 
            return False
            
        
        elif piece[0]=="Cavalier":  #Le cavalier peut sauter au dessus des pièces
            if deplac[0]*deplac[1]==2 or deplac[0]*deplac[1]==-2:  
                return True
            return False
        
        elif piece[0]=="Fou":
            if deplac[0]==deplac[1] or deplac[0]==-deplac[1]:
                dir_x = signe(deplac[0])
                dir_y = signe(deplac[1])
                a=deplac[0]*dir_x
                for i in range(1,a+1):
                    if plateau[depart[0]+i*dir_x][depart[1]+i*dir_y][1]==piece[1]:
                        return False
                    elif plateau[depart[0]+i*dir_x][depart[1]+i*dir_y][1]!=0 and i!=a:
                        return False
                return True
            return False
        
        elif piece[0]=="Tour":
            if deplac[0]==0 or deplac[1]==0:
                dir_x = signe(deplac[0])
                dir_y = signe(deplac[1])#un des deux vaudra 0 !
                if deplac[0]==0:
                    a=deplac[1]*dir_y
                else :
                    a=deplac[0]*dir_x
                for i in range(1,a+1):
                    if plateau[depart[0]+i*dir_x][depart[1]+i*dir_y][1]==piece[1]:
                        return False
                    elif plateau[depart[0]+i*dir_x][depart[1]+i*dir_y][1]!=0 and i!=a:
                        return False
                return True
            return False
        
        elif piece[0]=="Dame":
            if deplac[0]==0 or deplac[1]==0 or deplac[0]==deplac[1] or deplac[0]==-deplac[1]:
                dir_x = signe(deplac[0])
                dir_y = signe(deplac[1])  
                if deplac[0]==0:
                    a=deplac[1]*dir_y
                else :
                    a=deplac[0]*dir_x
                for i in range(1,a+1):
                    if plateau[depart[0]+i*dir_x][depart[1]+i*dir_y][1]:
                        return False
                    elif plateau[depart[0]+i*dir_x][depart[1]+i*dir_y][1]!=0 and i!=a:
                        return False
                return True
            return False
        
        elif piece[0]=="Roi":
            if deplac[0]==1 or deplac[0]==0 or deplac[0]==-1:
                if deplac[1]==1 or deplac[1]==0 or deplac[1]==-1:
                    return True
            return False
        


def inpt(stri):
    word=""
    print(stri) #example asking names
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False
                if event.key == pygame.K_0:
                    word+=str(chr(event.key))
                if event.key == pygame.K_1:
                    word+=chr(event.key)
                if event.key == pygame.K_2:
                    word+=chr(event.key)
                if event.key == pygame.K_3:
                    word+=chr(event.key)
                if event.key == pygame.K_4:
                    word+=chr(event.key)
                if event.key == pygame.K_5:
                    word+=chr(event.key)
                if event.key == pygame.K_6:
                    word+=chr(event.key)
                if event.key == pygame.K_7:
                    word+=chr(event.key)
                if event.key == pygame.K_8:
                    word+=chr(event.key)
                if event.key == pygame.K_9:
                    word+=chr(event.key)
                if event.key == pygame.K_a:
                    word+=chr(event.key)
                if event.key == pygame.K_b:
                    word+=chr(event.key)
                if event.key == pygame.K_c:
                    word+=chr(event.key)
                if event.key == pygame.K_d:
                    word+=chr(event.key)
                if event.key == pygame.K_e:
                    word+=chr(event.key)
                if event.key == pygame.K_f:
                    word+=chr(event.key)
                if event.key == pygame.K_g:
                    word+=chr(event.key)
                if event.key == pygame.K_h:
                    word+=chr(event.key)
                if event.key == pygame.K_i:
                    word+=chr(event.key)
                if event.key == pygame.K_j:
                    word+=chr(event.key)
                if event.key == pygame.K_k:
                    word+=chr(event.key)
                if event.key == pygame.K_l:
                    word+=chr(event.key)
                if event.key == pygame.K_m:
                    word+=chr(event.key)
                if event.key == pygame.K_n:
                    word+=chr(event.key)
                if event.key == pygame.K_o:
                    word+=chr(event.key)
                if event.key == pygame.K_p:
                    word+=chr(event.key)
                if event.key == pygame.K_q:
                    word+=chr(event.key)
                if event.key == pygame.K_r:
                    word+=chr(event.key)
                if event.key == pygame.K_s:
                    word+=chr(event.key)
                if event.key == pygame.K_t:
                    word+=chr(event.key)
                if event.key == pygame.K_u:
                    word+=chr(event.key)
                if event.key == pygame.K_v:
                    word+=chr(event.key)
                if event.key == pygame.K_w:
                    word+=chr(event.key)
                if event.key == pygame.K_x:
                    word+=chr(event.key)
                if event.key == pygame.K_y:
                    word+=chr(event.key)
                if event.key == pygame.K_z:
                    word+=chr(event.key)
    print(word)       
    return word



def is_echec(couleur,plateau):
    pos_roi=position(["Roi",couleur],plateau)
    echec=False
    for i in range(8):
        for j in range(8):
            if vérif([i,j],pos_roi,plateau) :
                echec=True 
    return echec
    
def position(piece,plateau):
    i=0 
    j=0 
    trouvé=False
    while trouvé==False:
        if i+1>7 and j+1 >7:
            return [i,j]
        if plateau[i][j]==piece:
            trouvé=True
        elif [i,j]==[7,7]:
            trouvé = False
        elif i<7:
            i+=1
        elif j<7:
            j+=1 
            i=0
    return [i,j]

def partie(plateau,Joueur="Blanc"):
    en_cours=True
    rock_gauche_blanc=True
    rock_droit_blanc=True
    rock_gauche_noir=True
    rock_droit_noir=True
    pygame.init()
    WIDTH = 600
    HEIGHT = 600
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Jeu d'échecs")
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
        print_plateau(plateau,screen)
        rép=inpt("Quel es ton coup ?")
        print(rép)
        if rép == "0":
            en_cours=False
            print ("Fin du jeu, Vae Victis")
        else:
            try:
                int(rép[0])
                int(rép[1])
                int(rép[2])
                int(rép[3])
            except:
                rép=inpt("Erreur ! Veuillez entrer uniquement des entiers ! Quel es ton coup ?")
                réponse=[[int(rép[0]),int(rép[1])],[int(rép[2]),int(rép[3])]]

            réponse=[[int(rép[0]),int(rép[1])],[int(rép[2]),int(rép[3])]]
            for i in range(2):
                for j in range(2):
                    while réponse[i][j]>=8 or réponse[i][j]<0:
                        réponse=[[int(rép[0]),int(rép[1])],[int(rép[2]),int(rép[3])]]
            if vérif(réponse[0],réponse[1],plateau,rock_gauche_blanc,rock_droit_blanc,rock_gauche_noir,rock_droit_noir)\
                and plateau[réponse[0][0]][réponse[0][1]][1]==Joueur and is_echec(Joueur,duplateau(réponse[0],réponse[1],plateau))==False:
                piece=plateau[réponse[0][0]][réponse[0][1]]
                if piece[0]=="Tour":
                    if réponse[0]==[0,0]:
                        rock_gauche_blanc=False
                    elif réponse[0]==[7,0]:
                        rock_gauche_noir=False
                    elif réponse[0]==[0,7]:
                        rock_droit_blanc=False
                    elif réponse[0]==[7,7]:
                        rock_droit_noir=False
                elif piece[0]=="Roi":
                    if piece[1]=="Blanc":
                        rock_gauche_blanc=False
                        rock_droit_blanc=False
                    elif piece[1]=="Noir":
                        rock_droit_noir=False
                        rock_gauche_noir=False
                elif réponse[1][0]==0 and Joueur=="Noir" and piece[0]=="Pion":
                    is_prom=False
                    while is_prom==False:
                        prom=inpt("Quelle est la promotion que tu souhaites ?")
                        if prom=="dame" or prom=="fou" or prom=="cavalier" or prom=="tour":
                            print(prom.capitalize())
                            plateau[réponse[0][0]][réponse[0][1]][0]=prom.capitalize()
                            is_prom=True
                elif réponse[1][0]==7 and Joueur=="Blanc" and piece[0]=="Pion":
                    is_prom=False
                    while is_prom==False:
                        prom=inpt("Quelle est la promotion que tu souhaites ?")
                        if prom=="dame" or prom=="fou" or prom=="cavalier" or prom=="tour":
                            print(prom.capitalize())
                            plateau[réponse[0][0]][réponse[0][1]][0]=prom.capitalize()
                            is_prom=True
                coup(réponse[0],réponse[1],plateau)
                if Joueur == "Blanc":
                    Joueur="Noir"
                else:
                    Joueur="Blanc"
                if is_echec(Joueur,plateau):
                    if is_mat(Joueur,plateau):
                        en_cours=False
                        print("échec et mat !")
                    else :
                        print("échec !")
            else :
                print("coup invalide")
                    
def print_plateau(plat,screen):
    global wN,wR,wP,wQ,wB,wK,bN,bR,bP,bQ,bB,bK
#on place le plateau vide 
    plateau = pygame.transform.scale(pygame.image.load("images\\Board3.png"),(600, 600))
    screen.blit(plateau,(0, 0))

    positionX= 10
    positionY= 10
    for i in range(len(plat)):
        for j in range(len(plat[i])):
            if plat[i][j][1]== "Blanc":
                if plat[i][j][0] =="Cavalier":
                    screen.blit(wN,(positionX, positionY))
                elif plat[i][j][0] == "Tour":
                    screen.blit(wR,(positionX, positionY))
                elif plat[i][j][0] == "Pion":
                    screen.blit(wP,(positionX, positionY))
                elif plat[i][j][0] == "Dame":
                    screen.blit(wQ,(positionX, positionY))
                elif plat[i][j][0] == "Fou":
                    screen.blit(wB,(positionX, positionY))
                elif plat[i][j][0] == "Roi":
                    screen.blit(wK,(positionX, positionY))

            elif plat[i][j][1]== "Noir":
                if plat[i][j][0] =="Cavalier":
                    screen.blit(bN,(positionX, positionY))
                elif plat[i][j][0] == "Tour":
                    screen.blit(bR,(positionX, positionY))
                elif plat[i][j][0] == "Pion":                 
                    screen.blit(bP,(positionX, positionY))
                elif plat[i][j][0] == "Dame":
                    screen.blit(bQ,(positionX, positionY))
                elif plat[i][j][0] == "Fou":
                    screen.blit(bB,(positionX, positionY))
                elif plat[i][j][0] == "Roi":
                    screen.blit(bK,(positionX, positionY))           
            positionX +=73
        positionY +=73
        positionX = 10
    pygame.display.flip()


"""
    plateau=plat[::-1]
    for i in range(len(plateau)):
        ligne=""
        for j in range(len(plateau[i])):
            piece=plateau[i][j]
            if piece[0]==0:
                ligne+=". "
            elif piece[0]=="Tour":
                if piece[1]=="Blanc":
                    ligne+="R "
                else:
                    ligne+="r "
            elif piece[0]=="Fou":
                if piece[1]=="Blanc":
                    ligne+="B "
                else:
                    ligne+="b "
            elif piece[0]=="Pion":
                if piece[1]=="Blanc":
                    ligne+="P "
                else:
                    ligne+="p "
            elif piece[0]=="Dame":
                if piece[1]=="Blanc":
                    ligne+="Q "
                else:
                    ligne+="q "
            elif piece[0]=="Roi":
                if piece[1]=="Blanc":
                    ligne+="K "
                else:
                    ligne+="k "
            elif piece[0]=="Cavalier":
                if piece[1]=="Blanc":
                    ligne+="N "
                else:
                    ligne+="n "
        print(ligne)
"""     
def fen_plateau(chaine):
    res=[[]]
    pos_courante=0
    ligne=0
    longueur=len(chaine)
    while pos_courante!=longueur:
        char=chaine[pos_courante]
        if char=="/":
            res.append([])
            ligne+=1
        elif char=="1":
            res[ligne].append([0,0])
        elif char=="2":
            for i in range(2):
                res[ligne].append([0,0])
        elif char=="3":
            for i in range(3):
                res[ligne].append([0,0])
        elif char=="4":
            for i in range(4):
                res[ligne].append([0,0])
        elif char=="5":
            for i in range(5):
                res[ligne].append([0,0])
        elif char=="6":
            for i in range(6):
                res[ligne].append([0,0])
        elif char=="7":
            for i in range(7):
                res[ligne].append([0,0])
        elif char=="8":
            for i in range(8):
                res[ligne].append([0,0])
        elif char=="p":
            res[ligne].append(["Pion","Noir"])
        elif char=="r":
            res[ligne].append(["Tour","Noir"])
        elif char=="n":
            res[ligne].append(["Cavalier","Noir"])
        elif char=="b":
            res[ligne].append(["Fou","Noir"])
        elif char=="q":
            res[ligne].append(["Dame","Noir"])
        elif char=="k":
            res[ligne].append(["Roi","Noir"])
        elif char=="P":
            res[ligne].append(["Pion","Blanc"])
        elif char=="R":
            res[ligne].append(["Tour","Blanc"])
        elif char=="N":
            res[ligne].append(["Cavalier","Blanc"])
        elif char=="B":
            res[ligne].append(["Fou","Blanc"])
        elif char=="Q":
            res[ligne].append(["Dame","Blanc"])
        elif char=="K":
            res[ligne].append(["Roi","Blanc"])
        pos_courante+=1
    return res[::-1]


def is_mat(couleur,plateau):
    mat=True
    for i in range(8):
        for j in range(8):
            if plateau[i][j][1]==couleur:
                possib=coups_possible([i,j],plateau)
                for k in possib:
                    if is_echec(couleur,duplateau([i,j],k,plateau))!=True:
                        mat=False
    return mat
                
            
def duplateau(depart,arrivee,plateau):
    plateau_double=deepcopy(plateau)
    coup(depart,arrivee,plateau_double)
    return plateau_double
    
    
    
Plateau_2=fen_plateau("8/8/8/4p3/3P1P2/8/8/8")
Plat = fen_plateau("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
partie(Plat)
pygame.quit()