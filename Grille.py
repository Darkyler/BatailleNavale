# -*- coding: utf-8 -*-

from Position import Position

class Grille:
	def __init__(self,hauteur=19,largeur=19):
		self.hauteur = hauteur
		self.largeur = largeur
		self.positionsOcuppees = []

	def coordonneValide(self,Position):
		# Return true si la position appartient à la grille
		return (Position.getX() <= self.largeur and Position.getX() >= 0 and Position.getY() <= self.hauteur and Position.getY() >= 0)

	def marquerPosition(self,Position):
		# (1) La position n'est pas occupée par un bateau
		if not(self.aUnBateau(Position)) and self.coordonneValide(Position):
			self.positionsOcuppees.append(Position) 
		else:
			raise Exception 


	def aUnBateau(self,Position):
		# Renvoie True si la un bateau se trouve à une position donnée
		res = False
		for PositionCur in self.positionsOcuppees:
			if (Position.getX() == PositionCur.getX() and Position.getY() == PositionCur.getY()):
				res = True
		return res

	def estIntacte(self,Position): 
		# Return True si la case a un bateau et n'a pas déjà été tiré
		res = False
		for PositionCur in self.positionsOcuppees:
			if (Position.getX() == PositionCur.getX() and Position.getY() == PositionCur.getY() and not(PositionCur.get_Tire())):
				res = True
		return res 

	def quelBateau(self,Position):
		# Si Position.aUnBateau()
		for PositionCur in self.positionsOcuppees:
			if (Position.getX() == PositionCur.getX() and Position.getY() == PositionCur.getY()):
				res = PositionCur.getBateau()
		return res

	def enleverPosition(self,Position):
		for PositionCur in self.positionsOcuppees:
			if (Position.getX() == PositionCur.getX() and Position.getY() == PositionCur.getY()):
				PositionCur.set_Tire()

			

	def bateauEnVue(self,Position):
		res = False
		for Pos in self.positionsOcuppees:
			if (Position.getX() == Pos.getX() or Position.getY() == Pos.getY()):
				res = True
		return res




