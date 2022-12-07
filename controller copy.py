#pyuic5 -x view.ui -o view.py

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from view import *
import area 
import perimeter 

class ButtonError(Exception):
    #when user hits submit without selecting a radio button
    pass

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #set window icon and name
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

        #input boxes
        self.lineEdit_input_1.setVisible(False)
        self.lineEdit_input_2.setVisible(False)
        self.lineEdit_input_3.setVisible(False)
        self.radioButton_rectangle.clicked.connect(self.widgets)
        self.radioButton_triangle.clicked.connect(self.widgets)
        self.radioButton_circle.clicked.connect(self.widgets)
        self.radioButton_square.clicked.connect(self.widgets)
        self.comboBox.activated.connect(self.widgets) 

        self.pushButton_submit.clicked.connect(lambda: self.submit())

    #show widgets depending on radio button checked
    def widgets(self):
        #rectangle
        if self.radioButton_rectangle.isChecked():
            self.lineEdit_input_1.setVisible(True)
            self.lineEdit_input_2.setVisible(True)
            self.lineEdit_input_3.setVisible(False)
            self.label_enter_1.setText("Enter Base Length: ")
            self.label_enter_2.setText("Enter Height Length: ")
            self.label_enter_3.setText("")
            self.label_output_shape.setPixmap(QPixmap("images/rectangle.png"))
            self.label_output_text.setText("")
            self.label_output_shape_text_bottom.setText("")
            self.label_output_shape_text_middle.setText("")
            self.label_output_shape_text_right.setText("")
            self.label_output_shape_text_triangle_left.setText("")
            self.label_output_shape_text_triangle_right.setText("")

        #triangle area
        elif self.radioButton_triangle.isChecked() and self.comboBox.currentIndex() == 0:
            self.lineEdit_input_1.setVisible(True)
            self.lineEdit_input_2.setVisible(True)
            self.lineEdit_input_3.setVisible(False)
            self.label_enter_1.setText("Enter Base Length: ")
            self.label_enter_2.setText("Enter Height Length: ")
            self.label_enter_3.setText("")
            self.label_output_shape.setPixmap(QPixmap("images/triangle1.png"))
            self.label_output_text.setText("")
            self.label_output_shape_text_bottom.setText("")
            self.label_output_shape_text_middle.setText("")
            self.label_output_shape_text_right.setText("")
            self.label_output_shape_text_triangle_left.setText("")
            self.label_output_shape_text_triangle_right.setText("")

        #triangle perimeter
        elif self.radioButton_triangle.isChecked() and self.comboBox.currentIndex() == 1:
            self.lineEdit_input_1.setVisible(True)
            self.lineEdit_input_2.setVisible(True)
            self.lineEdit_input_3.setVisible(True)
            self.label_enter_1.setText("Enter Side 1: ")
            self.label_enter_2.setText("Enter Side 2: ")
            self.label_enter_3.setText("Enter Side 3: ")
            self.label_output_shape.setPixmap(QPixmap("images/triangle2.png"))
            self.label_output_text.setText("")
            self.label_output_shape_text_bottom.setText("")
            self.label_output_shape_text_middle.setText("")
            self.label_output_shape_text_right.setText("")
            self.label_output_shape_text_triangle_left.setText("")
            self.label_output_shape_text_triangle_right.setText("")

        #cricle
        elif self.radioButton_circle.isChecked():
            self.lineEdit_input_1.setVisible(True)
            self.lineEdit_input_2.setVisible(False)
            self.lineEdit_input_3.setVisible(False)
            self.label_enter_1.setText("Enter Radius: ")
            self.label_enter_2.setText("")
            self.label_enter_3.setText("")
            self.label_output_shape.setPixmap(QPixmap("images/circle.png"))
            self.label_output_text.setText("")
            self.label_output_shape_text_bottom.setText("")
            self.label_output_shape_text_middle.setText("")
            self.label_output_shape_text_right.setText("")
            self.label_output_shape_text_triangle_left.setText("")
            self.label_output_shape_text_triangle_right.setText("")

        #square
        elif self.radioButton_square.isChecked():
            self.lineEdit_input_1.setVisible(True)
            self.lineEdit_input_2.setVisible(False)
            self.lineEdit_input_3.setVisible(False)
            self.label_enter_1.setText("Enter Side Length: ")
            self.label_enter_2.setText("")
            self.label_enter_3.setText("")
            self.label_output_shape.setPixmap(QPixmap("images/square.png"))
            self.label_output_text.setText("")
            self.label_output_shape_text_bottom.setText("")
            self.label_output_shape_text_middle.setText("")
            self.label_output_shape_text_right.setText("")
            self.label_output_shape_text_triangle_left.setText("")
            self.label_output_shape_text_triangle_right.setText("")

    def submit(self):
        try: 
            shape = self.buttonGroup.checkedId()
            #tri -2, rect -3, square -4, circle -5
            
            equation = self.comboBox.currentIndex()
            #area 0, perimeter 1

            #rect
            if shape == -3:

                #area
                if equation == 0:
                    input_1 = float(self.lineEdit_input_1.text())
                    input_2 = float(self.lineEdit_input_2.text())

                    if input_1 <= 0 or input_2 <= 0:
                        raise ValueError

                    self.label_output_shape_text_bottom.setText(f"{input_1:.2f}")
                    self.label_output_shape_text_right.setText(f"{input_2:.2f}")
                    self.label_output_text.setText(f"Area: {area.rectangle(input_1, input_2):.2f}")

                #perimeter
                if equation == 1:
                    input_1 = float(self.lineEdit_input_1.text())
                    input_2 = float(self.lineEdit_input_2.text())

                    if input_1 <= 0 or input_2 <= 0:
                        raise ValueError

                    self.label_output_shape_text_bottom.setText(f"{input_1:.2f}")
                    self.label_output_shape_text_right.setText(f"{input_2:.2f}")
                    self.label_output_text.setText(f"Perimeter: {perimeter.rectangle(input_1, input_2):.2f}")

            #triangle
            if shape == -2:

                #area
                if equation == 0:
                    input_1 = float(self.lineEdit_input_1.text())
                    input_2 = float(self.lineEdit_input_2.text())

                    if input_1 <= 0 or input_2 <= 0:
                        raise ValueError

                    self.label_output_shape_text_bottom.setText(f"{input_1:.2f}")
                    self.label_output_shape_text_middle.setText(f"{input_2:.2f}")
                    self.label_output_text.setText(f"Area: {area.triangle(input_1, input_2):.2f}")

                #perimeter
                if equation == 1:
                    input_1 = float(self.lineEdit_input_1.text())
                    input_2 = float(self.lineEdit_input_2.text())
                    input_3 = float(self.lineEdit_input_3.text())

                    if input_1 <= 0 or input_2 <= 0 or input_3 <= 0:
                        raise ValueError

                    self.label_output_shape_text_bottom.setText(f"{input_1:.2f}")
                    self.label_output_shape_text_triangle_left.setText(f"{input_2:.2f}")
                    self.label_output_shape_text_triangle_right.setText(f"{input_3:.2f}")
                    self.label_output_text.setText(f"Perimeter: {perimeter.triangle(input_1, input_2, input_3):.2f}")

            #square
            if shape == -4:

                #area
                if equation == 0:
                    input_1 = float(self.lineEdit_input_1.text())

                    if input_1 <= 0:
                        raise ValueError

                    self.label_output_shape_text_bottom.setText(f"{input_1:.2f}")
                    self.label_output_text.setText(f"Area: {area.rectangle(input_1, input_1):.2f}")

                #perimeter
                if equation == 1:
                    input_1 = float(self.lineEdit_input_1.text())

                    if input_1 <= 0:
                        raise ValueError

                    self.label_output_shape_text_bottom.setText(f"{input_1:.2f}")
                    self.label_output_text.setText(f"Perimeter: {perimeter.rectangle(input_1, input_1):.2f}")

            #circle
            if shape == -5:

                #area
                if equation == 0:
                    input_1 = float(self.lineEdit_input_1.text())

                    if input_1 <= 0:
                        raise ValueError

                    self.label_output_shape_text_middle.setText(f"{input_1:.2f}")
                    self.label_output_text.setText(f"Area: {area.circle(input_1):.2f}")

                #perimeter
                if equation == 1:
                    input_1 = float(self.lineEdit_input_1.text())

                    if input_1 <= 0:
                        raise ValueError

                    self.label_output_shape_text_middle.setText(f"{input_1:.2f}")
                    self.label_output_text.setText(f"Perimeter: {perimeter.circle(input_1):.2f}")
        
            if shape == -1:
                raise ButtonError
    

            #clear inputs and unselect radio button
            self.lineEdit_input_1.setText("")
            self.lineEdit_input_2.setText("")
            self.lineEdit_input_3.setText("")
            self.radioButton_rectangle.setChecked(False)
            self.radioButton_triangle.setChecked(False)
            self.radioButton_circle.setChecked(False)
            self.radioButton_square.setChecked(False)

            

        except ValueError:
            self.label_output_text.setText("Please enter a positive number.")
            self.lineEdit_input_1.setText("")
            self.lineEdit_input_2.setText("")
            self.lineEdit_input_3.setText("")
            self.label_output_shape_text_bottom.setText("")
            self.label_output_shape_text_middle.setText("")
            self.label_output_shape_text_right.setText("")
            self.label_output_shape_text_triangle_left.setText("")
            self.label_output_shape_text_triangle_right.setText("")

        except ButtonError:
            self.label_output_text.setText("Please choose a shape.")
            self.label_output_shape.setPixmap(QPixmap("images/arrow.png"))
            
        except Exception as e:
            self.label_output_text.setText(f"{e}")


        