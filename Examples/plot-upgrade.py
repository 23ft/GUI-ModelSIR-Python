import sys
import random
import matplotlib
#matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        #fig = Figure(figsize=(width, height), dpi=dpi)
        
        fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(1, 3, figsize=(10,5), constrained_layout=True)
        
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        
        self.canvas.ax1.cla()  # Clear the canvas.
        self.canvas.ax1.plot(self.xdata, self.ydata, 'r')
        self.canvas.ax1.set_title('$Suceptibles$ $S_{(t)}$')
        self.canvas.ax1.set_xlabel('$t_{(weeks)}$')
        self.canvas.ax1.set_ylabel('$S_{(t)}$')
        #selfcanvas.ax1.legend(labels=["$not$ $vaccine$", "$vaccine$"])
        self.canvas.ax1.grid(True)
        
        
        
        self.canvas.ax2.cla()  # Clear the canvas.
        self.canvas.ax2.plot(self.xdata, self.ydata, 'r')
        
        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QApplication(sys.argv)
w = MainWindow()
app.exec_()