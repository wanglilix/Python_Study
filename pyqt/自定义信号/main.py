import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets,QtCore
from untitled import *

class mywindow(QtWidgets.QWidget,Ui_Form):
    _signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myPrint)
        self._signal.connect(self.mySignal)


    def myPrint(self):
        self.textEdit.setText("正在打印，请稍候....")  
        self._signal.emit("你妹，打印结束了吗，快回答！")

    def mySignal(self,string):
        print(string)
        self.textEdit.append("打印结束。")

if __name__=="__main__":  
    import sys  
  
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()  
    myshow.show()
    sys.exit(app.exec_()) 

