from Joueur import Joueur
class Partie:
	def __init__(self):
		self.joueur1 = Joueur()
		self.joueur2 = Joueur()

		# un peu d'la merde lol
		self.premierJoueur = self.joueur1
		self.JoueurSuivant = self.joueur2


		self.joueurActif = self.joueur1
		self.tour=0
		# Accesseurs vers les grilles des joueurs:
		# self.joueur1.get_Grille()
		# self.joueur2.get_Grille()

	def get_joueur1(self):
		return self.joueur1

	def get_joueur2(self):
		return self.joueur2


	def set_PremierJoueur(self,premierJoueur):
		self.premierJoueur(premierJoueur)

	def joueurSuivant(self):
		self.tour = self.tour + 1
		if (self.tour % 2 == 0):
			self.joueurActif = self.premierJoueur
		else:
			self.joueurActif = self.JoueurSuivant

		

	def get_JoueurActif(self):
		return self.joueurActif

	def get_JoueurSuivant(self):
		return self.JoueurSuivant






