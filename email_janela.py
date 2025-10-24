import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton,  QTableWidgetItem, QTableWidget, QCheckBox


class janela_email(QWidget):

    def __init__(self):
        super().__init__()


        # ------Criando a janela--------------------------
        self.setGeometry(500,50,500,800)
        self.setWindowTitle("LOGIN")
        self.setFixedSize(500,800)
        self.setWindowIcon(QIcon(".venv/icon2.png"))
        # ------------------------------------------------

        # -------Separação dos lados (Superior)-----------
        self.superior_label = QLabel()
        self.superior_label.setStyleSheet("QLabel{background-color:#FFFFFF}")
        # ajustar a altura da label
        self.superior_label.setFixedHeight(120)

        # ------------- Criando imagem-------------------
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/botao.png"))
        self.imagem_label.setFixedSize(100,50)
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setAlignment(Qt.AlignCenter)
        
        # ----------------------------------------------

        # -----------------Criando o titulo--------------
        self.titulo_label = QLabel("Welcome to email")
        self.titulo_label.setStyleSheet("QLabel{font-size:15pt; color:#000000; font-weight: normal;self}")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setContentsMargins(0,50,0,0)
        # -----------------------------------------------

        self.sub_titulo_label = QLabel("Please login to your account")
        self.sub_titulo_label.setStyleSheet("QLabel{font-size:11pt; color:#000000 text-align: center;}")
        self.sub_titulo_label.setAlignment(Qt.AlignCenter)
        self.sub_titulo_label.setContentsMargins(0,0,0,50)
        
        # --------------------------------------------------

        # -------------------------------------------------
        self.email_label = QLabel("Email Address")
        self.email_label.setStyleSheet("QLabel{font-size:10pt; color:#696969;}")
        self.email_label.setAlignment(Qt.AlignCenter)

        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet("QLineEdit{font-size: 15pt; border: 2px solid #020a70; border-radius: 10px;}")
        # --------------------------------------------------

        # --------------------------------------------------
        self.senha_label = QLabel("Password")
        self.senha_label.setStyleSheet("QLabel{font-size:10pt;color:#696969;}")
        self.senha_label.setAlignment(Qt.AlignCenter)

        self.senha_edit = QLineEdit()
        self.senha_edit.setStyleSheet("QLineEdit{font-size: 15pt; border: 2px solid #020a70; border-radius: 10px;}")
        # ----------------------------------------------------

        

        # ------------Criando separação horizontal------------
        self.horizontal_layout = QHBoxLayout()
        

        # ----------------Criando a checkbox------------------
        self.checkBox = QCheckBox("Remember me")
        self.checkBox.setStyleSheet("QLabel{font-size:15pt}")
        # Adicionando a checkbox ao layout horizontal
        self.horizontal_layout.addWidget(self.checkBox)
        # ---------------------------------------------------
        
        

        # -----------criando label horizontal----------------- 
        self.horizontal_label= QLabel()
        self.horizontal_label.setLayout(self.horizontal_layout)
        
        # -----------------------------------------------------

        # ------Criando a frase da parte horizontal----------
        self.esqueceu_senha_label= QLabel("Forgot your Password?")
        self.esqueceu_senha_label.setStyleSheet("QLabel{font-size: 10pt; color:#000080;}") 
        # -------------------adicionando----------------------
        self.horizontal_layout.addWidget(self.esqueceu_senha_label)
        # ----------------------------------------------------

       
        # ---Criando a frase que vai em baixo da figura------
        self.novo_user_label = QLabel("New User?Create on Account")
        self.novo_user_label.setText('<span style="color:#000000;font-size:10pt;">New user<span>"<a href="#" style ="color:#000080;text-decoration:underline; fonte-weight:bold;">Create an Account</a>')
        self.novo_user_label.setAlignment(Qt.AlignCenter)
        # ---------------------------------------------------

        # ----------------------or---------------------------
        self.or_label = QLabel("OR")
        self.or_label.setStyleSheet("QLabel{font-size: 10pt; color:#696969;}") 
        self.or_label.setAlignment(Qt.AlignCenter)
        # ----------------------------------------------------
        
        # -------Separação dos lados (inferior)-----------
        self.inferior_label = QLabel()    
        self.inferior_label.setStyleSheet("QLabel{background-color:#020a70}")
        # ajustar a altura da label
        self.superior_label.setFixedHeight(600)
        # -------------------------------------------------


        # Criando horizontal layout na parte inferior 
        self.h_inferior_layout = QHBoxLayout()
        # --------------------------------------------

        # ------criando a imagem na label inferior-----
        self.facebook_label = QLabel()
        self.facebook_label.setPixmap(QPixmap(".venv/facebook.png"))
        self.facebook_label.setScaledContents(True)
        self.facebook_label.setFixedSize(200,70)
        # ----------------------------------------------

        # adicionando a imagem facebook ao layout horizontal
        self.h_inferior_layout.addWidget(self.facebook_label)
        # ---------------------------------------------------


        # ------criando a imagem na label inferior-----
        self.google_label = QLabel()
        self.google_label.setPixmap(QPixmap(".venv/google.png"))
        self.google_label.setScaledContents(True)
        self.google_label.setFixedSize(200,70)
        # ----------------------------------------------


        # adicionando a imagem facebook ao layout horizontal
        self.h_inferior_layout.addWidget(self.google_label)
        

        # adicionando o h_inferior_layout ao inferior label
        self.inferior_label.setLayout(self.h_inferior_layout)
        # ------------------------------------------------
        

       
        # organizar esses controles em um layout em vertical
        self.v_controles = QVBoxLayout()

        self.v_titulos = QVBoxLayout()
        self.v_titulos.setSpacing(-5)
      
        self.v_controles.addLayout(self.v_titulos)
        self.v_titulos.addWidget(self.titulo_label)
        self.v_titulos.addWidget(self.sub_titulo_label)
        self.v_controles.addWidget(self.email_label)
        self.v_controles.addWidget(self.email_edit)
        self.v_controles.addWidget(self.senha_label)
        self.v_controles.addWidget(self.senha_edit)
        self.v_controles.addWidget(self.horizontal_label)
        self.v_controles.addWidget(self.imagem_label, alignment=Qt.AlignCenter)
        self.v_controles.addWidget(self.novo_user_label)
        self.v_controles.addWidget(self.or_label)
        
      
        
        

        
        # adicionar os controles na parte superior
        self.superior_label.setLayout(self.v_controles)
        # adicionar os controles na parte inferior
        self.inferior_label.setLayout(self.v_controles)


        
        # Vamos criar um controle de layout 
        # para dispor as label superior e inferior, uma a abaixo 
        # da outra respectivamente.
        self.v_layout = QVBoxLayout()
        # self.v_layout.setStretch(1)

        self.v_layout.addWidget(self.superior_label)
        self.v_layout.addWidget(self.inferior_label)
        # adicionar o layout organizado na janela
        self.setLayout(self.v_layout)
        

app = QApplication(sys.argv)
janela = janela_email()
janela.show()
app.exec_()