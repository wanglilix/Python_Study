import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QLineEdit,QInputDialog
from PyQt5 import QtWidgets,QtCore
from untitled import *


class mywindow(QtWidgets.QWidget,Ui_Form):
    _signal = QtCore.pyqtSignal(str)
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myPrint)
        self._signal.connect(self.mySignal)
        self.pushButton_2.clicked.connect(self.msg)
        self.dial.sliderMoved['int'].connect(self.myPrint2)

    def msg(self):
        QMessageBox.information(self,"标题","马上退出",QMessageBox.Yes|QMessageBox.No)
        doubleNum,ok1 = QInputDialog.getDouble(self,"标题","计数：",37.56,-1000,1000,2)
        intNum,ok2 = QInputDialog.getInt(self,"标题","计数：",37,-1000,1000,2)
        stringNum,ok3 = QInputDialog.getText(self,"标题","姓名",QLineEdit.Normal,"王尼玛")
        items = ["Spring","Summer","Fall","Winter"]
        item ,ok4 = QInputDialog.getItem(self,"标题","Season:",items,1,True)
        text,ok5 = QInputDialog.getMultiLineText(self,"标题","Address:","John Doe\nFreedom Street")


    def myPrint(self):
        self.textEdit.setText("正在打印，请稍候....")  
        self._signal.emit("你妹，打印结束了吗，快回答！")


    def myPrint2(self,int):
        self.textEdit.setText(str(int))

    def mySignal(self,string):
        print(string)
        self.textEdit.append("打印结束。")

if __name__=="__main__":
    import sys  
  
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()  
    myshow.show()
    sys.exit(app.exec_()) 

