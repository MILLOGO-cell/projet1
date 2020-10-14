import os
from tkinter import *
import math
import tkinter.messagebox

"""def ressource_path(relative_path):
    base_path = getattr(Sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
image_path=("C:/Users/Mr MILLOGO/Desktop/Calculatrice/calculator.ico")"""

fenetre = Tk()
fenetre.title("CALCULATRICE")
#fenetre.iconbitmap(image_path)
fenetre.geometry("410x445")
fenetre.configure(background="dark slate gray")
fenetre.resizable(width=False, height= False)
##########################GRILLE###############################
boite = Frame(fenetre)
boite.grid()
##############################################################
class calc(object):
	"""docstring for calc"""
	def __init__(self):
		self.total=0
		self.actuel=0
		self.val_entree= True
		self.test_num = False
		self.op=""
		self.resultat = False
	def num_entre(self,num):
		self.resultat = False
		premier_num = ecran.get()
		second_num = str(num)
		if self.val_entree:
			self.actuel= second_num
			self.val_entree = False
		else:
			if second_num ==".":
				if second_num in premier_num:
					return
			self.actuel = premier_num + second_num
		self.display(self.actuel)
		
	def somme_total(self):
		self.resultat = True
		self.actuel = float(self.actuel)
		if self.test_num == True:
			self.valid_function()
		else:
			self.total = float(ecran.get())

	def display(self,value):
		ecran.delete(0, END)
		ecran.insert(0, value)

 

	def valid_function(self):
		if self.operateur == "Addition":
			self.total += self.actuel
		if self.operateur == "Soustraction":
			self.total -= self.actuel
		if self.operateur == "Multiplication":
			self.total *= self.actuel	
		if self.operateur == "Division":
			self.total /= self.actuel
		if self.operateur == "Modulo":
			self.total %= self.actuel
		self.val_entree = True
		self.test_num = False
		self.display(self.total)

	def operation(self, operateur):
		self.actuel = float(self.actuel)
		if self.test_num:
			self.valid_function()
		elif not self.resultat:
			self.total = self.actuel
			self.val_entree = True
		self.test_num = True
		self.operateur = operateur
		self.resultat = False

	def Effacer(self):
		self.resultat= False
		self.actuel="0"
		self.display(0)
		self.val_entree=True

	def Annuler(self):
		ex=ecran.get()
		ex=ex[0:len(ex)-1]
		ecran.delete(0,END)
		ecran.insert(0,ex)

	def Racine(self):
		 self.resultat=False
		 self.actuel = math.sqrt(float(ecran.get()))
		 self.display(self.actuel)

	def Plus_Moins(self):
		self.resultat=False
		self.actuel=-(float(ecran.get()))
		self.display(self.actuel)

	def cosinus(self):
		self.resultat=False
		self.actuel=math.cos(math.radians(float(ecran.get())))
		self.display(self.actuel)
	
	def tan(self):
		self.resultat=False
		self.actuel=math.tan(math.radians(float(ecran.get())))
		self.display(self.actuel)

	def sinus(self):
		self.resultat=False
		self.actuel=math.sin(math.radians(float(ecran.get())))
		self.display(self.actuel)

	def pi(self):
		self.resultat = False
		self.actuel = math.pi
		self.display(self.actuel)

	def tau(self):
		self.resultat = False
		self.actuel = math.tau
		self.display(self.actuel)

	def e(self):
		self.resultat = False
		self.actuel = math.e
		self.display(self.actuel)

	def degre(self):
		self.resultat=False
		self.actuel=math.degrees(float(ecran.get()))
		self.display(self.actuel)

	def log2(self):
		self.resultat=False
		self.actuel=math.log2(float(ecran.get()))
		self.display(self.actuel)

	def log10(self):
		self.resultat=False
		self.actuel=math.log10(float(ecran.get()))
		self.display(self.actuel)

	def log(self):
		self.resultat=False
		self.actuel=math.log(float(ecran.get()))
		self.display(self.actuel)

	def log1p(self):
		self.resultat=False
		self.actuel=math.log1p(float(ecran.get()))
		self.display(self.actuel)
	
	def factoriel(self):
		self.resultat=False
		self.actuel=math.factorial(float(ecran.get()))
		self.display(self.actuel)
	
	def sinh(self):
		self.resultat=False
		self.actuel=math.sinh(float(ecran.get()))
		self.display(self.actuel)

	def cosh(self):
		self.resultat=False
		self.actuel=math.cosh(float(ecran.get()))
		self.display(self.actuel)
	
	def acos(self):
		self.resultat=False
		self.actuel=math.acos(float(ecran.get()))
		self.display(self.actuel)
	
	def asin(self):
		self.resultat=False
		self.actuel=math.asin(float(ecran.get()))
		self.display(self.actuel)

	def atan(self):
		self.resultat=False
		self.actuel=math.atan(float(ecran.get()))
		self.display(self.actuel)

	def rad(self):
		self.resultat=False
		self.actuel=math.radians(float(ecran.get()))
		self.display(self.actuel)
	
	def tanh(self):
		self.resultat=False
		self.actuel=math.tanh(float(ecran.get()))
		self.display(self.actuel)

	def mantisse(self):
		self.resultat=False
		self.actuel=math.frexp(float(ecran.get()))
		self.display(self.actuel)



val_ajoute = calc()	
##########################BARRE DE TACHES#######################
def sortie():
	sortie = tkinter.messagebox.askyesno("MILLOGO CALCULATOR", "Voulez-vous confirmez votre sortie?")
	if sortie>0:
		fenetre.destroy()
		return
def scientifique():
	fenetre.resizable(width=False, height= False)
	fenetre.geometry("814x445")
	

def standard():
	fenetre.resizable(width=False, height= False)
	fenetre.geometry("410x445")
	
menubar = Menu(boite)

menu_fich= Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Menu", menu=menu_fich)
menu_fich.add_command(label="Standard", command = standard )
menu_fich.add_command(label="Scientifique", command= scientifique)
menu_fich.add_separator()
menu_fich.add_command(label="Sortie",command = sortie)
fenetre.config(menu=menubar)

###########################ECRAN###################################
ecran = Entry(boite,font=('arial',22,'bold'),bd=4,justify=RIGHT)
ecran.grid(row=0, column=0, columnspan=4, pady=10)
ecran.insert(0,"PRêT!")
###############################################################

#########################PAVE NUMERIQUE#######################
pave_num="789456123"
i=0
bouton=[]
for j in range (2,5):
    for k in range(3):
        bouton.append(Button(boite, width=7,height=2, font=('arial',15,'bold'),bd=6,text= pave_num[i]))
        bouton[i].grid(row = j, column = k, pady = 0)
        bouton[i] ["command"]=lambda x = pave_num[i]:val_ajoute.num_entre(x)
        i+=1
#######################################################################################################

############################################BOUTONS STANDARD##########################################################
boutton_Effacer= Button(boite, text=("EFFACER"),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command= val_ajoute.Effacer).grid(row=1, column= 0, pady=0)

boutton_annuler= Button(boite, text=("<=|"),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = val_ajoute.Annuler).grid(row=1, column=1, pady=1)

boutton_racine= Button(boite, text=("√"),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = val_ajoute.Racine).grid(row=1, column=2, pady=1)

boutton_addition= Button(boite, text=("+"),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = lambda: val_ajoute.operation("Addition")).grid(row=1, column=3, pady=1)

boutton_soustraction= Button(boite, text=("-"),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = lambda: val_ajoute.operation("Soustraction")).grid(row=2, column=3, pady=1)

boutton_multiplication= Button(boite, text=("x"),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = lambda: val_ajoute.operation("Multiplication")).grid(row=3, column=3, pady=1)

boutton_division =Button(boite, text=chr(247),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = lambda: val_ajoute.operation("Division")).grid(row=4, column=3, pady=1)

boutton_zero= Button(boite, text=("0"),width=7, height=2, font=('arial',15,'bold'),bd=6
                      ,command=lambda:val_ajoute.num_entre(0)).grid(row=5, column=1, pady=1)

boutton_virgule= Button(boite, text=("."),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = lambda: val_ajoute.num_entre (".")).grid(row=5, column=2, pady=1)

boutton_plus_moins= Button(boite, text=chr(177),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command=val_ajoute.Plus_Moins).grid(row=5, column=0, pady=1)

boutton_egale= Button(boite, text=("="),width=7, height=2, font=('arial',15,'bold'),bd=6,
                        bg="red",command = val_ajoute.somme_total).grid(row=5, column=3, pady=1)
#############################################################################################################

########################################BOUTONS SCINTIFIQUE##################################################
boutton_pi = Button(boite, text="π", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.pi).grid(row=3, column=4, pady=0)

boutton_cos = Button(boite, text="cos", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.cosinus).grid(row=3, column=5, pady=0)

boutton_tan = Button(boite, text="tan", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.tan).grid(row=3, column=6, pady=1)

boutton_sin = Button(boite, text="sin", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.sinus).grid(row=4, column=4, pady=1)


bouton_log = Button(boite, text="log", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.log).grid(row=4, column=7, pady=1)


bouton_tanh = Button(boite, text="tanh", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command = val_ajoute.tanh).grid(row=4, column=6, pady=1)

bouton_e = Button(boite, text="e", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.e).grid(row=3, column=7, pady=1)

bouton_deg = Button(boite, text="deg", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.degre).grid(row=4, column=5, pady=1)

bouton_loglp= Button(boite, text="loglp", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command=val_ajoute.log1p).grid(row=5, column=5, pady=1)


bouton_log2 = Button(boite, text="log2", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command=val_ajoute.log2).grid(row=5, column=6, pady=1)

bouton_log10 = Button(boite, text="log10", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.log10).grid(row=5, column=7, pady=1)

bouton_2pi = Button(boite, text="2π", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.tau).grid(row=5, column=4, pady=0)    

bouton_facto = Button(boite, text="!", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.factoriel).grid(row=1, column=4, pady=0)    

bouton_sinh = Button(boite, text="sinh", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.sinh).grid(row=1, column=5, pady=0)    

bouton_acos = Button(boite, text="acos", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.acos).grid(row=1, column=6, pady=0)    

bouton_asin = Button(boite, text="asin", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.asin).grid(row=1, column=7, pady=0)    

bouton_atan = Button(boite, text="atan", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.atan).grid(row=2, column=4, pady=0)    

bouton_rad = Button(boite, text="rad", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.rad).grid(row=2, column=5, pady=0)    

bouton_cosh = Button(boite, text="cosh", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.cosh).grid(row=2, column=6, pady=0)

bouton_mantisse = Button(boite, text="mantissse", width =7,height=2, font=('arial',15,'bold'), bd=6,
	bg="powder blue",command =val_ajoute.mantisse).grid(row=2, column=7, pady=0)                   
######################################################################################################

####################################TEXTE "Mode Scientique"####################################
lbdisplay = Label(boite, text="Mode Scientifique",font=('arial',28,'bold'),justify=CENTER)    #
lbdisplay.grid(row = 0, column= 4, columnspan =4)                                             #
###############################################################################################


fenetre.mainloop()