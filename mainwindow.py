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
        self.songslide = QSlider(1)
        self.songslide.setMinimum(0)
        self.songslide.setMaximum(100)
        self.songslide.setSingleStep(1)
        self.volumeslide = QSlider(1)
        self.volumeslide.setMinimum(0)
        self.volumeslide.setMaximum(100)
        self.volumeslide.setSingleStep(10   )
        #listlay = QHBoxLayout()
        playlist = QTableView()
        PlayList_Model 	= QStringListModel()
        PlayList_Model.setStringList("Item 1;Item 2;Item 3;Item 4".split(";"))
        playlist.setModel(PlayList_Model)
        #listlay.addWidget(playlist)
        #listlay.addWidget(volumeslide)
        mainlayout = QVBoxLayout()
        butlayout = QHBoxLayout()
        butlayout.addWidget(prevbut)
        butlayout.addWidget(playbut)
        butlayout.addWidget(nextbut)
        butlayout.addWidget(openbut)
        mainlayout.addWidget(songtags)
        mainlayout.addWidget(self.volumeslide)
        mainlayout.addLayout(butlayout)
        mainlayout.addWidget(self.songslide)
        mainlayout.addWidget(playlist)
        self.setLayout(mainlayout)
        self.player = Player()
        #time_change = pyqtSignal(int)
        #self.Time = self.player.pipeline.get_clock().get_time()
        
        #time_change = pyqtSignal([self.player.pipeline.get_clock().get_time()], ['QString'])
        #QWidget.connect(playbut.clicked(),player.play_stop())
        QObject.connect(playbut, SIGNAL('clicked()'), self, SLOT('play()'))
        QObject.connect(nextbut, SIGNAL('clicked()'), self, SLOT('nextsong()'))
        QObject.connect(prevbut, SIGNAL('clicked()'), self, SLOT('prevsong()'))
        QObject.connect(openbut, SIGNAL('clicked()'), self, SLOT('Open_Song()'))
        QObject.connect(self.volumeslide, SIGNAL('valueChanged(int)'), self, SLOT('Volume_Set(int)'))
        QObject.connect(self.songslide, SIGNAL('valueChanged(int)'), self, SLOT('Seek_Set(int)'))
        #QObject.connect(self, SIGNAL('time_change(int)'), self, SLOT('show_time(int)'))
    
    '''@property
    def Time(self):
        return self.Time
    @Time.setter
    def Time(self):
        self.Time = self.player.pipeline.get_clock().get_time()
        self.time_change.emit(new_time,self.player.pipeline.get_clock().get_time())'''
    

    @pyqtSlot()
    def play(self):
        self.player.play_stop()
    @pyqtSlot()
    def nextsong(self):
        print(self.player.song_duration())
        print('next')
    @pyqtSlot()
    def prevsong(self):
        print('prev')
    @pyqtSlot()
    def Open_Song(self):
        
        file_name = QFileDialog.getOpenFileName(self,"Open Files", "~", "All Files (*.ogg)")
        if file_name=='':
            file_name = 'song.ogg'
        #self.player.play_next(file_name)
        self.songslide.setMaximum(self.player.play_next(file_name))
        #self.player.song_time()
        
    @pyqtSlot(int)
    def Volume_Set(self,vol):
        print(self.volumeslide.sliderPosition())
        self.player.setVolume(vol / 100)
    @pyqtSlot(int)
    def Seek_Set(self,sek):
        #print(self.songslide.sliderPosition())
        self.player.shift_to(sek)
    @pyqtSlot(int)
    def show_time(self,time):
        print(time)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #ignore()
    mainwindow = Mainwindow()
    mainwindow.setWindowTitle("PyMusicPlayer")
    mainwindow.show()
    mainwindow.resize(300, 500)
    sys.exit(app.exec_())


