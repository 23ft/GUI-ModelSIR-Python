from base import QApplication, AppMain, sys


if __name__ == '__main__':
    Appx = QApplication(sys.argv)

    mainWindow = AppMain()
    mainWindow.show()

    sys.exit(Appx.exec())