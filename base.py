"""
   Felipe Deaza - 23ft
   Model SIR APP - PyQt5
   2022
   
   First Version.
"""

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                               QHBoxLayout, QVBoxLayout, QBoxLayout, QMainWindow, QFrame, QMenu, QTabWidget, QComboBox, QGridLayout, QTableWidget)
from PyQt5.QtCore import Qt, QSize, QPointF, QRect, QMargins, QAbstractTableModel
from PyQt5.QtGui import QLinearGradient, QPalette, QColor, QIcon, QPixmap, QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from Examples.articulo import Article
from styles.style import *
import sys

""" App Objets - App Widgets """

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100, sol1 = 0, sol2 = 0, time = 0):
        #fig = Figure(figsize=(width, height), dpi=dpi)
        
        fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(1, 3, figsize=(10,5), constrained_layout=True)
        
        self.ax1.plot(time, sol1[0][:,0], lw = 1.5, color = 'green')
        self.ax1.plot(time, sol2[0][:,0], lw = 1.5, color = 'blue')
        self.ax1.set_title('$Suceptibles$ $S_{(t)}$')
        self.ax1.set_xlabel('$t_{(weeks)}$')
        self.ax1.set_ylabel('$S_{(t)}$')
        self.ax1.legend(labels=["$not$ $vaccine$", "$vaccine$"])
        self.ax1.grid(True)
        
        self.ax2.plot(time, sol1[0][:,1], lw = 1.5, color = 'red')
        self.ax2.plot(time, sol2[0][:,1], lw = 1.5, color = 'orange')
        self.ax2.set_xlabel('$t_{(weeks)}$')
        self.ax2.set_ylabel('$I_{(t)}$')
        self.ax2.set_title('$Infectados$ $I_{(t)}$')
        self.ax2.legend(labels=["$not$ $vaccine$", "$vaccine$"])
        self.ax2.grid(True)

        self.ax3.plot(time, sol1[0][:,2], lw = 1.5, color = 'purple')
        self.ax3.plot(time, sol2[0][:,2], lw = 1.5, color = 'brown')
        self.ax3.set_title('$Resistentes$ $R_{(t)}$')
        self.ax3.set_xlabel('$t_{(weeks)}$')
        self.ax3.set_ylabel('$R_{(t)}$')
        self.ax3.legend(labels=["$not$ $vaccine$", "$vaccine$"])
        self.ax3.grid(True)

        super(MplCanvas, self).__init__(fig)


class SecondTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        # layout para el objeto SecondTabWidget.
        self.layout = QVBoxLayout(self)

        # Instacia QtabWidget.
        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        self.tabs.setFixedWidth(1000)
        
        # pestaña 1
        self.tab1 = QFrame(self)    # Primera pestaña, se pasa como widget.
        # self.tab1.setFrameShape(QFrame.NoFrame)
        # self.tab1.setFrameShadow(QFrame.Sunken)
        self.tab1.setAutoFillBackground(True)
        self.tab1.setStyleSheet("""
                                    background-color: white;
                                    
                                """) # #B2B2B2

        # pestaña 2
        self.tab2 = QWidget()   # Segunda pestaña, se pasa como widget.

        # pestaña 3
        self.tab3 = QWidget()   # Tercera pestaña, se pasa como widget.

        # Add new tabs in QtabWidget.
        self.tabs.addTab(self.tab1, "SIR - Model")
        #self.tabs.addTab(self.tab2, "Transistores")
        #self.tabs.addTab(self.tab3, "Modulos-PCB")  # Añadimos pestañas a tabs.

        # añadimos el widget en layout de SecondTabWidget.
        self.layout.addWidget(self.tabs)

        # definimos el layout.
        self.setLayout(self.layout)


class FirstTabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()  # Objeto tabwidgte permite tener pestañas.
        
        
        
        self.tab1 = QWidget()    # Primera pestaña, se pasa como widget.
        self.tab1.setObjectName("tab1_firts")
        
        
        self.tab2 = QWidget()   # Segunda pestaña, se pasa como widget.
        self.tab3 = QWidget()   # Tercera pestaña, se pasa como widget.

        #self.tabs.setFixedWidth(380)
        self.tabs.setStyleSheet("""
                                    background-color: white;

                                """)

        self.tabs.addTab(self.tab1, "User Panel")
        #self.tabs.addTab(self.tab2, "RK2")
        #self.tabs.addTab(self.tab3, "RK2")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def menuHand(self):
        print("pepe")

""" App Widnows """

class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        """ Propieties AppMain """
        self.widget_db = QWidget()          # widget for storage grid layout.
        self.grid_layout = QGridLayout()    # grid layout for data base registers.
        self.rows = None        # rows in grid layout.
        self.Columns = None     # columns in grid layout.
        self.w = 1240           # width window.
        self.h = 480            # height window.
        
        """  Values For Upgrade Graphs"""
        self.sol1 = None
        self.sol2 = None
        self.time = None
        
        """ Configuration AppMain"""
        self.setWindowTitle("Model SIR [Differencial Equations] - 23ft")
        self.setFixedSize(self.w, self.h)   # config initial size.
        self.setStyleSheet(main_css)        # define style sheet 
        
        """ Build Widget """
        self.initUi()

    def initUi(self):

        """
            <MainDiv>
            Principal Div Block in AppMain
        """
        self.frame = QFrame(self)               #frame Main.
        self.frame.setObjectName("AppMainFrame")
        #self.frame.setFrameShape(QFrame.NoFrame)
        #self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setAutoFillBackground(True)
        self.frame.setFixedWidth(self.w)
        self.frame.setFixedHeight(self.h)

        
        self.mainbox = QHBoxLayout(self.frame)  # layout, first block of tabs and second block of tabs.
        self.first = FirstTabWidget()           # first block of tabs
        self.second = SecondTabWidget()         # second block of tabs
        
        self.first.tabs.setFixedWidth(260)      
        """ 
            <FirstTabWidget>
            Actions Data Base 
        """
        self.layout_tools = QVBoxLayout()
        self.layout_tools.setContentsMargins(0,0,0,0)   # quitar magins del layout.
        #self.layout_tools.setAlignment(Qt.AlignCenter)
        
        self.first_frame = QFrame()
        self.first_frame.setFixedWidth(300)
        self.first_frame.setObjectName("FirstFrame")
        self.first_frame.setStyleSheet(firstTab_Frames_css)
        
        self.second_frame = QFrame()
        self.second_frame.setObjectName("SecondFrame")
        self.second_frame.setFixedWidth(300)
        self.second_frame.setStyleSheet(firstTab_Frames_css)
        #self.second_frame.setFrameShape(QFrame.NoFrame)
        #self.second_frame.setFrameShadow(QFrame.Sunken)
        #self.second_frame.setAutoFillBackground(True)
        
        """ Suceptibles values """
        c = 40
        c1 = 5
        c2 = -5
        c3 = 40
        
        """
            Initial Values
        """
        self.label_initial = QLabel("Initial Values SIR", self.first_frame)
        self.label_initial.setObjectName("init_values_label")
        self.label_initial.setStyleSheet(init_values_panel)
        self.label_initial.move(65+c1, 10+c2)
        
        """ Suceptibles S0"""
        self.label_s = QLabel("S0", self.first_frame)
        self.label_s.setObjectName("s-label")
        self.label_s.move(32+c3-55,  14+c+10-20)
        self.label_s.setStyleSheet(qlabel_css_params)
        
        self.entry_s0 = QLineEdit(self.first_frame)
        self.entry_s0.setFixedWidth(70)
        self.entry_s0.setPlaceholderText("Init S")
        self.entry_s0.setClearButtonEnabled(True)
        self.entry_s0.move(65+c3-55-10, 12+c+10-20)
        self.entry_s0.returnPressed.connect(self.update_canvas)
        
        """ Xo value"""
        self.label_x0 = QLabel("Xo", self.first_frame)
        self.label_x0.setObjectName("s-label")
        self.label_x0.move(32+c3+62,  14+c+10-20)
        self.label_x0.setStyleSheet(qlabel_css_params)
        
        self.entry_x0 = QLineEdit(self.first_frame)
        self.entry_x0.setFixedWidth(70)
        self.entry_x0.setPlaceholderText("Xo")
        self.entry_x0.setClearButtonEnabled(True)
        self.entry_x0.move(65+c3+62-10, 12+c+10-20)
        
        """ Xf value"""
        
        self.label_xf = QLabel("Xf", self.first_frame)
        self.label_xf.setObjectName("s-label")
        self.label_xf.move(32+c3+62,  35+c+15-20)
        self.label_xf.setStyleSheet(qlabel_css_params)
        
        self.entry_xf = QLineEdit(self.first_frame)
        self.entry_xf.setFixedWidth(70)
        self.entry_xf.setPlaceholderText("Xf")
        self.entry_xf.setClearButtonEnabled(True)
        self.entry_xf.move(65+c3+62-10, 33+c+15-20)
        
        """ n values """
        self.label_n = QLabel("n", self.first_frame)
        self.label_n.setObjectName("r-label")
        self.label_n.move(32+c3+62,  56+c+20-20)
        self.label_n.setStyleSheet(qlabel_css_params)
        
        self.entry_n = QLineEdit(self.first_frame)
        self.entry_n.setFixedWidth(70)
        self.entry_n.setPlaceholderText("n")
        self.entry_n.setClearButtonEnabled(True)
        self.entry_n.move(65+c3+62-10, 54+c+20-20)
        
        """ Infected values """
        self.label_i = QLabel("I0", self.first_frame)
        self.label_i.setObjectName("i-label")
        self.label_i.move(32+c3-55,  35+c+15-20)
        self.label_i.setStyleSheet(qlabel_css_params)
        
        self.entry_i0 = QLineEdit(self.first_frame)
        self.entry_i0.setFixedWidth(70)
        self.entry_i0.setPlaceholderText("Init I")
        self.entry_i0.setClearButtonEnabled(True)
        self.entry_i0.move(65+c3-55-10, 33+c+15-20)
        
        """ Resistents values """
        self.label_r = QLabel("R0", self.first_frame)
        self.label_r.setObjectName("r-label")
        self.label_r.move(32+c3-55,  56+c+20-20)
        self.label_r.setStyleSheet(qlabel_css_params)
        
        self.entry_r0 = QLineEdit(self.first_frame)
        self.entry_r0.setFixedWidth(70)
        self.entry_r0.setPlaceholderText("Init R")
        self.entry_r0.setClearButtonEnabled(True)
        self.entry_r0.move(65+c3-55-10, 54+c+20-20)
        
        """ Poblacion Total """
        self.total_poblacion = QLabel("N (Poblacion Total)", self.first_frame)
        self.total_poblacion.setObjectName("poblacion_total")
        self.total_poblacion.setStyleSheet(qlabel_css_twoframe)
        self.total_poblacion.move(32+c3-60,  56+c+50-20)
        
        self.entry_poblation = QLineEdit(self.first_frame)
        self.entry_poblation.setFixedWidth(90)
        self.entry_poblation.setPlaceholderText("Total Poblation")
        self.entry_poblation.setClearButtonEnabled(True)
        self.entry_poblation.move(32+c3+10-60,  56+c+70-20)
        
        self.stepsize = QLabel("h (Step Size)", self.first_frame)
        self.stepsize.setObjectName("step_size")
        self.stepsize.setStyleSheet(qlabel_css_twoframe)
        self.stepsize.move(32+c3+85,  56+c+50-20)
        
        self.entry_stepsize = QLineEdit(self.first_frame)
        self.entry_stepsize.setFixedWidth(90)
        self.entry_stepsize.setPlaceholderText("Step Size")
        self.entry_stepsize.setClearButtonEnabled(True)
        self.entry_stepsize.move(32+c3+10+65,  56+c+70-20)
        
        
        #self.button_insert = QPushButton("Insert", self.second_frame)
        #self.button_insert.setStyleSheet("background-color: #9C3D54")
        #self.button_insert.setObjectName("button_insert")
        #self.button_insert.setFixedWidth(135)
        #self.button_insert.setFixedHeight(28)
        #self.button_insert.move(int(self.second_frame.width() / 2) - int(self.button_insert.width() / 2), 0)

        """  
            CONSTANTS
        """
        
        self.label_const = QLabel("Constants SIR", self.second_frame)
        self.label_const.setObjectName("init_values_label")
        self.label_const.setStyleSheet(init_values_panel)
        self.label_const.move(65+c1, 70-65)
        
        # B - Tasa contagios
        self.label_tasa = QLabel("B (Tasa Contagios)", self.second_frame)
        self.label_tasa.setObjectName("tasa_contagios_label")
        self.label_tasa.setStyleSheet(qlabel_css_twoframe)
        self.label_tasa.move(32-20, 35+c-20)
        
        self.entry_tasa = QLineEdit(self.second_frame, text="3.61e-5")
        self.entry_tasa.setFixedWidth(100)
        self.entry_tasa.setPlaceholderText("Tasa Contagios")
        self.entry_tasa.setClearButtonEnabled(True)
        self.entry_tasa.move(32+118,  70-20)
        
        
        # Y - Coef. Retiro Natural
        self.label_coef_retnatural = QLabel("Y (Coef. Retiro Natural)", self.second_frame)
        self.label_coef_retnatural.setObjectName("coef_retiro_natural")
        self.label_coef_retnatural.setStyleSheet(qlabel_css_twoframe)
        self.label_coef_retnatural.move(32-20,  35+c+20+10-20)
        
        self.entry_ret_natu = QLineEdit(self.second_frame)
        self.entry_ret_natu.setFixedWidth(100)
        self.entry_ret_natu.setPlaceholderText("Coef. Retiro Natural")
        self.entry_ret_natu.setClearButtonEnabled(True)
        self.entry_ret_natu.move(32+118,  90+10-20)
        
        # V - Indice Covertura Vacuna
        self.label_indice_cob_vacun = QLabel("v (Ind. Cobertura Vacuna)", self.second_frame)
        self.label_indice_cob_vacun.setObjectName("indice_cob_vacun")
        self.label_indice_cob_vacun.setStyleSheet(qlabel_css_twoframe)
        self.label_indice_cob_vacun.move(32-20,  35+c+40+20-20)
        
        self.entry_cob_vacu = QLineEdit(self.second_frame)
        self.entry_cob_vacu.setFixedWidth(100)
        self.entry_cob_vacu.setPlaceholderText("Ind. Cobertura Vacuna")
        self.entry_cob_vacu.setClearButtonEnabled(True)
        self.entry_cob_vacu.move(32+118,  110+20-20)      
        
        # e -  Indice Eficacia Vacuna
        self.label_indice_ef_vacuna = QLabel("e (Ind. Eficacia Vacuna)", self.second_frame)
        self.label_indice_ef_vacuna.setObjectName("indice_ef_vacuna")
        self.label_indice_ef_vacuna.setStyleSheet(qlabel_css_twoframe)
        self.label_indice_ef_vacuna.move(32-20,  35+c+60+30-20)
        
        self.entry_efi_vacu = QLineEdit(self.second_frame)
        self.entry_efi_vacu.setFixedWidth(100)
        self.entry_efi_vacu.setPlaceholderText("Ind. Eficacia Vacuna")
        self.entry_efi_vacu.setClearButtonEnabled(True)
        self.entry_efi_vacu.move(32+118,  130+30-20)
        
        self.layout_tools.addWidget(self.first_frame)
        self.layout_tools.addWidget(self.second_frame)
        self.first.tab1.setLayout(self.layout_tools)
        
        """ 
            <SecondTabWidget> 
            Data Base View - Objet 
        """
        
        self.model_sir = Article(S0 = 99986, I0 = 14, R0 = 0)
        
        self.sol1, self.sol2, self.time = self.model_sir.updateSolution(52)
        self.canvas = MplCanvas(sol1=self.sol1, sol2=self.sol2, time=self.model_sir.simulation_time)
        self.canvas.setFixedWidth(900)
        
        self.canvas_layout = QVBoxLayout()
        self.canvas_layout.addWidget(self.canvas)
        self.second.tab1.setLayout(self.canvas_layout)
        
        """ Add widgets in main window """
        self.mainbox.addWidget(self.first)      # add first widget in mainbox layout.
        self.mainbox.addWidget(self.second)     # add second widget in mainbox layout.
        self.setCentralWidget(self.frame)       # set central widget.
    
    def update_canvas(self):
        
        self.model_sir.updateValues(int(self.entry_s0.text()), 
                                    int(self.entry_i0.text()), 
                                    int(self.entry_r0.text()), 
                                    float(self.entry_tasa.text()),
                                    float(self.entry_ret_natu.text()),
                                    float(self.entry_cob_vacu.text()),
                                    float(self.entry_efi_vacu.text()),
                                    int(self.entry_x0.text()),
                                    int(self.entry_xf.text()),
                                    int(self.entry_n.text()))
        
        self.sol1, self.sol2, self.time = self.model_sir.updateSolution(int(self.entry_n.text()))
        
        self.canvas.ax1.cla()
        self.canvas.ax1.plot(self.time, self.sol1[0][:,0], lw = 1.5, color = 'green')
        self.canvas.ax1.plot(self.time, self.sol2[0][:,0], lw = 1.5, color = 'blue')
        self.canvas.ax1.set_title('$Suceptibles$ $S_{(t)}$')
        self.canvas.ax1.set_xlabel('$t_{(weeks)}$')
        self.canvas.ax1.set_ylabel('$S_{(t)}$')
        self.canvas.ax1.legend(labels=["$not$ $vaccine$", "$vaccine$"])
        self.canvas.ax1.grid(True)
        
        self.canvas.ax2.cla()
        self.canvas.ax2.plot(self.time, self.sol1[0][:,1], lw = 1.5, color = 'red')
        self.canvas.ax2.plot(self.time, self.sol2[0][:,1], lw = 1.5, color = 'orange')
        self.canvas.ax2.set_xlabel('$t_{(weeks)}$')
        self.canvas.ax2.set_ylabel('$I_{(t)}$')
        self.canvas.ax2.set_title('$Infectados$ $I_{(t)}$')
        self.canvas.ax2.legend(labels=["$not$ $vaccine$", "$vaccine$"])
        self.canvas.ax2.grid(True)

        self.canvas.ax3.cla()
        self.canvas.ax3.plot(self.time, self.sol1[0][:,2], lw = 1.5, color = 'purple')
        self.canvas.ax3.plot(self.time, self.sol2[0][:,2], lw = 1.5, color = 'brown')
        self.canvas.ax3.set_title('$Resistentes$ $R_{(t)}$')
        self.canvas.ax3.set_xlabel('$t_{(weeks)}$')
        self.canvas.ax3.set_ylabel('$R_{(t)}$')
        self.canvas.ax3.legend(labels=["$not$ $vaccine$", "$vaccine$"])
        self.canvas.ax3.grid(True)

        self.canvas.draw()

        
        
