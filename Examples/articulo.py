"""
   Felipe Deaza - 23ft
   Modelo SIR en python!
   2022
   
   Second Version
"""

from sympy import *
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

class Article():
    def __init__(self, S0 = 0, I0 = 0, R0 = 0, B = 0, Y = 0, v = 0, e = 0, Xo = 0, Xf = 0, n = 0):
        
        """ Propieties Graphs """
        self.solution = None
        self.solutionWithVaccine = None
        self.figure_model_sir = None
        self.ax1 = None
        self.ax2 = None
        self.ax3 = None
        self.figure = None
        
        """ Initial Values """
        self.S0 = S0  # suceptibles en semana 0
        self.I0 = I0     # infectados en semana 0
        self.R0 = R0      # resistentes en semana 0

        """ Constants """
        self.B = 3.61e-5  # tasa de contagio
        self.Y = 3.47     # coeficiente retiro natural
        self.N = self.S0+ self.I0+ self.R0 # numero individuos
        self.v = 0.20     # indice cobertura vacunal
        self.e = 0.67     # indice eficacia vacuna

        self.Xo = 0
        self.Xf = 51
        self.n = 52
        
        self.simulation_time = None
        self.y0 = [self.S0, self.I0, self.R0]
    
    def updateValues(self, S0 = 0, I0 = 0, R0 = 0, B = 0, Y = 0, v = 0, e = 0, Xo = 0, Xf = 0, n = 0):
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.B = B
        self.Y = Y

        self.v = v
        self.e = e
        self.Xo = Xo
        self.Xf = Xf
        self.n = n
        
        self.N = self.S0+ self.I0+ self.R0
        
    def _grafica_resistentes(self):
       plt.plot(self.simulation_time, self.solution[0][:,2], lw = 1.5, color = 'purple')
       plt.plot(self.simulation_time, self.solutionWithVaccine[0][:,2], lw = 1.5, color = 'brown')
       plt.title('$Resistentes$ $R_{(t)}$')
       plt.xlabel('$t_{(weeks)}$')
       plt.ylabel('$R_{(t)}$')
       plt.legend(labels=["$not$ $vaccine$", "$vaccine$"])
       plt.grid(True)
       plt.savefig('resistentes.pdf')
       plt.show()

    def _grafica_infectados(self):
       plt.plot(self.simulation_time, self.solution[0][:,1], lw = 1.5, color = 'red')
       plt.plot(self.simulation_time, self.solutionWithVaccine[0][:,1], lw = 1.5, color = 'orange')
       plt.xlabel('$t_{(weeks)}$')
       plt.ylabel('$I_{(t)}$')
       plt.title('$Infectados$ $I_{(t)}$')
       plt.legend(labels=["$not$ $vaccine$", "$vaccine$"])
       plt.grid(True)
       plt.savefig("infectados.pdf")
       plt.show()

    def _grafica_sucep(self):
       plt.plot(self.simulation_time, self.solution[0][:,0], lw = 1.5, color = 'green')
       plt.plot(self.simulation_time, self.solutionWithVaccine[0][:,0], lw = 1.5, color = 'blue')
       plt.subplots_adjust(left=0.19)
       plt.title('$Suceptibles$ $S_{(t)}$')
       plt.xlabel('$t_{(weeks)}$')
       plt.ylabel('$S_{(t)}$')
       plt.legend(labels=["$not$ $vaccine$", "$vaccine$"])
       plt.grid(True)
       plt.savefig('suceptilbles.pdf')
       plt.show()

    def graficacion(self):
       """ Graficacion """
       
       
       self.figure, (self.ax1, self.ax2, self.ax3) = plt.subplots(1, 3, figsize=(10,5), constrained_layout=True)
       self.figure.suptitle('Modelo SIR -  Python')
    
       self.ax1.plot(self.simulation_time, self.solution[0][:,0], lw = 1.5, color = 'green')
       self.ax1.plot(self.simulation_time, self.solutionWithVaccine[0][:,0], lw = 1.5, color = 'blue')
       self.ax1.set_title('$Suceptibles$ $S_{(t)}$')
       self.ax1.set_xlabel('$t_{(weeks)}$')
       self.ax1.set_ylabel('$S_{(t)}$')
       self.ax1.legend(labels=["$not$ $vaccine$", "$vaccine$"])
       self.ax1.grid(True)

       self.ax2.plot(self.simulation_time, self.solution[0][:,1], lw = 1.5, color = 'red')
       self.ax2.plot(self.simulation_time, self.solutionWithVaccine[0][:,1], lw = 1.5, color = 'orange')
       self.ax2.set_xlabel('$t_{(weeks)}$')
       self.ax2.set_ylabel('$I_{(t)}$')
       self.ax2.set_title('$Infectados$ $I_{(t)}$')
       self.ax2.legend(labels=["$not$ $vaccine$", "$vaccine$"])
       self.ax2.grid(True)

       self.ax3.plot(self.simulation_time, self.solution[0][:,2], lw = 1.5, color = 'purple')
       self.ax3.plot(self.simulation_time, self.solutionWithVaccine[0][:,2], lw = 1.5, color = 'brown')
       self.ax3.set_title('$Resistentes$ $R_{(t)}$')
       self.ax3.set_xlabel('$t_{(weeks)}$')
       self.ax3.set_ylabel('$R_{(t)}$')
       self.ax3.legend(labels=["$not$ $vaccine$", "$vaccine$"])
       self.ax3.grid(True)

       #plt.show()
    
       return self.figure

    def Vacunados(self, N,v,e):
        """ Aplicando la formula V = (Nve)/9 --> para el calculo numero individuos vacunados cada semana """
        return ((N*v*e)/9) 

    def modelWithVaccine(self, t, x, B, Y, N,v,e):

       S = x[0] # suceptibles
       I = x[1] # infectados
       R = x[2] # resistentes
    
       """ Funcion a trozo Vacunados """
       V = self.Vacunados(self.N,self.v,self.e) if ((t>9) and (t <= 18)) else 0 # Individuos vacunados
    
       """ Sistema ecuaciones ordenado """
       dS = -(B*I*S) - V
       dI = (B*I*S) - (Y*I)
       dR = (Y*I) + V
    
       return [dS, dI, dR]

    def modelWithoutVaccine(self, t, x, B, Y):

       S = x[0] # suceptibles
       I = x[1] # infectados
       R = x[2] # resistentes
    
       """ Sistema ecuaciones ordenado """
       dS = -(B*I*S)
       dI = (B*I*S) - (Y*I)
       dR = (Y*I)
    
       return [dS, dI, dR]

    def updateSolution(self, n):
        
        self.simulation_time = np.linspace(self.Xo,self.Xf, n) # del 0 al 10, 2501 datos.
        self.y0 = [self.S0, self.I0, self.R0]
        self.N = self.S0+ self.I0+ self.R0
        
        self.solution = odeint(self.modelWithoutVaccine, self.y0, self.simulation_time, full_output=True, tfirst=True, args=(self.B, self.Y))
        self.solutionWithVaccine = odeint(self.modelWithVaccine, self.y0, self.simulation_time, full_output=True, tfirst=True, args=(self.B, self.Y, self.N,self.v,self.e))
        
        return self.solution, self.solutionWithVaccine, self.simulation_time
        
    def showGraphic(self):
        self.figure_model_sir = self.graficacion()
        
        
