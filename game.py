# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import LOGIC 
import time

#values          [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,  65,  66]      ]
Positions_Left = [95,  95,  95,  95,  95,  95,  95,  95, 175, 245, 315, 385, 455, 525, 595, 665, 735, 805, 895, 895, 895, 895, 895, 895, 895, 895, 805, 735, 665, 595, 525, 455, 385, 315, 230, 230, 230, 230, 230, 230, 230, 315, 385, 455, 525, 595, 665, 745, 750, 750, 750, 750, 670, 600, 530, 460, 390, 370, 370, 370, 460, 515, 575, 635, 670, 605, 530]
Positions_Up   =[725, 655, 585, 515, 445, 375, 305, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 220, 295, 365, 440, 510, 580, 650, 730, 730, 730, 730, 730, 730, 730, 730, 730, 730, 648, 586, 529, 472, 415, 353, 348, 348, 348, 348, 348, 348, 348, 410, 470, 530, 610, 635, 635, 635, 635, 635, 545, 455, 420, 440, 440, 440, 440, 510, 510, 510]

cadena_inicial = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" 

cadena_final = "</span></p></body></html>"





class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 1200)
        font = QtGui.QFont()
        font.setBold(True)
        Dialog.setFont(font)
        self.Board = QtWidgets.QWidget(Dialog)
        self.Board.setGeometry(QtCore.QRect(70, 10, 961, 781))
        self.Board.setObjectName("Board")
        self.Board.setStyleSheet("")
        
        self.textEdit_Titulo = QtWidgets.QTextEdit(self.Board)
        self.textEdit_Titulo.setGeometry(QtCore.QRect(0, 0, 611, 51))
        self.textEdit_Titulo.setObjectName("textEdit")
        
        self.textEdit_Turno = QtWidgets.QTextEdit(self.Board)
        self.textEdit_Turno.setGeometry(QtCore.QRect(20, 70, 280, 41))
        self.textEdit_Turno.setObjectName("textEdit_2")
        self.textEdit_Turno.setVisible(False)

        self.textEdit_NumPart = QtWidgets.QTextEdit(self.Board)
        self.textEdit_NumPart.setGeometry(QtCore.QRect(350, 70, 200, 90))
        self.textEdit_NumPart.setObjectName("textEdit_4")
        self.textEdit_NumPart.setVisible(False)

        self.textEdit_getNumPart = QtWidgets.QTextEdit(self.Board)
        self.textEdit_getNumPart.setGeometry(QtCore.QRect(570, 90, 50, 40))
        self.textEdit_getNumPart.setObjectName("textEdit_5")
        self.textEdit_getNumPart.setVisible(False)

        self.textEdit_Part = QtWidgets.QTextEdit(self.Board)
        self.textEdit_Part.setGeometry(QtCore.QRect(390, 80, 190, 50))
        self.textEdit_Part.setObjectName("textEdit_6")
        self.textEdit_Part.setVisible(False)

        self.textEdit_getPart = QtWidgets.QTextEdit(self.Board)
        self.textEdit_getPart.setGeometry(QtCore.QRect(585, 90, 90, 40))
        self.textEdit_getPart.setObjectName("textEdit_7")
        self.textEdit_getPart.setVisible(False)

        self.pushButton = QtWidgets.QPushButton(self.Board)
        self.pushButton.setGeometry(QtCore.QRect(670, 0, 120, 60))
        self.pushButton.setStyleSheet("background-color: rgb(0, 220, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Click)

        self.pushButton2 = QtWidgets.QPushButton(self.Board)
        self.pushButton2.setGeometry(QtCore.QRect(650, 90, 91, 41))
        self.pushButton2.setStyleSheet("background-color: rgb(0, 220, 0);")
        self.pushButton2.setObjectName("ingresar")
        self.pushButton2.setVisible(False)
        self.pushButton2.clicked.connect(self.Ingresar)

        self.pushButton3 = QtWidgets.QPushButton(self.Board)
        self.pushButton3.setGeometry(QtCore.QRect(690, 90, 91, 41))
        self.pushButton3.setStyleSheet("background-color: rgb(0, 220, 0);")
        self.pushButton3.setObjectName("ingresar")
        self.pushButton3.setVisible(False)
        self.pushButton3.clicked.connect(self.Agregar)

        self.pushButton4 = QtWidgets.QPushButton(self.Board)
        self.pushButton4.setGeometry(QtCore.QRect(650, 0, 200, 60))
        self.pushButton4.setStyleSheet("background-color: rgb(0, 220, 0);")
        self.pushButton4.setObjectName("IniciarGame")
        self.pushButton4.setVisible(False)
        self.pushButton4.clicked.connect(self.iniciarGame)



        self.frame = QtWidgets.QFrame(self.Board)
        self.frame.setGeometry(QtCore.QRect(30, 150, 1600, 1000))
        self.frame.setStyleSheet("background-image: url(Images/Tablero.JPG) no-repeat")
        self.frame.setObjectName("frame")
    

        self.frame_Star = QtWidgets.QFrame(self.Board)
        self.frame_Star.setGeometry(QtCore.QRect(15, 725, 40, 40))
        self.frame_Star.setStyleSheet("background-image: url(Images/star.png) no-repeat")
        self.frame_Star.setObjectName("frame_star")
        self.frame_Star.setVisible(False)

        self.frame_Cora = QtWidgets.QFrame(self.Board)
        self.frame_Cora.setGeometry(QtCore.QRect(60, 725, 40, 40))
        self.frame_Cora.setStyleSheet("background-image: url(Images/Cora.png) no-repeat")
        self.frame_Cora.setObjectName("frame_Cora")
        self.frame_Cora.setVisible(False)

        self.frame_ray = QtWidgets.QFrame(self.Board)
        self.frame_ray.setGeometry(QtCore.QRect(105, 725, 40, 40))
        self.frame_ray.setStyleSheet("background-image: url(Images/Rayo.png) no-repeat")
        self.frame_ray.setObjectName("frame_ray")
        self.frame_ray.setVisible(False)

        self.frame_tree = QtWidgets.QFrame(self.Board)
        self.frame_tree.setGeometry(QtCore.QRect(150, 725, 40, 40))
        self.frame_tree.setStyleSheet("background-image: url(Images/Tree.png) no-repeat")
        self.frame_tree.setObjectName("frame_tree")
        self.frame_tree.setVisible(False)

        self.alert = QtWidgets.QMessageBox(self.Board)
        self.alert.setGeometry(QtCore.QRect(700, 300, 100, 100))
        self.alert.setWindowTitle("Alert")
        self.alert.setText("Numero de participantes deben ser 2, 3 o 4")
        self.alert.setIcon(QtWidgets.QMessageBox.Warning)  # You can also use other icons like Information, Critical, or Question
        self.alert.setStandardButtons(QtWidgets.QMessageBox.Ok)  # Adding OK and Cancel buttons
        self.alert.setVisible(False)

        self.TURNO = QtWidgets.QMessageBox(self.Board)
        self.TURNO.setGeometry(QtCore.QRect(700, 300, 100, 100))
        self.TURNO.setWindowTitle("Turno")
        self.TURNO.setText("Numero de participantes deben ser 2, 3 o 4")
        self.TURNO.setIcon(QtWidgets.QMessageBox.Information)  # You can also use other icons like Information, Critical, or Question
        self.TURNO.setStandardButtons(QtWidgets.QMessageBox.Yes)  # Adding OK and Cancel buttons
        self.TURNO.setVisible(False)

        self.Cuadro = QtWidgets.QInputDialog(self.Board)
        self.Cuadro.setWindowTitle("Ejercicio")
        self.Cuadro.setLabelText("Número de repeticiones:")

        self.Cuadro.resize(600, 400)  # Width and height

    # Customize the font
        self.font = QtGui.QFont()
        self.font.setPointSize(14)  # Set font size
        self.Cuadro.setFont(self.font)

        self.pushButton.setFont(self.font)
        self.pushButton2.setFont(self.font)
        self.pushButton3.setFont(self.font)
        self.pushButton4.setFont(self.font)
        self.alert.setFont(self.font)
        self.TURNO.setFont(self.font)


        self.Participantes = []
        self.N_participantes = 0

        self.text(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def Click(self):
        self.pushButton.setVisible(False)
        self.pushButton2.setVisible(True)
        self.textEdit_NumPart.setVisible(True)
        self.textEdit_getNumPart.setVisible(True)


    def Ingresar(self):
        self.N_participantes = int(self.textEdit_getNumPart.toPlainText())
        if(self.N_participantes<2 or self.N_participantes>4):
            self.alert.setVisible(True)
            response = self.alert.exec_()
            if response == QtWidgets.QMessageBox.Ok:
                print("OK clicked!")
                self.alert.setVisible(False)
                self.textEdit_getNumPart.setHtml("")
        else:
            self.pushButton2.setVisible(False)
            self.textEdit_NumPart.setVisible(False)
            self.textEdit_getNumPart.setVisible(False)
            self.textEdit_Part.setVisible(True)
            self.textEdit_getPart.setVisible(True)
            self.pushButton3.setVisible(True)
            self.frame_Star.setVisible(True)
            self.frame_Cora.setVisible(True)
            if self.N_participantes > 2:
                self.frame_ray.setVisible(True)
                if self.N_participantes == 4:
                    self.frame_tree.setVisible(True)


    def Agregar(self):
        self.Participantes.append(self.textEdit_getPart.toPlainText())
        self.textEdit_getPart.setHtml("")
        self.textEdit_Titulo.setHtml(cadena_inicial+"<span style=\" font-size:24pt;\">Bienvenido--- "+self.Participantes[-1]+ cadena_final)
        if len(self.Participantes)==self.N_participantes:
            self.textEdit_Part.setVisible(False)
            self.textEdit_getPart.setVisible(False)
            self.pushButton3.setVisible(False)
            self.pushButton4.setVisible(True)
            
        else:
            self.textEdit_Part.setText(cadena_inicial+"<span style=\" font-size:14pt;\">Participante "+ str(len(self.Participantes)+1) +cadena_final)
    

    def text(self, Dialog):
        Dialog.setWindowTitle("Dialog")
        #Dialog.setWindowBackground()
        self.textEdit_Titulo.setHtml(cadena_inicial+"<span style=\" font-size:24pt;\">Bienvenidos al LARATRON"+cadena_final)
        self.textEdit_Turno.setHtml(cadena_inicial+"<span style=\" font-size:14pt;\">Turno de:---"+cadena_final)
        self.textEdit_NumPart.setHtml(cadena_inicial+"<span style=\" font-size:14pt;\">Numero de participantes: "+cadena_final)
        self.textEdit_Part.setHtml(cadena_inicial+"<span style=\" font-size:14pt;\">Participante 1: "+cadena_final)
        
        self.pushButton.setText("Iniciar")
        self.pushButton2.setText("Ingresar")
        self.pushButton3.setText("Agregar")
        self.pushButton4.setText("Comenzar batalla")
       



    def iniciarGame(self):
        self.textEdit_Titulo.setHtml(cadena_inicial+"<span style=\" font-size:24pt;\">----¡COMENZAMOS!----   "+cadena_final)
        self.textEdit_Turno.setVisible(True)  
        self.pushButton4.setVisible(False)
        names_P = self.Participantes
        FamilyGame = LOGIC.BOARD(self.N_participantes, names_P)
        
        while(FamilyGame.statusGame == FamilyGame.noExisteGanador):
            for Part in FamilyGame.Participants:
                self.textEdit_Turno.setHtml(cadena_inicial+"<span style=\" font-size:18pt;\">Turno de:"+ Part.name + cadena_final)
                Move = Part.play()
                self.TURNO.setText(f'{Part.name}: Por favor presiona el botón para lanzar dados')
                self.TURNO.setVisible(True)
                response = self.TURNO.exec_()
                if response == QtWidgets.QMessageBox.Yes:
                    self.printBoard(FamilyGame.Participants)

                    if Part.status == True:
                        self.alert.setText(f'tenemos ganador: felicidades {Part.name}')
                        self.alert.setVisible(True)
                        FamilyGame.statusGame = FamilyGame.existeGanador
                        response = self.alert.exec_()
                        if response == QtWidgets.QMessageBox.Ok:
                            break
                    FamilyGame.checkIfPositionIsTaken(Part)    # Regresar una posicion a quien lo estaba ocupando
                    self.printBoard(FamilyGame.Participants)
                    accion, leyend, level = FamilyGame.Action(Part.Position)
                    self.alert.setText(f'\t {Move} \t \n\n Llegas a pos: {Part.Position} \n\n {leyend}')
                    self.alert.setVisible(True)
                    response = self.alert.exec_()
                    if response == QtWidgets.QMessageBox.Ok:
                        if accion == "Nothing" or accion == "Water":
                            self.textEdit_Titulo.setHtml(cadena_inicial+"<span style=\" font-size:18pt;\">Aburrido" + cadena_final)
                            time.sleep(1)
                        else:
                            self.textEdit_Titulo.setHtml(cadena_inicial+"<span style=\" font-size:18pt;\">--¡Vamos!---¡Con todo!" + cadena_final)
                            self.generateAction(Part,  accion, level)
                            if Part.status == True:
                                self.alert.setText(f'tenemos ganador: felicidades {Part.name}')
                                self.alert.setVisible(True)
                                FamilyGame.statusGame = FamilyGame.existeGanador
                                if response == QtWidgets.QMessageBox.Ok:
                                    break
                            FamilyGame.checkIfPositionIsTaken(Part)    # Regresar una posicion a quien lo estaba ocupando
                            self.printBoard(FamilyGame.Participants)
                            time.sleep(1)

    
    

    def generateAction(self, Part,  accion, level):
       
        ok = self.Cuadro.exec_()
        if ok:
            text = self.Cuadro.textValue()
            Rep = int(text)
            if accion=="Reto":
                Part.calculateAvance(level, Rep)
            else:
                Part.calculateRetroceso(level, Rep)

    
    def printBoard(self, Participants):
            self.putOnBoard_Star(Participants[0].Position)
            self.putOnBoard_Cora(Participants[1].Position)
            if self.N_participantes > 2:
                self.putOnBoard_ray(Participants[2].Position)
                if self.N_participantes == 4:
                    self.putOnBoard_tree(Participants[3].Position)

    def putOnBoard_Star(self, Pos):
        self.frame_Star.setGeometry(QtCore.QRect(Positions_Left[Pos], Positions_Up[Pos], 40, 40))


    def putOnBoard_Cora(self, Pos):
        self.frame_Cora.setGeometry(QtCore.QRect(Positions_Left[Pos], Positions_Up[Pos], 40, 40))

    def putOnBoard_ray(self, Pos):
        self.frame_ray.setGeometry(QtCore.QRect(Positions_Left[Pos], Positions_Up[Pos], 40, 40))

    def putOnBoard_tree(self, Pos):
        self.frame_tree.setGeometry(QtCore.QRect(Positions_Left[Pos], Positions_Up[Pos], 40, 40))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
