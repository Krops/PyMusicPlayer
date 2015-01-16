# [Create a window]

import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv) #ignore()
window = QWidget()
window.setWindowTitle("PyMusicPlayer")
window.show()

# [Add widgets to the widget]

songtags = QLabel("PSY - GANGNAM STYLE")
playbut = QPushButton(">")
nextbut = QPushButton(">>")
prevbut = QPushButton("<<")
songslide = QSlider(1)
playlist = QTableView()
mainlayout = QVBoxLayout(window)
butlayout = QHBoxLayout()
butlayout.addWidget(prevbut)
butlayout.addWidget(playbut)
butlayout.addWidget(nextbut)
mainlayout.addWidget(songtags)
mainlayout.addLayout(butlayout)
mainlayout.addWidget(songslide)
mainlayout.addWidget(playlist)


window.resize(300, 500)


sys.exit(app.exec_())