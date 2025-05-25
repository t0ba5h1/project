from PyQt5.QtWidgets import *
import os
from PIL import ImageFilter, Image, ImageOps
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

workdir = ''


class ImageProcessor():
    def __init__(self): 
        self.image = None
        self.dir = None
        self.filename = None
        self.savedir = "Modified/"

    def LoadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir,filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width, label_height = image_label.width(), image_label.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.KeepAspectRatio)
        image_label.setPixmap(scaled_pixmap)
        image_label.setVisible(True)

    def saveImage(self):
        path = os.path.join(workdir, self.savedir)
        if not(os.path.exists(path)
                or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bnw(self):
        self.image = ImageOps.grayscale(self.image)
        self.saveImage()
        image_path = os.path.join(self.dir,
                                  self.savedir,
                                  self.filename)
        self.showImage(image_path)

    def do_blured(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir,
                                  self.savedir,
                                  self.filename)
        self.showImage(image_path)

    def do_mirrored(self):
        self.image = ImageOps.mirror(self.image)
        self.saveImage()
        image_path = os.path.join(self.dir,
                                  self.savedir,
                                  self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.rotate(90)
        self.saveImage()
        image_path = os.path.join(self.dir,
                                  self.savedir,
                                  self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.rotate(270)
        self.saveImage()
        image_path = os.path.join(self.dir,
                                  self.savedir,
                                  self.filename)
        self.showImage(image_path)

def showChosenImage():
    if image_list.currentRow() >= 0:
        filename = image_list.currentItem().text()
        workimage.LoadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)


workimage = ImageProcessor()

def chooseworkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extension):
    result = []
    for file in files:
        if file.endswith(extension):
            result.append(file)
    return result

def ShowfileNameslist():
    chooseworkdir()
    files = filter(os.listdir(workdir), 'png')
    image_list.clear()
    for file in files:
        image_list.addItem(file)

app = QApplication([])
main_win = QWidget()

folder_button = QPushButton('Папка')
left_button = QPushButton('Лево')
right_button = QPushButton('Право')
mirror_button = QPushButton('Зеркало')
sharpness_button = QPushButton('Резкость')
BnW_button = QPushButton('Ч/Б')
image_label = QLabel('Картинка')
image_list = QListWidget()


main_layout = QHBoxLayout()
left_layout = QVBoxLayout() 
right_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()

buttons_layout.addWidget(left_button)
buttons_layout.addWidget(right_button)
buttons_layout.addWidget(mirror_button)
buttons_layout.addWidget(sharpness_button)
buttons_layout.addWidget(BnW_button)

left_layout.addWidget(image_label)
left_layout.addLayout(buttons_layout)

right_layout.addWidget(folder_button)
right_layout.addWidget(image_list)

main_layout.addLayout(right_layout)
main_layout.addLayout(left_layout)

folder_button.clicked.connect(ShowfileNameslist)
image_list.currentRowChanged.connect(showChosenImage)

BnW_button.clicked.connect(workimage.do_bnw)
sharpness_button.clicked.connect(workimage.do_blured)
mirror_button.clicked.connect(workimage.do_mirrored)
left_button.clicked.connect(workimage.do_left)
right_button.clicked.connect(workimage.do_right)

main_win.setLayout(main_layout)
main_win.setWindowTitle('Easy Editor')
main_win.show()
main_win.resize(700, 500)
app.exec_()