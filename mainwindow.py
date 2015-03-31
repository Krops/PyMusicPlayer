# [Create a window]

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from player import Player
class Mainwindow(QWidget):
    def __init__(self):
        super(Mainwindow, self).__init__()
        songtags = QLabel("PSY - GANGNAM STYLE")
        playbut = QPushButton(">")
        nextbut = QPushButton(">>")
        prevbut = QPushButton("<<")
        openbut = QPushButton("^")
        songslide = QSlider(1)
        volumeslide = QSlider(1)
        #listlay = QHBoxLayout()
        playlist = QTableView()
        #listlay.addWidget(playlist)
        #listlay.addWidget(volumeslide)
        mainlayout = QVBoxLayout()
        butlayout = QHBoxLayout()
        butlayout.addWidget(prevbut)
        butlayout.addWidget(playbut)
        butlayout.addWidget(nextbut)
        butlayout.addWidget(openbut)
        mainlayout.addWidget(songtags)
        mainlayout.addWidget(volumeslide)
        mainlayout.addLayout(butlayout)
        mainlayout.addWidget(songslide)
        mainlayout.addWidget(playlist)
        self.setLayout(mainlayout)
        self.player = Player('/home/krop/Documents/Projects/PyMusicPlayer/song.ogg')
        #QWidget.connect(playbut.clicked(),player.play_stop())
        QObject.connect(playbut, SIGNAL('clicked()'), self, SLOT('play()'))
        QObject.connect(nextbut, SIGNAL('clicked()'), self, SLOT('nextsong()'))
        QObject.connect(prevbut, SIGNAL('clicked()'), self, SLOT('prevsong()'))
        QObject.connect(openbut, SIGNAL('clicked()'), self, SLOT('Open_Song()'))

    @pyqtSlot()
    def play(self):
        self.player.play_stop()
    @pyqtSlot()
    def nextsong(self):
        print('next')
    @pyqtSlot()
    def prevsong(self):
        print('prev')
    @pyqtSlot()
    def Open_Song(self):
        file_name = QFileDialog.getOpenFileName(self,"Open Files", "/home/krop", "All Files (*.ogg)")
        self.player.play_next(file_name)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #ignore()
    mainwindow = Mainwindow()
    mainwindow.setWindowTitle("PyMusicPlayer")
    mainwindow.show()
    mainwindow.resize(300, 500)
    sys.exit(app.exec_())


