# Form implementation generated from reading ui file 'UI Files/SettingsMenu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QColorDialog
from PyQt6.QtCore import pyqtSignal, QObject

import pyaudio
import json
import AudioIn as AI

class Ui_Settings(object):

    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(400, 300)

        self.InputChoice = QtWidgets.QComboBox(parent=Settings)
        self.InputChoice.setGeometry(QtCore.QRect(90, 70, 201, 22))
        self.InputChoice.setObjectName("InputChoice")

        self.InputLabel = QtWidgets.QLabel(parent=Settings)
        self.InputLabel.setGeometry(QtCore.QRect(90, 50, 111, 16))
        self.InputLabel.setObjectName("InputLabel")

        self.MicLevelLabel = QtWidgets.QLabel(parent=Settings)
        self.MicLevelLabel.setGeometry(QtCore.QRect(90, 110, 111, 16))
        self.MicLevelLabel.setObjectName("MicLevelLabel")

        self.MicLevelSlider = QtWidgets.QSlider(parent=Settings)
        self.MicLevelSlider.setGeometry(QtCore.QRect(90, 130, 201, 18))
        self.MicLevelSlider.setMaximum(12000)
        self.MicLevelSlider.setProperty("value", 500)
        self.MicLevelSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.MicLevelSlider.setObjectName("MicLevelSlider")

        self.MicLevelSpin = QtWidgets.QSpinBox(parent=Settings)
        self.MicLevelSpin.setGeometry(QtCore.QRect(300, 130, 61, 21))
        self.MicLevelSpin.setMaximum(12000)
        self.MicLevelSpin.setProperty("value", 500)
        self.MicLevelSpin.setObjectName("MicLevelSpin")

        self.MicLevelSlider.valueChanged.connect(self.MicLevelSpin.setValue)
        self.MicLevelSpin.valueChanged.connect(self.MicLevelSlider.setValue)

        self.ShakeLabel = QtWidgets.QLabel(parent=Settings)
        self.ShakeLabel.setGeometry(QtCore.QRect(100, 180, 71, 16))
        self.ShakeLabel.setObjectName("ShakeLabel")

        self.ShakeMultiplyer = QtWidgets.QDoubleSpinBox(parent=Settings)
        self.ShakeMultiplyer.setGeometry(QtCore.QRect(100, 200, 62, 22))
        self.ShakeMultiplyer.setMaximum(20.0)
        self.ShakeMultiplyer.setSingleStep(0.1)
        self.ShakeMultiplyer.setProperty("value", 1.0)
        self.ShakeMultiplyer.setObjectName("ShakeMultiplyer")

        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Settings)
        self.buttonBox.setGeometry(QtCore.QRect(90, 250, 211, 31))
        self.resetButton = self.buttonBox.addButton(QtWidgets.QDialogButtonBox.StandardButton.Reset)
        self.resetButton.clicked.connect(self.resetSettings)

        self.applyButton = self.buttonBox.addButton(QtWidgets.QDialogButtonBox.StandardButton.Apply)
        self.applyButton.clicked.connect(self.applySettings)

        self.cancelButton = self.buttonBox.addButton(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        self.cancelButton.clicked.connect(self.closeSettings)

        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")


        self.colorLabel = QtWidgets.QLabel(parent=Settings)
        self.colorLabel.setGeometry(QtCore.QRect(230, 180, 111, 16))
        self.colorLabel.setObjectName("colorLabel")

        self.colorButton = QPushButton('Select Color', Settings)
        self.colorButton.setGeometry(QtCore.QRect(230, 200, 84, 22))
        self.colorButton.clicked.connect(self.openColorDialog)

        self.colorSquare = QtWidgets.QLabel(Settings)
        self.colorSquare.setGeometry(QtCore.QRect(320, 200, 20, 20))
        self.colorSquare.setAutoFillBackground(True)  # Ensure background color is applied
        self.colorSquare.setStyleSheet("background-color: #04F404")  # Default color

        self.populate_microphone_devices()
        self.loadSettings()
        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.InputLabel.setText(_translate("Settings", "Input Device"))
        self.MicLevelLabel.setText(_translate("Settings", "Input Trigger Level"))
        self.ShakeLabel.setText(_translate("Settings", "Shake Level"))
        self.colorLabel.setText(_translate("Settings", "Background Color"))


    def list_microphone_devices(self):
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        num_devices = info.get('deviceCount')
        devices = []
        for i in range(num_devices):
            device = p.get_device_info_by_host_api_device_index(0, i)
            if device.get('maxInputChannels') > 0:
                devices.append(device.get('name'))
        return devices

    def populate_microphone_devices(self):
        microphone_devices = self.list_microphone_devices()
        self.InputChoice.addItems(microphone_devices)

    def openColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            print('Selected color:', color.name())
            self.colorSquare.setStyleSheet(f"background-color: {color.name()}")
        else:
            print('Invalid color selected or dialog canceled')

    
    def loadSettings(self):
        with open('settings.json', 'r') as settings:
            data = json.load(settings)
            print(data)
            self.setMicLevel(data['micLevel'])
            self.ShakeMultiplyer.setValue(data['shakeMultiplyer'])
            self.colorSquare.setStyleSheet(f"background-color: {data['backgroundColor']}")
            AI.setAudioDevice(data['audioDevice'])
            self.InputChoice.setCurrentIndex(data['audioDevice'])


    def setMicLevel(self, value):
        self.MicLevelSlider.setValue(value)
        self.MicLevelSpin.setValue(value)

    def resetSettings(self):
        self.InputChoice.clear()
        self.populate_microphone_devices()
        self.ShakeMultiplyer.setValue(1.0)
        self.setMicLevel(500)
        self.colorSquare.setStyleSheet("background-color: #04F404")
        AI.setAudioDevice(0)

    def applySettings(self):
        color = self.colorSquare.palette().color(self.colorSquare.backgroundRole())
        hex_color = "#{:02x}{:02x}{:02x}".format(color.red(), color.green(), color.blue())

        values = {
            "micLevel": self.MicLevelSpin.value(),
            "shakeMultiplyer": self.ShakeMultiplyer.value(),
            "backgroundColor": hex_color,
            "audioDevice" : self.InputChoice.currentIndex()
        }

        with open('settings.json', 'w') as settings:
            json.dump(values, settings)

        self.closeSettings()

            

    def closeSettings(self):
        self.close()