#!/usr/bin/env python3

from math import inf

class leplusCourtChemin:

    def __init__(self,graphe,depart,arrivee):
      
      self.graphe = graphe
      self.depart = depart
      self.arrivee = arrivee
      self.marque, self.pere = self.dijkstra()


    def mini(listeSommets, marque):
        """Renvoie le sommet de listeSommets ayant la plus petite marque.

        In : liste listeSommets et dictionnaire de noms de sommets associés     à des marques inou inf
        Out: string sommetPlusPetit
        """
        marquePlusPetite = inf
        sommetPlusPetit = None
        for sommet in listeSommets:
            if marque[sommet] < marquePlusPetite:
                marquePlusPetite = marque[sommet]
                sommetPlusPetit = sommet
        return sommetPlusPetit
        
    mini = staticmethod(mini) 

    def dijkstra(self):
        """Renvoie le les marques présentes à la fin de l'algorithme dijikstra et chemin le plus court entre les sommets depart et arrivee.

        In : object leplusCourtChemin
        Out: dict marque et dict pere
        """
        # initialisation
        marque = {}
        for sommet in self.graphe:
            marque[sommet] = inf
        marque[self.depart] = 0

        non_selectionnes = [sommet for sommet in self.graphe]

        pere = {}
        pere[self.depart] = None

        # boucle principale:
        while non_selectionnes:
        # sélection:
            sommetPlusPetit = leplusCourtChemin.mini(non_selectionnes,marque)
            if sommetPlusPetit == self.arrivee:
                break
            non_selectionnes.remove(sommetPlusPetit)
        # mise à jour des voisins du sommet sélectionné:
            VoisinsAVisiter = [sommet for sommet in self.graphe[sommetPlusPetit] if sommet in non_selectionnes]
            for sommet in VoisinsAVisiter:
                p = marque[sommetPlusPetit] + self.graphe[sommetPlusPetit][sommet]
                if p < marque[sommet]:
                    marque[sommet] = p
                    pere[sommet] = sommetPlusPetit
        return marque, pere

    def affichageCheminMin(self):
        """Renvoie une string donnant le chemin le plus court de depart a arrivee en appelant le fonction dijikstra

        In : object leplusCourtChemin
        Out: string
        """
        distance = self.marque
        pere = self.pere
        print("La distance de {} à {} est de longueur {}.".format(self.depart, self.arrivee, distance[self.arrivee]))
        chemin = self.arrivee
        sommet = self.arrivee
        while pere[sommet] != None:
            chemin = pere[sommet] +' - '+ chemin
            sommet = pere[sommet]
        print("Le chemin de {} à {}: {}.".format(self.depart, self.arrivee,chemin))

if __name__ == "__main__":
    graphe_longueur = {
        'Parme':{'La Spézia':124, 'Bologne':104},
        'La Spézia':{'Parme':124, 'Florence':163},
        'Bologne':{'Parme':104, 'Florence':131, 'Pérouse': 245},
        'Florence':{'La Spézia':163,'Bologne':131,'Pérouse': 150, 'Rome':283},
        'Pérouse':{'Bologne':245, 'Florence':150, 'Rome':181},
        'Rome':{'Florence':283, 'Pérouse':181},
    }

    graphe_vitesse = {
        'Parme':{'La Spézia':83, 'Bologne':71},
        'La Spézia':{'Parme':83, 'Florence':106},
        'Bologne':{'Parme':71, 'Florence':99, 'Pérouse': 174},
        'Florence':{'La Spézia':106,'Bologne':99,'Pérouse': 103, 'Rome':168},
        'Pérouse':{'Bologne':174, 'Florence':103, 'Rome':127},
        'Rome':{'Florence':168, 'Pérouse':127},
    }
    
    graphe_éco = {
        'Parme':{'La Spézia':25, 'Bologne':15},
        'La Spézia':{'Parme':25, 'Florence':43},
        'Bologne':{'Parme':15, 'Florence':22, 'Pérouse': 3},
        'Florence':{'La Spézia':43,'Bologne':22,'Pérouse': 20, 'Rome':42},
        'Pérouse':{'Bologne':30, 'Florence':20, 'Rome':22},
        'Rome':{'Florence':42, 'Pérouse':22},
    }
    print("\nLongueur\n")
    C1 = leplusCourtChemin(graphe_longueur, 'Parme', 'Rome')
    C1.affichageCheminMin()
    print("\nVitesse\n")
    C2 = leplusCourtChemin(graphe_vitesse, 'Parme', 'Rome')
    C2.affichageCheminMin()
    print("\nPrix\n")
    C3 = leplusCourtChemin(graphe_éco, 'Parme', 'Rome')
    C3.affichageCheminMin()
