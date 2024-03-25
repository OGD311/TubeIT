# Form implementation generated from reading ui file 'MenuV1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QGraphicsPixmapItem, QLabel
from PyQt6.QtCore import QPropertyAnimation, QPoint, Qt

import random
import json
import AudioIn as AI

class Ui_TubeIt(object):
    
    def __init__(self) -> None:
        self.startedMic = False
        self.PNGView = None
        self.curAudioLevel = 0
        self.refreshRate = 20
        self.image1 = None
        self.image2 = None
        self.updateVals(first=True)


    def setupUi(self, TubeIt):
        TubeIt.setObjectName("TubeIt")
        TubeIt.setFixedSize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(TubeIt)
        self.centralwidget.setObjectName("centralwidget")

        self.MainLabel = QLabel(parent=self.centralwidget)
        self.MainLabel.setGeometry(635, 70, 200, 50)
        self.MainLabel.setObjectName("MainLabel")
        font = self.MainLabel.font()
        font.setPointSize(20)
        self.MainLabel.setFont(font)

        self.PNGView = QtWidgets.QGraphicsView(self.centralwidget)
        self.PNGView.setGeometry(QtCore.QRect(10, 20, 551, 511))
        self.PNGView.setObjectName("PNGView")
        self.scene = QtWidgets.QGraphicsScene()
        self.PNGView.setScene(self.scene)
        self.PNGView.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(self.backgroundColor)))

        self.Shake = QtWidgets.QCheckBox(self.centralwidget)
        self.Shake.setGeometry(QtCore.QRect(650, 370, 101, 31))
        self.Shake.setObjectName("Shake")

        self.Start = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.Start.setGeometry(QtCore.QRect(600, 420, 151, 31))
        self.Start.setMouseTracking(False)
        start_button = self.Start.addButton("Start", QtWidgets.QDialogButtonBox.ButtonRole.ActionRole)
        start_button.clicked.connect(self.start_microphone)
        stop_button = self.Start.addButton("Stop", QtWidgets.QDialogButtonBox.ButtonRole.ActionRole)
        stop_button.clicked.connect(self.stop_microphone)
        self.Start.setCenterButtons(True)
        self.Start.setObjectName("Start")

        self.Image1 = QtWidgets.QToolButton(self.centralwidget)
        self.Image1.setGeometry(QtCore.QRect(610, 180, 131, 22))
        self.Image1.setObjectName("Image1")
        self.Image1.clicked.connect(lambda: self.load_image1(new=True))

        self.Image2 = QtWidgets.QToolButton(self.centralwidget)
        self.Image2.setGeometry(QtCore.QRect(610, 270, 131, 22))
        self.Image2.setObjectName("Image2")
        self.Image2.clicked.connect(lambda: self.load_image2(new=True))

        self.File1 = QtWidgets.QLabel(self.centralwidget)
        self.File1.setGeometry(QtCore.QRect(580, 210, 200, 16))
        self.File1.setObjectName("File1")
        self.File1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.File2 = QtWidgets.QLabel(self.centralwidget)
        self.File2.setGeometry(QtCore.QRect(580, 300, 200, 16))
        self.File2.setObjectName("File2")
        self.File2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.inputLevelLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLevelLabel.setGeometry(QtCore.QRect(580, 450, 200, 16))
        self.inputLevelLabel.setObjectName("inputLevelLabel")
        self.inputLevelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.Copyright = QtWidgets.QLabel(self.centralwidget)
        self.Copyright.setGeometry(QtCore.QRect(140, 540, 300, 16))
        self.Copyright.setObjectName("Copyright")
        self.Copyright.setAlignment(Qt.AlignmentFlag.AlignCenter)

        TubeIt.setCentralWidget(self.centralwidget)

        # Menu
        self.menubar = QtWidgets.QMenuBar(TubeIt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menubar.setParent(TubeIt)

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        TubeIt.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(TubeIt)
        self.statusbar.setObjectName("statusbar")
        TubeIt.setStatusBar(self.statusbar)

        # self.actionImport = QtGui.QAction(TubeIt)
        # self.actionImport.setObjectName("actionImport")
        # self.actionImport.setShortcutVisibleInContextMenu(False)
        # self.menuOptions.addAction(self.actionImport)

        # self.actionExport = QtGui.QAction(TubeIt)
        # self.actionExport.setObjectName("actionExport")
        # self.actionExport.setShortcutVisibleInContextMenu(False)
        # self.menuOptions.addAction(self.actionExport)

        self.actionSettings = QtGui.QAction(TubeIt)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.setShortcutVisibleInContextMenu(True)
        self.menuOptions.addAction(self.actionSettings)

        # Create toggleable action for Fullscreen
        self.actionFullscreen = QtGui.QAction(TubeIt)
        self.actionFullscreen.setCheckable(True)
        self.actionFullscreen.setObjectName("actionFullscreen")
        self.actionFullscreen.triggered.connect(self.toggle_fullscreen)
        self.menuOptions.addAction(self.actionFullscreen)

        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(TubeIt)
        QtCore.QMetaObject.connectSlotsByName(TubeIt)

        self.updateVals()


    def retranslateUi(self, TubeIt):
        _translate = QtCore.QCoreApplication.translate
        TubeIt.setWindowTitle(_translate("TubeIt", "TubeIt"))
        self.MainLabel.setText(_translate("MainWindow", "TubeIt"))
        self.Shake.setText(_translate("TubeIt", "Shake?"))
        self.Image1.setText(_translate("TubeIt", "Select Still Image"))
        self.Image2.setText(_translate("TubeIt", "Select Talking Image"))
        self.File1.setText(_translate("TubeIt", "None"))
        self.File2.setText(_translate("TubeIt", "None"))
        self.inputLevelLabel.setText(_translate("TubeIt", "Input Level: "))
        self.Copyright.setText(_translate("TubeIt", "Copyright (c) 2024 ogd311. All rights reserved."))
        self.menuOptions.setTitle(_translate("TubeIt", "Options"))
        # self.actionImport.setText(_translate("TubeIt", "Import"))
        # self.actionExport.setText(_translate("TubeIt", "Export"))
        self.actionSettings.setText(_translate("TubeIt", "Settings"))
        self.actionFullscreen.setText(_translate("TubeIt", "Fullscreen"))



    ## Message code
    def raiseWarning(self, message):
        warning_msg = QMessageBox()
        warning_msg.setIcon(QMessageBox.Icon.Warning)
        warning_msg.setText(message)
        warning_msg.setWindowTitle("Warning")
        warning_msg.exec()

    def raiseMessage(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Message")
        msg.exec()

    ## Microphone

    def start_microphone(self):
        if not self.startedMic:
            self.updateVals()
            self.microphone = AI.MicrophoneInput()
            self.microphone.open_stream()  # Call open_stream before starting
            self.microphone.start()  # Start the thread
            self.startedMic = True
            self.update_Audio_Level()
            self.switch_images()

    def stop_microphone(self):
        if self.startedMic:
            self.microphone.stop()
            self.startedMic = False
            self.curAudioLevel = 0

    def update_Audio_Level(self):
        self.curAudioLevel = self.microphone.curVal()
        self.inputLevelLabel.setText(f"Input Level: {self.curAudioLevel}")
        QtCore.QTimer.singleShot(self.refreshRate, self.update_Audio_Level)


    ## Images
        
    def switch_images(self):
        if self.curAudioLevel >= self.micLevel:
            self.viewImage(self.image2, shake=self.Shake.isChecked())
        else:
            self.viewImage(self.image1)

        QtCore.QTimer.singleShot(self.refreshRate, self.switch_images)


    def load_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        file_dialog.setViewMode(QFileDialog.ViewMode.List)
        file_dialog.setDirectory("C:/")  # Set default directory if needed
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            if file_names:
                image_path = file_names[0]
                return image_path

    def getName(self, filepath):
        split = filepath.split('/')
        return split[-1]
    

    def shake_image(self, image):
        dx = random.randint(int(-5*self.shakeMultiplyer), int(5*self.shakeMultiplyer))  # Random horizontal movement
        dy = random.randint(int(-5*self.shakeMultiplyer), int(5*self.shakeMultiplyer))  # Random vertical movement
        image.moveBy(dx, dy)

    def viewImage(self, filename, shake=False):
        self.scene.clear()
        image = QtGui.QImage(filename)
        if image.isNull():
            self.raiseWarning("Error: Unable to load image")
            return None

        pixmap = QtGui.QPixmap.fromImage(image)
        pixmap = pixmap.scaled(self.PNGView.viewport().size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        pixmapItem = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.scene.addItem(pixmapItem)

        if shake:
            try:
                self.shake_image(pixmapItem)
            except Exception as e:
                print(e)

        self.scene.setSceneRect(QtCore.QRectF(pixmapItem.boundingRect()))


    def load_image1(self, new=False):
        if not self.image1 or new == True:
            self.image1 = self.load_image()

        if self.image1:
            self.File1.setText(self.getName(self.image1))
            self.updateView()
            self.saveStill()

    def load_image2(self, new=False):
        if not self.image2 or new==True:
            self.image2 = self.load_image()

        if self.image2:
            self.File2.setText(self.getName(self.image2))
            self.updateView()
            self.saveTalking()

    def updateView(self):
        if self.image2:
            self.viewImage(self.image2)
        if self.image1:
            self.viewImage(self.image1)

        
        

    ## Fullscreen for
    def toggle_fullscreen(self):
        if self.actionFullscreen.isChecked():
            print("Fullscreen activated")
            # Hide all UI elements
            self.MainLabel.hide()
            self.Shake.hide()
            self.Start.hide()
            self.Image1.hide()
            self.Image2.hide()
            self.File1.hide()
            self.File2.hide()
            self.inputLevelLabel.hide()
            self.Copyright.hide()
            self.menuOptions.hide()
            self.statusbar.hide()
            # Resize PNGView to fill the entire central widget
            self.PNGView.setGeometry(self.centralwidget.geometry())  
            self.PNGView.move(0,0)

        else:
            print("Fullscreen deactivated")
            # Show all UI elements
            self.MainLabel.show()
            self.Shake.show()
            self.Start.show()
            self.Image1.show()
            self.Image2.show()
            self.File1.show()
            self.File2.show()
            self.inputLevelLabel.show()
            self.Copyright.show()
            self.menuOptions.show()
            self.statusbar.show()
            # Restore original size and position of PNGView
            self.PNGView.setGeometry(QtCore.QRect(10, 20, 551, 511))  
            

    def getSettings(self):
        with open('settings.json', 'r') as settings:
            data = json.load(settings)
            print(data)
            array_data = [value for key, value in data.items()]
            print(array_data)

            return array_data
    
    def updateVals(self, first=False):
        micLevel, shakeMultiplyer, backgroundColor, audioDevice, image1, image2 = self.getSettings()
        AI.setAudioDevice(audioDevice)
        
        if self.startedMic:  # Stop existing microphone instance if running
            self.stop_microphone()

        self.micLevel = micLevel
        self.shakeMultiplyer = shakeMultiplyer
        self.backgroundColor = backgroundColor
        self.image1, self.image2 = image1, image2
        
        if self.PNGView:
            self.PNGView.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(self.backgroundColor)))

        if image1 and not first:
            self.load_image1()
        
        if image2 and not first:
            self.load_image2()



    def saveStill(self):
        with open('settings.json', 'r') as settings:
            data = json.load(settings)

        values = {
            "micLevel": data["micLevel"],
            "shakeMultiplyer": data["shakeMultiplyer"],
            "backgroundColor": data["backgroundColor"],
            "audioDevice" : data["audioDevice"],
            "stillImage" : self.image1,
            "talkingImage" : data["talkingImage"],
        }

        with open('settings.json', 'w') as settings:
            json.dump(values, settings)

    def saveTalking(self):
        with open('settings.json', 'r') as settings:
            data = json.load(settings)

        values = {
            "micLevel": data["micLevel"],
            "shakeMultiplyer": data["shakeMultiplyer"],
            "backgroundColor": data["backgroundColor"],
            "audioDevice" : data["audioDevice"],
            "stillImage" : data["stillImage"],
            "talkingImage" : self.image2
        }

        with open('settings.json', 'w') as settings:
            json.dump(values, settings)