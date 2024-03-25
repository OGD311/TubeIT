import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from MainMenu import Ui_PNGTuber  # Import the class representing your main UI
from SettingsMenu import Ui_Settings  # Import the class representing the settings Settings UI

class SettingsSettings(QDialog, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MyPNGTuber(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PNGTuber()
        self.ui.setupUi(self)

        # Connect the menu action to the method
        self.ui.actionSettings.triggered.connect(self.open_settings)

    def open_settings(self):
        # Create an instance of the settings Settings and display it
        settings_Settings = SettingsSettings()
        settings_Settings.exec()

def main():
    app = QApplication(sys.argv)
    main_window = MyPNGTuber()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
