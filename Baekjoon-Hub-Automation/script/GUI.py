import sys
import process
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import webbrowser
from PyQt5.QtGui import QIcon
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
form= uic.loadUiType(BASE_DIR + r'\gui.ui')[0]



class Thread(QThread):
    count_signal = pyqtSignal(int)
    end_signal = pyqtSignal()
    fail_signal = pyqtSignal()
    def __init__(self, parent):
        super().__init__(parent)
        self.id=''
        self.pw = ''
        self.ischecked=False
        self.driver=None
        self.wait_time=5.5

    def run(self):
        self.elem=process.start_setting_BJ(self.id, self.pw, self.ischecked, self.driver)
        if self.elem==-1:
            self.fail_signal.emit()
            self.quit()
            self.wait(100)
            return

        self.count_signal.emit(len(self.elem)*self.wait_time)
        process.start_BJ(self.id,self.elem,self.driver,self.wait_time)
        self.end_signal.emit()
        self.quit()
        self.wait(100)






class Window(QMainWindow, form) :
    def __init__(self) :
        super().__init__()
        self.id=''
        self.pw=''

        self.up=False
        self.setupUi(self)
        self.driver=process.set_chrome_driver()
        self.driver.get("https://www.acmicpc.net/")
        self.blog_button.clicked.connect(self.blog_button_push)
        self.EP_button.clicked.connect(self.EP_button_push)
        self.programme_start_button.clicked.connect(self.programme_start_button_push)
        self.non_auto_button.clicked.connect(self.non_auto_button_push)
        self.apply_button.clicked.connect(self.apply_button_push)
        self.setWindowTitle("백준 허브 자동 업로드 프로그램 -플레이스")
        self.setWindowIcon(QIcon(BASE_DIR + r'\BHA_icon.png'))



    def blog_button_push(self) :
        webbrowser.open("https://gameplace.tistory.com/")

    def EP_button_push(self):
        process.start_EP(self.driver)

    def warning(self):
        QMessageBox.warning(self, '경고', 'ID나 PW가 입력되지 않았습니다.\nID와 PW를 입력 후 적용 버튼을 눌러주세요.')

    def apply_button_push(self):
        self.id=self.ID_Box.text()
        self.pw=self.PW_Box.text()
        self.up=True
        QMessageBox.information(self, '정보', '입력 완료')


    def programme_start_button_push(self):
        if(self.up==True):
            self.T = Thread(self)
            self.T.end_signal.connect(self.end)
            self.T.count_signal.connect(self.predict)
            self.T.fail_signal.connect(self.fail)
            self.T.id = self.id
            self.T.pw = self.pw
            self.T.ischecked = self.non_auto_bool.isChecked()
            self.T.driver = self.driver
            self.T.up = self.up
            self.T.wait_time=self.wait_time_setting.value()
            self.T.start()
        else:
            self.warning()


    def end(self):
        QMessageBox.information(self, '정보', '모든 업로드가 완료 되었습니다.')
    def fail(self):
        QMessageBox.warning(self, '경고', 'ID나 PW가 잘못되거나,\nreCAPTCHA로 인해 로그인이 되지 않았습니다.\n다시 시도해 주세요.')


    def predict(self,i):
        self.time_label.setText(" %d 분 %d 초"%(i//60,i%60))



    def non_auto_button_push(self):
        process.start_nat_BJ(self.driver)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
