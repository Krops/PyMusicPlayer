import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
try:
    from PyQt4.phonon import Phonon
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "Music Player",
            "Your Qt installation does not have Phonon support.",
            QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
            QtGui.QMessageBox.NoButton)
    sys.exit(1)
class Mainwindow(QWidget):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.aoutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mobject = Phonon.MediaObject(self)
        self.metainfo = Phonon.MediaObject(self)
        Phonon.createPath(self.mobject, self.aoutput)
        self.mobject.setTickInterval(1000)
        
        self.mobject.setCurrentSource(Phonon.MediaSource('song.ogg'))
        self.mobject.tick.connect(self.tock)
        #QObject.connect(self.mobject, SIGNAL('tick(int)'), self, SLOT('tock(int)'))
        #self.mobject.stateChanged.connect(self.stateChanged)
        #self.metainfo.stateChanged.connect(self.metaStateChanged)
        #self.mobject.currentSourceChanged.connect(self.sourceChanged)
        #self.mobject.aboutToFinish.connect(self.aboutToFinish)
        
        songtags = QLabel("PSY - GANGNAM STYLE")
        playbut = QPushButton(">")
        nextbut = QPushButton(">>")
        prevbut = QPushButton("<<")
        openbut = QPushButton("^")
        self.timeLcd = QLCDNumber()
        self.timeLcd.display("00:00") 
        self.songslide = Phonon.SeekSlider(self.mobject)
        #print(self.songslide.tracking)
        self.songslide.setSingleStep(1000)
        self.volumeslide = Phonon.VolumeSlider(self)
        self.volumeslide.setAudioOutput(self.aoutput)
        #listlay = QHBoxLayout()
        playlist = QTableView()
        PlayList_Model 	= QStringListModel()
        PlayList_Model.setStringList("Item 1;Item 2;Item 3;Item 4".split(";"))
        playlist.setModel(PlayList_Model)
        #listlay.addWidget(playlist)
        #listlay.addWidget(volumeslide)
        mainlayout = QVBoxLayout()
        butlayout = QHBoxLayout()
        butlayout.addWidget(self.timeLcd)
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
        QObject.connect(playbut, SIGNAL('clicked()'), self, SLOT('play_stop()'))
        QObject.connect(openbut, SIGNAL('clicked()'), self, SLOT('Open_Song()'))
        QObject.connect(nextbut, SIGNAL('clicked()'), self, SLOT('nextsong()'))
        QObject.connect(prevbut, SIGNAL('clicked()'), self, SLOT('prevsong()'))
        #QObject.connect(self.volumeslide, SIGNAL('valueChanged(int)'), self, SLOT('Volume_Set(int)'))
        #QObject.connect(self.mobject, SIGNAL('seekableChanged(bool)'), self, SLOT('Seek_Set(int)'))
    
    #@pyqtSlot(int)
    def tock(self,time):
        displayTime = QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.timeLcd.display(displayTime.toString('mm:ss'))
    @pyqtSlot()
    def play_stop(self):
        #print(self.mobject.state())
        
        '''if self.mobject.state() == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, "Fatal Error",
                        self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, "Error",
                        self.mediaObject.errorString())'''

        if self.mobject.state() == Phonon.PlayingState:
            self.mobject.pause()
            print('paused')
        elif self.mobject.state() == Phonon.PausedState:
            self.mobject.play()
            print('playing')
            
    @pyqtSlot()
    def Open_Song(self):
        file_name = QFileDialog.getOpenFileName(self,"Open Files",QDesktopServices.storageLocation(QDesktopServices.MusicLocation))
        if file_name=='':
            file_name = 'song.ogg'
        print(file_name)
        self.play_next(file_name)
        #self.songslide.setMaximum(self.play_next(file_name))
    @pyqtSlot(int)
    def Volume_Set(self,vol):
        print(self.volumeslide.sliderPosition())

    @pyqtSlot(int)
    def Seek_Set(self,sek):
        print(self.songslide.sliderPosition())

    @pyqtSlot()
    def nextsong(self):
        print('next')
    @pyqtSlot()
    def prevsong(self):
        print('prev')
    def play_next(self,location):
        self.mobject.stop()
        self.mobject.clearQueue()
        self.mobject.setCurrentSource(Phonon.MediaSource(location))
        self.metainfo.setCurrentSource(Phonon.MediaSource(location))
        self.mobject.play()
        #self.mobject.seekableChanged(True)
        #print(self.mobject.isSeekable())

        
if __name__ == "__main__":
    app = QApplication(sys.argv) #ignore()
    mainwindow = Mainwindow()
    mainwindow.setWindowTitle("PyMusicPlayer")
    mainwindow.show()
    mainwindow.resize(300, 500)
    sys.exit(app.exec_())