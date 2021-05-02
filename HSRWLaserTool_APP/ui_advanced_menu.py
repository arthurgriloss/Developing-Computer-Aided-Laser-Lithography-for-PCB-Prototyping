from main import*

class UiAdvancedMenu(MainWindow):

    def toogle_menu(self, max_height, enable):
        if enable:
            height = self.ui.advMenu.height()
            max_extend = max_height
            standard = 5

            if height == 5:
                height_extended = max_extend
                self.ui.advanced_button.setText("Return")
                style = """background-color: rgb(0, 240, 112);
                border-radius: 20px;
                color: rgb(255, 255, 255);"""
            else:
                height_extended = standard
                self.ui.advanced_button.setText("Advanced")
                style = """background-color: rgb(0, 0, 0);
                border-radius: 20px;
                color: rgb(255, 255, 255);"""

            self.ui.adv_label.setStyleSheet(style)
            self.animation = QPropertyAnimation(self.ui.advMenu, b"geometry")
            self.animation.setDuration(400)
            self.animation.setStartValue(QRect(0, 0, 800, height))
            self.animation.setEndValue(QRect(0, 0, 800, height_extended))
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            