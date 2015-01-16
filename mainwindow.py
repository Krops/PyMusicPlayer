# [Create a window]

import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv) #ignore()
window = QWidget()
window.setWindowTitle("PyMusicPlayer")
window.show()

# [Add widgets to the widget]

# Create some widgets (these won't appear immediately):
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


# Put the widgets in a layout (now they start to appear):


# [Resizing the window]

# Let's resize the window:
window.resize(300, 500)

# The widgets are managed by the layout...
#window.resize(320, 180)

# [Run the application]

# Start the event loop...
sys.exit(app.exec_())