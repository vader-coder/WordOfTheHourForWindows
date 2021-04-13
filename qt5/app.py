import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from loadHtml import loadFile

#app instance
app = QApplication(sys.argv)

#gui instance

window = QWidget()
window.setWindowTitle('App')
window.setGeometry(200, 200, 480, 480)
#window.move(60, 15)
helloWorld = '<h1>Hello World!</h1>'
helloMsg = QLabel(loadFile('words.html'), parent=window)
#helloMsg.move(60, 15)

#could use same html style from his website.

#show gui
window.show()

#run event loop
sys.exit(app.exec_())