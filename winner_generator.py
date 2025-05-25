from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
#подключение библиотек
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('определить победителя')
button = QPushButton ('Сгенерировать')
text = QLabel('Нажми что бы узнать победителя')
winner = QLabel('?')
#создание элементов интерфейса
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignHCenter)
line.addWidget(winner, alignment=Qt.AlignHCenter)
line.addWidget(button, alignment=Qt.AlignHCenter)
main_win.setLayout(line)
#обработка событий


def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')
button.clicked.connect(show_winner)
#запуск приложения
main_win.show()
app.exec_()






