# encoding=utf-8
from trainer import Trainer
from IME_generated import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtCore import Qt
from os import path
from mysolver import MySolver


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None, solver=MySolver):
        super(MyMainWindow, self).__init__(parent)
        # loadUi('./IME.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.solver = solver()
        self.ui.InputBox.textChanged.connect(self.check_change)
        self.ui.InputBox.returnPressed.connect(self.mysetfocus)
        self.candidate = []
        self.candidate_page = 0
        self.candidate_per_page = 5
        self.ui.actiontrain.triggered.connect(self.train)
        self.ui.actionload.triggered.connect(self.load_model)

    def train(self):
        data_directory = QFileDialog.getExistingDirectory(self, "选择pinyin.txt,pinyin_train.txt所在的目录")
        print(data_directory)
        mabiao = path.join(data_directory, "pinyin.txt")
        yuliao = path.join(data_directory, "pinyin_train.txt")
        target_model = path.join(path.curdir, "HMM_IME.pkl")
        my_trainer = Trainer()
        my_trainer.train(mabiao, yuliao)
        my_trainer.save_model(target_model)

    def load_model(self):
        model_file = QFileDialog.getOpenFileName(self, "选择.pkl文件")[0]
        print(model_file)
        self.solver = MySolver(model_file)

    def mysetfocus(self):

        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Equal:
            if len(self.candidate) > (self.candidate_page + 1) * self.candidate_per_page:
                self.candidate_page += 1
                self.set_string()
                # print("+")
        if e.key() == Qt.Key_Minus:
            if self.candidate_page - 1 >= 0:
                self.candidate_page += -1
                self.set_string()
                # print("-")
        if Qt.Key_0 <= e.key() <= Qt.Key_9:
            x = e.key() - Qt.Key_0
            if x < self.candidate_per_page:
                if len(self.candidate) > self.candidate_page * self.candidate_per_page + x:
                    self.ui.Result.insertPlainText(
                        str(self.candidate[self.candidate_page * self.candidate_per_page + x][0]))
                    self.ui.InputBox.setText("")
            self.ui.InputBox.setFocusPolicy(Qt.StrongFocus)
            self.ui.InputBox.setFocus()
            # print(e.key())
        if e.key() == Qt.Key_Space:
            self.ui.InputBox.setFocusPolicy(Qt.StrongFocus)
            self.ui.InputBox.setFocus()
            # print(e.key())

    def check_change(self, mystr):
        self.candidate = self.solver.solve(mystr)
        self.candidate_page = 0
        self.set_string()
        print(self.candidate)

    def set_string(self):
        final_str = ""
        if len(self.candidate) < self.candidate_per_page * (1 + self.candidate_page):
            for i in range(len(self.candidate) - self.candidate_per_page * self.candidate_page):
                final_str += str(i + 1) + ". "
                final_str += self.candidate[self.candidate_page * self.candidate_per_page + i][0] + " (prob:"
                final_str += str(self.candidate[self.candidate_page * self.candidate_per_page + i][1]) + ") "
                final_str += "     "
        else:
            for i in range(self.candidate_per_page):
                final_str += str(i + 1) + ". "
                final_str += self.candidate[self.candidate_page * self.candidate_per_page + i][0] + " (prob:"
                final_str += str(self.candidate[self.candidate_page * self.candidate_per_page + i][1]) + ") "
                final_str += "   "

        self.ui.candidate.setText(final_str)
