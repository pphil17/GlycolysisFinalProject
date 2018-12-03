#!/usr/bin/env python

 #Cells use one of two methods to break down glucose and produce ATP, efficient aerobic pathway that requires oxygen or using glycolysis, an inefficient anaerobic pathway.
 #Glycolysis is the metabolic process of breaking down carbohydrates, such as glucose, and making enzymes & ATP. Glycolysis is part of the anaerobic pathway and is used when oxygen levels are too low and cannot support the level of ATP being produced
 #The model assumes that cells have a target level of ATP demand. The model is testing what happens to cells under anaerobic conditions (glycolysis), during ten generations, depending on the ATP levels produced.
master
class glycolytic pathway:
    def __init__(self,number,generations):
        self.number=Cell number
        self.generation= generations
        Cell number=[10]
        generations=[10]
    def reproduction (self):
        #cell meets ATP limit and reproduces
        for gen in range(generations):
            if fA=>0.8:
                Cellnumber=Cellnumber[-1]*2
        #cell didn't meet ATP limit necessary to reproduce, but has enough ATP to survive (cell goes into a state similar to G0).
            elif:
                fA=>0.3
                Cellnumber=cellnumber[-1]
        #Cell didn't meet ATP limit to reproduce or survive.
            elif:
                fA=0.3
                Cellnumber=0
                Cellnumber.append(Cellnumber)
    def printgraph (self):
        
#ATP production determines the behavior of the cell
#ATP demand is higher for cancer cells than in a normal cell, so ATP production has to be higher in order for cell to reproduce
#ATP provides cells with energy, but a certain amount of ATP has to be produced to allow cells to survive and reproduce.  

        #equation for oxygen con
 Vo=0.012

O=0.056

Ko=0.05

Fo=Vo*(O/(O+Ko))

Fo
Out[8]: 0.006339622641509434

#ATP levels are determined by glucose consumption and oxygen concentration
#Oxygen consumption fO is determined by oxygen concentration (cells use glycolysis or areobic pathway)
#since the cells are using glycolysis, oxygen con is low/near zero. Shows oxygen concentration is insufficient and cells will use glycolysis to produce ATP
#Under the Warburg effect cancer cells will undergo Glycolysis, regardless of the oxygen concentration
  

#user input to modify equation to begin tests

#class glycolytic pathway:
class glycolytic:
    def __init__(self,Oxygencon,Glucosecon,Protonprd,ATPprodc):
	self.Oxygencon = Oxygencon
	self.Glucosecon = Glucosecon
	self.Protonprd = Protonprd
	sel.ATPprodc = ATPprodc


       #equation for oxygen con
#Oxygen consumption determines oxygen concentration (which, in normal cells, determines if cells use glycolysis or areobic pathway)
#The equations for oxygen concentration, ATP production, glucose concentration, and proton production will be the same as it is in non-glycolysis pathway
                   
 master
        #equation for gluco con
#Cells uses glucose to produce ATP, but glycolysis is an insuffiecient way of producing ATP (2 ATP per glucose molecule broken down)
#Glucose consumption is driven by the need to meet ATP demand.
#pG is a multiplier representing the altered glucose metabolism seen in many tumor cells (i.e., the Warburg effect), G is the amount of glucose, Kg is the half-max concentration of glucose, pG
import numpy as np

pG = np.linspace(0, 1, 100)
Ao=0.1
G=5
Kg=0.04
Fg=-(((1*0.1/2)+(27*Fo/10))*(5/(5+0.04)))
        #equation for proton prd

        #equation for ATP prd
Fg=Fg
Fo=Fo
Fa=-(((2*Fg)+(27*Fo))/5)


    #Model tests cell reproduction under aerobic (non-glycolytic) pathway for ten generations
master
class non-glycolytic pathway
def __init__(self,number,generations):
        self.number=Cell number
        self.generation= generations
        Cell number=[10]
        generations=[10]
    def reproduction (self):


#Cancer cells under the Warburg effect will choose to undergo Glycolysis no matter the amount of oxygen present
#class non-glycolytic pathway equations same as glycolytic pathway.
    #def __init__(self,Oxygencon,Glucoseconc,prtonprd,atpprodcn)
 master
        #equation for Oxygencon
        #equation for glucose
        #equation for ATP prd
#ATP prd will be higher in cells that use non-glycolytic pathway, produces 36 ATP

#Proton production, Fh, is linked to the amount of glycolysis that does not feed the aerobic pathway
#equation for proton prd, kH accounts for the parameter of proton buffering
  if fa >= 0.8:
        return{ number*2 }
#this is a rough draft
        else
         fa <= 0.3:


        kH = 0.00025
        pG = pG
        Vo =0.012
        fo = fo

        return fH = kH * 5.8 * pG * ( Vo + fo )
Fg=Fg
fo=fo
Fa=-(((2*Fg)+(27*fo))/5)
#Fa, ATP production necessary for  cell reproduction
#fa, proton production, if it meets proton limit will acidify normal cells and allow cancer cells, which are better equipped to handle acidity, to reproduce

#sets up how ATP production and cell pH will affect cell numbers and generations
#ATP prod increases >>cell pH will become become lower (more acidic)
#Cancer cell generations will increase, while normal cell populations will decrease

#Testing how varying ATP prod rates will affect cell generations (what is the threshhold for death or reproduction of cells).
class cell:
    def __init__(self, number, ATPfa, cellpH, generation):
        self.number = number
        self.ATPfa = ATPfa
        self.cellpH = cellpH
        self.generation = generation
        #number of cells
        #threshhold for death of cells
        #threshhold for reproduction(cell number of surviving cells double)

class cell:
    def __init__(self, number, ATPfa, cellpH, generation):
        self.number = number
        self.ATPfa = ATPfa
        self.cellpH = cellpH
        self.generation = generation
        #number of cells
        #threshhold for death of cells
        #threshhold for reproduction(cell number of surviving cells double)
        #how ATP affects the threshhold
Living = cell("GenOne", > = 0.8, 6.1, 2)
Duplicating = cell("GenOne" 

#Plotting effects of increased altered metabolism of cancer cells vs. amount of hydrogens produced (changes in acidity)
#Cancer cells increase acidity of surronding environment to eliminate normal cells and then invade tissue
#The x values represent cancer cell's altered metabolism (increased intake of glucose and oxygen), if large enough, will affect the y values (increased proton production). 
import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [1,2,4,7,4]
plt.scatter(pG, Hydrogen_Prod, label='No of hydrogens produced', color='c', marker='^')

plt.xlabel('pG')
plt.ylabel('Hydrogen_Prod')
plt.title('H vs pG')
plt.legend()
plt.show()
master
    
master
    
#In order for cancer cells to kill off competition (normal cells), they make the microenvironment more acidic

