################################################################################

## LASER TOOL APPLICATION
## V: 1.0.0
## BACHELOR THESIS B.SC MECHANICAL ENG. AT HOCHSCHULE RHEIN-WAAL
## DEVELOPING COMPUTER-AIDED LASER LITHOGRAPHY FOR PCB PROTOTYPING
## BY: ARTHUR GRILO DA SILVA SANTOS

################################################################################

import serial
from time import sleep
import sys
import os
from subprocess import Popen, PIPE
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.uic import loadUi

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

## ==> ADVANCED MENU
from ui_advanced_menu import *

## ==> GCODE LOADER WINDOW
from ui_gcode_loader import Ui_GcodeLoader

## ==> GRBL STREAMER WINDOW
from ui_grbl_stream import Ui_GrblStream


#########################################################################################################################
# SPLASH SCREEN
#########################################################################################################################
class SplashScreen(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## FRAMELESS WINDOW
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.counter = 0    # Loader Counter

        ## ==> SERIAL ##
        config = open("config.txt")
        lines = config.readlines()
        self.serialcom = serial.Serial(
            lines[2].strip(),
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)   # Open grbl serial port 
        self.serialcom.write(str.encode('\r\n\r\n')) # Hit enter a few times to wake the Printrbot # Start grbl
        sleep(2)
        self.serialcom.flushInput()  # Flush startup text in serial input
        config.close()

        ## QTIMER ==> CONNECTING TO THE SERIAL
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(30) 

        QtCore.QTimer.singleShot(500, lambda: self.ui.label_loading.setText("CONNECTING TO THE SERIAL..."))
        QtCore.QTimer.singleShot(2000, lambda: self.ui.label_loading.setText("STARTING..."))

        ## ==> READ DEFAULT VALUES ##
        default_variables = open("default_variables.txt")
        line = default_variables.readlines()

        self.root_direct = line[0].strip()
        self.tool_diam = float(line[1].strip())
        self.n_passes_iso = int(line[2].strip())
        self.pcb_height = int(line[3].strip())
        self.overlap = int(line[4].strip())
        self.feed_rate = int(line[5].strip())
        self.spindle_speed = int(line[6].strip())
        self.pin_gap = int(line[7].strip())
        self.pcb_width = int(line[8].strip())

        default_variables.close()

        self.show()
        ## ==> END ##

    
    # PROGRESS EFFECT AND DELAY TO START PORT SERIAL COMMUNICATION
    def progress(self):

            self.ui.progressBar.setValue(self.counter)  # Set value to progress bar

            # CLOSE SPLASH SCREE AND OPEN APP
            if self.counter > 100:
                self.timer.stop()

                # SHOW MAIN WINDOW
                self.close()    # Close splash screen
                self.main = MainWindow()
                self.main.show()
              

            self.counter += 1   # Increase counter


#########################################################################################################################
# MAIN/ADVANCED MENU SCREEN
#########################################################################################################################
class MainWindow(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## FRAMELESS WINDOW
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MODE BUTTONS
        self.ui.isolate_button.clicked.connect(self.status)
        self.ui.remove_button.clicked.connect(self.status)
        self.ui.soldermask_button.clicked.connect(self.status)
        self.ui.gcode_button.clicked.connect(self.status)

        self.ui.next_button.clicked.connect(self.start) # Start button
        self.ui.shutdown_button.clicked.connect(self.shutdown) # Shutdown button
        self.ui.browse_button.clicked.connect(self.browsefiles) # Main browse button
        
        self.ui.advanced_button.clicked.connect(lambda: UiAdvancedMenu.toogle_menu(self, 480, True))    # Advanced menu button

        ## ==> ADVANCED MENU ##
        self.ui.root_button.clicked.connect(self.browse_root)   # root browse button

        # DISPLAY DEFAULT VALUES ADVANCED MENU
        self.root_direct = window.root_direct
        self.ui.tool_diameter.setValue(window.tool_diam)
        self.ui.passes_iso.setValue(window.n_passes_iso)
        self.ui.pcb_height.setValue(window.pcb_height)
        self.ui.overlap.setValue(window.overlap)
        self.ui.feed_rate.setValue(window.feed_rate)
        self.ui.spin_speed.setValue(window.spindle_speed)
        self.ui.pin_gap.setValue(window.pin_gap)
        self.ui.pcb_width.setValue(window.pcb_width)

        # MATRIX CONTAINING ALL CHECKBOX (MACHINE POINT OF VIEW):
        self.checkbox_matrix = [[self.ui.k0, self.ui.k1, self.ui.k2, self.ui.k3, self.ui.k4, self.ui.k5, self.ui.k6, self.ui.k7, self.ui.k8],
                [self.ui.j0, self.ui.j1, self.ui.j2, self.ui.j3, self.ui.j4, self.ui.j5, self.ui.j6, self.ui.j7, self.ui.j8],
                [self.ui.i0, self.ui.i1, self.ui.i2, self.ui.i3, self.ui.i4, self.ui.i5, self.ui.i6, self.ui.i7, self.ui.i8],
                [self.ui.h0, self.ui.h1, self.ui.h2, self.ui.h3, self.ui.h4, self.ui.h5, self.ui.h6, self.ui.h7, self.ui.h8],
                [self.ui.g0, self.ui.g1, self.ui.g2, self.ui.g3, self.ui.g4, self.ui.g5, self.ui.g6, self.ui.g7, self.ui.g8],
                [self.ui.f0, self.ui.f1, self.ui.f2, self.ui.f3, self.ui.f4, self.ui.f5, self.ui.f6, self.ui.f7, self.ui.f8],
                [self.ui.e0, self.ui.e1, self.ui.e2, self.ui.e3, self.ui.e4, self.ui.e5, self.ui.e6, self.ui.e7, self.ui.e8],
                [self.ui.d0, self.ui.d1, self.ui.d2, self.ui.d3, self.ui.d4, self.ui.d5, self.ui.d6, self.ui.d7, self.ui.d8],
                [self.ui.c0, self.ui.c1, self.ui.c2, self.ui.c3, self.ui.c4, self.ui.c5, self.ui.c6, self.ui.c7, self.ui.c8],
                [self.ui.b0, self.ui.b1, self.ui.b2, self.ui.b3, self.ui.b4, self.ui.b5, self.ui.b6, self.ui.b7, self.ui.b8],
                [self.ui.a0, self.ui.a1, self.ui.a2, self.ui.a3, self.ui.a4, self.ui.a5, self.ui.a6, self.ui.a7, self.ui.a8]] 
        ## ==> END ##

        
    # BROWSE BUTTON FUNCTION
    def browsefiles(self):

        file_directory = QFileDialog.getOpenFileName(self, "Open File", self.root_direct)
        self.ui.directory_edit.setText(file_directory[0]) 
        self.file_directory = file_directory[0]


    # ROOT BROWSE BUTTON FUNCTION
    def browse_root(self):

        root_directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ui.root_browse.setText(root_directory)
        self.root_direct = root_directory


    # TOOGLE EFFECT METHOD BUTTON SELECTION
    def status(self):

        toggled = u"""QPushButton{\n
	background-color:rgb(0, 143, 66);\n
	border-style: outset;\n
	border-width: 2px;\n
	border-color: white;\n
	color:rgb(255, 255, 255);\n
	border-radius: 10px;\n
}"""
        not_toggled = u"""QPushButton{\n
	background-color:rgb(0, 240, 112);\n
	border-style: outset;\n
	border-width: 2px;\n
	border-color: white;\n
	color:rgb(255, 255, 255);\n
	border-radius: 10px;\n
}"""
        if self.ui.isolate_button.isChecked():
            self.ui.isolate_button.setStyleSheet(toggled)
            self.ui.remove_button.setStyleSheet(not_toggled)
            self.ui.soldermask_button.setStyleSheet(not_toggled)
            self.ui.gcode_button.setStyleSheet(not_toggled)
        elif self.ui.remove_button.isChecked():
            self.ui.isolate_button.setStyleSheet(not_toggled)
            self.ui.remove_button.setStyleSheet(toggled)
            self.ui.soldermask_button.setStyleSheet(not_toggled)
            self.ui.gcode_button.setStyleSheet(not_toggled)
        elif self.ui.soldermask_button.isChecked():
            self.ui.isolate_button.setStyleSheet(not_toggled)
            self.ui.remove_button.setStyleSheet(not_toggled)
            self.ui.soldermask_button.setStyleSheet(toggled)
            self.ui.gcode_button.setStyleSheet(not_toggled)
        elif self.ui.gcode_button.isChecked():
            self.ui.isolate_button.setStyleSheet(not_toggled)
            self.ui.remove_button.setStyleSheet(not_toggled)
            self.ui.soldermask_button.setStyleSheet(not_toggled)
            self.ui.gcode_button.setStyleSheet(toggled)

    # START BUTTON PROCESSES
    def start(self):

        # READ ADVANCED VALUES        
        self.tool_diam = self.ui.tool_diameter.value()
        self.n_passes_iso = int(self.ui.passes_iso.value())
        self.pcb_height = int(self.ui.pcb_height.value())
        self.overlap = int(self.ui.overlap.value())
        self.feed_rate = int(self.ui.feed_rate.value())
        self.spindle_speed = int(self.ui.spin_speed.value())
        self.pin_gap = int(self.ui.pin_gap.value())
        self.pcb_width = int (self.ui.pcb_width.value())

        # SAVE NEW DEFAULT
        if self.ui.default_check.isChecked():
            default_variables = open("default_variables.txt", "w+")
            default_variables.write(f"""{self.root_direct}\n{self.tool_diam}\n{self.n_passes_iso}\n{self.pcb_height}\n{self.overlap}\n{self.feed_rate}\n{self.spindle_speed}\n{self.pin_gap}\n{self.pcb_width}

            #############
            1. standard directory
            2. tool diameter [mm]
            3. number of passes (iso) [unit]
            4. number of passes (rem) [unit]
            5. overlap [%]
            6. feed rate [mm/min]
            7. spindlespeed [rpm]
            8. pin gap [mm]
            9. side size [mm]
            ###########
            """)
            default_variables.close()

        # KEEP PARAMETERS FOR FURTHER OPERATIONS
        if self.ui.keep_check.isChecked():
            window.root_direct = self.root_direct
            window.tool_diam = self.ui.tool_diameter.value()
            window.n_passes_iso = int(self.ui.passes_iso.value())
            window.pcb_height = int(self.ui.pcb_height.value())
            window.overlap = int(self.ui.overlap.value())
            window.feed_rate = int(self.ui.feed_rate.value())
            window.spindle_speed = int(self.ui.spin_speed.value())
            window.pin_gap = int(self.ui.pin_gap.value())
            window.pcb_width = int(self.ui.pcb_width.value())

        # CHECK ACTIVE PINS
        self.xy_pos = []    # Initiate variable
        for i in range(9):
            same_row = 0
            for j in range(11):
                if self.checkbox_matrix[j][i].isChecked():
                    same_row += 1
                    if same_row > 1:
                        # Pins with horizontal arrangement
                        self.x_offset = int(self.xy_pos[0][0] * self.pin_gap)
                        self.y_offset = int(self.xy_pos[0][1] * self.pin_gap - self.pcb_height/2)
                    else:
                        self.xy_pos.append([j, i])
        
        if len(self.xy_pos) == 2:
            if self.xy_pos[0][0] == self.xy_pos[1][0]:
                # Pins with vertical arrangement
                self.x_offset = int(min(self.xy_pos[0][0], self.xy_pos[1][0]) * self.pin_gap - self.pcb_width/2)
                self.y_offset = int(min(self.xy_pos[0][1], self.xy_pos[1][1]) * self.pin_gap)
            else:
                # Pins with rectangular arrangement
                self.x_offset = int(min(self.xy_pos[0][0], self.xy_pos[1][0]) * self.pin_gap)
                self.y_offset = int(min(self.xy_pos[0][1], self.xy_pos[1][1]) * self.pin_gap)
        
        self.mirror()   # Ask the user if he wants to mirror the image

        ## SELECT MODE
        if self.ui.gcode_button.isChecked():
            self.file = self.file_directory

            # SHOW STREAM WINDOW
            self.loader = GrblStream()
            self.loader.show()

            # CLOSE LOADER SCREEN
            self.close()
        else:
            # SCRIPT FILE PROCESSING
            self.scripiting()

            # SHOW LOADER WINDOW
            self.loader = GcodeLoader()
            self.loader.show()

            # CLOSE MAIN SCREEN
            self.close()
    

    # MIRROR ENTITY
    def mirror(self):
        if self.ui.gcode_button.isChecked():
            pass
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Mirror entity")
            msg.setText("Do you want to mirror the entity?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            msg.setDefaultButton(QMessageBox.No)
            msg.buttonClicked.connect(self.mirror_action)

            show = msg.exec_()

    
    # CONTINUATION OF MIRROR FUNCTION
    def mirror_action(self, button):
        if button.text() == "&Yes":
            self.mirror = True
        else:
            self.mirror = False
    

    # SHUTDOWN MACHINE
    def shutdown(self):
        msg = QMessageBox()
        msg.setWindowTitle("Shutdown")
        msg.setText("Do you really want to shutdown the machine?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.shutdown_action)

        show = msg.exec_()


    # CONTINUATION OF SHUTDOWN FUNCTION
    def shutdown_action(self, button):
        if button.text() == "&Yes":
            os.system('sudo shutdown now')

    
    # GENERATE SCRIPT FILE
    def scripiting(self):

        file_name_pos = self.file_directory.rfind("/")
        file_name = self.file_directory[file_name_pos+1:]   # Only file name without directory
        
        # SELECT METHOD
        if self.ui.isolate_button.isChecked():
            method = "isolate FILE_NAME -dia DIAM -passes N_PASSES -overlap OVERL -combine 1 -outname isolatio_route".replace(
            "FILE_NAME", f"{file_name}").replace("DIAM", f"{self.tool_diam}"
            ).replace("N_PASSES", f"{self.n_passes_iso}").replace("OVERL", f"{self.overlap}")
        else:
            method = "ncc FILE_NAME -tooldia DIAM -overlap 10 -margin 1 -method combine -all -outname isolatio_route".replace(
            "FILE_NAME", f"{file_name}").replace("DIAM", f"{self.tool_diam}")

        # CHECK IF MIRROR OR NOT    
        if self.mirror:
            axis = "X"
        else:
            axis = "N"

        # OPEN SCRIPT FILE CONTENT
        standard_script = open("standard_script.txt")
        modified_script = open("script.txt", "w+")
        config = open("config.txt")
        line = config.readlines()
        directory = line[1].strip().replace("\\", "/")

        for line in standard_script:
            if line.strip() == "METHOD":
                modified_script.write(method + "\n")
            else:
                modified_script.write(line.replace("FILE_DIRECTORY", self.file_directory).replace("WIDTH", f"{self.pcb_width}").replace(
                "HEIGHT", f"{self.pcb_height}").replace("FILE_NAME", f"{file_name}").replace("X_CONTOUR", f"{self.x_offset}").replace(
                "Y_CONTOUR", f"{self.y_offset}").replace("X_OFSET", f"{self.x_offset}").replace("Y_OFSET", f"{self.y_offset}").replace(
                "AXISNAME", axis).replace("FEEDR", f"{self.feed_rate}").replace("SS", f"{self.spindle_speed}").replace("DIRECTORY", f"{directory}/gcode.txt"))

    
        config.close()
        standard_script.close()
        modified_script.close()


#########################################################################################################################        
# GCODE GENERATION SCREEN
#########################################################################################################################
class GcodeLoader(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_GcodeLoader()
        self.ui.setupUi(self)

        # DELETE EXISTING GCODE IF IT EXIST
        if os.path.isfile("gcode.txt"):
            os.remove("gcode.txt")
        
        self.angle = 90 # Starting angle loading circle
        self.countdown = 0

        ## FREMELESS WINDOW
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.flatcam()  # Open FlatCAM
        
        ## QTIMER ==> SENDING NEW G-CODE COMMAND LINE
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.load_loop)
        self.timer.start(30)
    ## ==> END ##


    # INITIATE FLATCAM SHELL AND SCRIPT
    def flatcam(self):
        
        config = open("config.txt")
        line = config.readlines()
        flatcam_directory = line[0].strip()    # Select the directory with the file FlatCAM.py
        cmd = ["python3", f"{flatcam_directory}/FlatCAM.py", f"--shellfile={line[1].strip()}/script.txt"]

        self.process = Popen(cmd, stdout=PIPE)  # Initiate cmd
        config.close()


    # LOADING EFFECT
    def load_loop(self):

        # CHECK FOR TIMEOUT DUE TO WRONF FILE FORMAT OR SCRIPT ISSUE
        if self.countdown >= 10000: # 5 min
            # CLOSE FLATCAM
            self.process.terminate()

            # POP UP ERROR MSG
            self.count_down_timeout()

            # RETURN TO THE MAIN WINDOW
            self.directory = window.main.file_directory
            self.timer.stop()
            window.main = MainWindow()
            window.main.ui.directory_edit.setText(self.directory)   # Display last file at file selection 
            window.main.file_directory = self.directory # Set last selected as defaut option
            window.main.show()
            self.close()

        self.angle -= 1
        if self.angle < 0:
            self.angle = 360

        styleSheet = """QFrame{
                            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:ANG, stop:0 rgba(0, 85, 127, 255), stop:1 rgba(255, 255, 255, 0));
                            border-radius: 220px;
                        }"""
        newStyleSheet = styleSheet.replace("ANG", str(self.angle))

        self.ui.circularProgress.setStyleSheet(newStyleSheet)

        # CLOSE FLATCAM AFTER GCODE FILE GENERATION
        if os.path.isfile("gcode.txt") == True:
            sleep(1)    # Delay to avoid corrupted files
            self.process.terminate()

            # STOP TIMER
            self.timer.stop()

            # SHOW STREAM WINDOW
            window.main.file = "gcode.txt"
            self.stream = GrblStream()
            self.stream.show()
            self.close()

        self.countdown += 1

    def count_down_timeout(self):
        msg = QMessageBox()
        msg.setWindowTitle("Timeout")
        msg.setText("The software was not able to create a G-code. Probably because it was not a Gerber file")
        msg.setIcon(QMessageBox.Critical)

        show = msg.exec_()


#########################################################################################################################
# GRBL STREAM SCREEN
#########################################################################################################################
class GrblStream(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_GrblStream()
        self.ui.setupUi(self)

        ## FREMELESS WINDOW
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## ==> HOMING FUNCTION
        # window.serialcom.write(str.encode("G28"))
        # grbl_out = window.serialcom.readline() # Wait for grbl response with carriage return

        self.progressBarValue(0, 100)   # Start bar at 0%
        self.start_status = False   # Check if running or not

        # OPEN GENERATED G-CODE
        self.directory = window.main.file_directory
        self.file = open(window.main.file)
        self.lines = self.file.readlines()
        self.n_lines = len(self.lines)  # File lenght
        self.actual_line = 0    # Line trackers
        self.file.close()

        # PLAY/PAUSE/STOP FUNCTION CALL
        self.ui.play_pause_button.clicked.connect(self.play_pause)
        self.ui.stop_button.clicked.connect(self.main_window)
    ## ==> END ##


    # PLAY PAUSE LINE STREAMING
    def play_pause(self):

        if self.start_status == False:
            ## QTIMER ==> CALL THE FUNCTION
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.grbl_stream)
            self.ui.engrave_label.setText("Engraving...")
            self.timer.start(1)

            window.serialcom.write(str.encode("~")) # Start Cycle
            self.start_status =  True
        else:
            window.serialcom.write(str.encode("!"))  # Hold feed

            ## QTIMER ==> CONNECTING TO THE SERIAL
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.main_window)
            self.timer.start(300000) # Five min time to start again otherwise it comes back to the main menu

            self.ui.send_label.setText("PROGRAM PAUSED...")
            self.ui.gcode_label.setText("Press Play to continue")

            self.start_status = False


    # STREAM LINE TO GRBL
    def grbl_stream(self):
        

        if self.actual_line == self.n_lines:

            ## QTIMER ==> DELAY TO READ MSG
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.return_main)
            self.timer.start(3000)

            QtCore.QTimer.singleShot(1, lambda: self.ui.send_label.setText("PROCESS CONCLUDED!"))
            QtCore.QTimer.singleShot(1, lambda: self.ui.gcode_label.setText("Returning to the main window!"))
        else:
            line = self.format_line(self.lines[self.actual_line])
            if line != "":
                self.ui.send_label.setText("SENDING: ")
                self.ui.gcode_label.setText(line)
                window.serialcom.write(str.encode(line + '\n')) # Send g-code block to grbl
                grbl_out = window.serialcom.readline() # Wait for grbl response with carriage return
        self.progressBarValue(self.actual_line, self.n_lines)
        self.actual_line += 1


    # LOADING EFFECT
    def progressBarValue(self, value, max_value):

        progress = (max_value - value) / max_value
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        styleSheet = """QFrame{\n
                    border-radius: 220px;\n
                    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop: STOP_1 rgba(0, 170, 0, 0), stop: STOP_2 rgba(0, 85, 127, 255));\n
                    }"""
        newStyleSheet = styleSheet.replace("STOP_1", stop_1).replace("STOP_2", stop_2)
        self.ui.circularProgress.setStyleSheet(newStyleSheet)

        # PERCENTAGE DISPLAY
        html = """<html><head/><body><p align="center">VALUE<span style=" font-size:72pt; vertical-align:super;">%</span></p></body></html>"""
        newHtml = html.replace("VALUE", str(int((1 - progress) * 100)))
        self.ui.progress_label.setText(newHtml)

    
    # RESTART LINE STREAMING
    def restart(self):

        self.timer.stop()
        self.start_status = False


    # STOP PROCESS AND CALL RETURN
    def main_window(self):
        
        window.serialcom.close()
        window.serialcom.open()
        window.serialcom.write(str.encode("M5"))    # turn laser off
        window.serialcom.write(str.encode("G28"))   # homing command or function

        ## QTIMER ==> DELAY TO READ MSG
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.return_main)
        self.timer.start(3000)
        
        self.ui.engrave_label.setText("STOPPED")
        QtCore.QTimer.singleShot(1, lambda: self.ui.send_label.setText("PROCESS INTERRUPTED!"))
        QtCore.QTimer.singleShot(1, lambda: self.ui.gcode_label.setText("Returning to the main window!"))

    
    # RETURN TO THE MAIN WINDOW
    def return_main(self):
        self.timer.stop()
        window.main = MainWindow()
        window.main.ui.directory_edit.setText(self.directory)   # Display last file at file selection 
        window.main.file_directory = self.directory # Set last selected as defaut option
        window.main.show()
        self.close()

    
    # FORMAT G-CODE LINES TO STREAM FORMAT
    def format_line(self, line):

        formated_line = ""  # Initiate variable
        line = line.strip()

        # IGNORE COMMENTARY LINES
        if "(" in line:
            line = ""

        # SUBSTITUE Z MOVEMENTS FOR LASER ON AND OFF
        if ("Z" in line):
                if float(line[5:]) > 0:
                    line = "M5"
                else:
                    line = f"M3 S{window.main.spindle_speed}"

        # SEPARATE CONCATENATED WORDS
        if line != "":
            order = []
            for pos, char in enumerate(line):
                if char.isalpha():
                    order.append(pos)
            splitted_line = []
            splitted_line.append(line[order[-1]:].strip())
            for i in range(1, len(order)):
                splitted_line.append(line[order[-i-1]:order[-i]].strip())
            splitted_line.reverse()
            formated_line = " ".join(splitted_line)
        return formated_line


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
## ==> END ##
