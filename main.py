import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from MainMenu import Ui_PNGTuber  # Import the class representing your main UI
from SettingsMenu import Ui_Settings  # Import the class representing the settings Settings UI

import json

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
        self.ui.updateVals()

def main():
    app = QApplication(sys.argv)
    main_window = MyPNGTuber()
    main_window.show()
    sys.exit(app.exec())

try:
    values = {
        "micLevel": 500,
        "shakeMultiplyer": 1.0,
        "backgroundColor": '#04F404',
        "audioDevice" : 0
    }

    with open('settings.json', 'x') as settings:
        json.dump(values, settings)
    settings.close()
except:
    pass

if __name__ == "__main__":
    main()
