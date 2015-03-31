import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst
import signal
Gst.init(None)
signal.signal(signal.SIGINT, signal.SIG_DFL)
class Player:
    def __init__(self,song_name='started'):
        self.song_name = song_name
        #self.song_name = 'file://' + song_name
        print(self.song_name)

        self.pipeline = Gst.Pipeline()
        source = Gst.ElementFactory.make('filesrc', 'source')
        source.set_property('location', self.song_name)
        decodebin = Gst.ElementFactory.make('decodebin', 'decodebin')
        audioconvert = Gst.ElementFactory.make('audioconvert', 'audioconvert')
        volume = Gst.ElementFactory.make('volume', 'volume')
        audiosink = Gst.ElementFactory.make('autoaudiosink', 'audio-output')
        def on_pad_added(decodebin, pad):
            pad.link(audioconvert.get_static_pad('sink'))
        decodebin.connect('pad-added', on_pad_added)
        [self.pipeline.add(k) for k in [source, decodebin, audioconvert, volume, audiosink]]
        source.link(decodebin)
        audioconvert.link(volume)
        volume.link(audiosink)
        #self.playbin = Gst.ElementFactory.make('playbin', None)
        #self.pipeline.add(self.playbin)
        #self.playbin.set_property('uri', self.song_name)
        message_bus = self.pipeline.get_bus()
        message_bus.add_signal_watch()
        message_bus.connect('message', self.message_handler)
        self.pipeline.get_by_name('volume').set_property('volume', 1)
        self.pipeline.set_state(Gst.State.PAUSED)
        
    def play_stop(self):
        if self.pipeline.get_state(0)[1] == Gst.State.PLAYING:
            self.pipeline.set_state(Gst.State.PAUSED)
            print('paused')
            
        elif self.pipeline.get_state(0)[1] == Gst.State.PAUSED or self.pipeline.get_state(0)[1] == Gst.State.NULL:
            self.pipeline.set_state(Gst.State.PLAYING)
            print('playing')
        
            
    def shift_to(self,shift_time):
        pass
    def indicate(self):
        pass
    def setVolume(self,vol):
        pass
    def play_next(self,location):
        self.pipeline.set_state(Gst.State.NULL)
        self.pipeline.get_by_name('source').set_property('location', location)
        self.play_stop()
        

    def message_handler(self, bus, message):

        struct = message.get_structure()
        if message.type == Gst.MessageType.EOS:
            print('END')
        elif message.type == Gst.MessageType.TAG and message.parse_tag() and struct.has_field('taglist'):
            print('meta tags')
            taglist = struct.get_value('taglist')
            for x in range(taglist.n_tags()):
                name = taglist.nth_tag_name(x)
                print('  %s: %s' % (name, taglist.get_string(name)[1]))
        else:
            pass
if __name__ == "__main__":
    player = Player('/home/krop/Documents/Projects/PyMusicPlayer/song.ogg')
    player.play_stop()