#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle

class Question:

    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.right_answer = right_answer
        self.question = question
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3

questions = [
    Question("сколько 2+2?", "4", "5", "квадратный корень из 89754", "хз"),
    Question("столица Уругвая?", "Монтевидео", "Буенос-Айрес", "Москва", "Нью Йорк"),
    Question("как зовут первого призедента США?", "Вашингтон", "Обэмэ", "Пушкин", "Майкл Джексон"),
    Question("какая самая густонаселённая страна мира?", "Монако", "Монголия", "Россия", "Нарния")
]
question_number = -1
app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)

question = QLabel(questions[question_number].question)
button_answer = QPushButton("Ответить")

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton(questions[question_number].right_answer)
rbtn_2 = QRadioButton(questions[question_number].wrong_1)
rbtn_3 = QRadioButton(questions[question_number].wrong_2)
rbtn_4 = QRadioButton(questions[question_number].wrong_3)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answers)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
layout_line3.addStretch(1)
layout_line3.addWidget(button_answer, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
AnsGroupBox.hide()

main_win.setLayout(layout_card)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def check_answer():
    if answers[0].isChecked():
        return True
    return False

def next_question():
    global question_number
    question_number = (question_number + 1) % len(answers)
    question.setText(questions[question_number].question)
    shuffle(answers)
    answers[0].setText(questions[question_number].right_answer)
    answers[1].setText(questions[question_number].wrong_1)
    answers[2].setText(questions[question_number].wrong_2)
    answers[3].setText(questions[question_number].wrong_3)


def  show_answer():
    if button_answer.text() == "Ответить":
        button_answer.setText("Следующий вопрос")
        RadioGroupBox.hide()
        AnsGroupBox.show()
        if check_answer():
            lb_Result.setText('Вы ответили правильно!')
        else:
            lb_Result.setText("Вы ответили неверно!")
        lb_Correct.setText(f"Правильный ответ: {answers[0].text()}")
    else:
        button_answer.setText("Ответить")
        RadioGroupBox.show()
        AnsGroupBox.hide()
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        next_question()

button_answer.clicked.connect(show_answer)
next_question()
main_win.show()
app.exec_()