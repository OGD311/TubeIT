import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from MainMenu import Ui_TubeIt  # Import the class representing your main UI
from SettingsMenu import Ui_Settings  # Import the class representing the settings Settings UI

import json

class SettingsSettings(QDialog, Ui_Settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon.ico"))



class MyTubeIt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TubeIt()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("icon.ico"))

        
        # Connect the menu action to the method
        self.ui.actionSettings.triggered.connect(self.open_settings)
    
    ## Keybinds
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F:
            print('Toggle')
            self.ui.actionFullscreen.setChecked(not self.ui.actionFullscreen.isChecked())
            self.ui.toggle_fullscreen()

        if event.key() == Qt.Key.Key_S:
            print('Shake')
            self.ui.Shake.setChecked(not self.ui.Shake.isChecked())


    def open_settings(self):
        # Create an instance of the settings Settings and display it
        settings_Settings = SettingsSettings()
        settings_Settings.exec()
        self.ui.updateVals()
        if self.ui.startedMic == True:
            self.ui.start_microphone()

def main():
    app = QApplication(sys.argv)
    main_window = MyTubeIt()
    main_window.show()
    sys.exit(app.exec())

try:
    values = {
        "micLevel": 500,
        "shakeMultiplyer": 1.0,
        "backgroundColor": '#04F404',
        "audioDevice" : 0,
        "stillImage" : "",
        "talkingImage" : ""
    }

    with open('settings.json', 'x') as settings:
        json.dump(values, settings)
    settings.close()
except:
    pass

if __name__ == "__main__":
    main()
