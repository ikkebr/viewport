import wx
import os
from subprocess import Popen

PATH_TO_VLC = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

class ViewFrameGenerator(wx.Frame):
    def __init__(self, parent, title):
        super(ViewFrameGenerator, self).__init__(parent, title=title, size=(1024,768))

        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        self.InitUI()
        self.Centre()


    def InitUI(self):
        wx.StaticText(self, label='x:', pos=(10,10))
        wx.StaticText(self, label='y:', pos=(10,30))
        wx.StaticText(self, label='w:', pos=(10,50))
        wx.StaticText(self, label='h:', pos=(10,70))
      
        self.str_x = wx.StaticText(self, label='', pos=(30, 10))
        self.str_y = wx.StaticText(self, label='', pos=(30, 30))
        self.str_w = wx.StaticText(self, label='', pos=(30, 50))
        self.str_h = wx.StaticText(self, label='', pos=(30, 70))

        start_btn = wx.Button(self, -1, 'Generate VLC ViewPort', (10, 90))

        self.Bind(wx.EVT_BUTTON,  self.on_start_click, id=start_btn.GetId())
        self.Bind(wx.EVT_MOVE, self.on_move)
        self.Bind(wx.EVT_SIZE, self.on_resize)


    def on_start_click(self, event):
        Popen(r'%s --qt-minimal-view --no-autoscale screen:// :screen-fps=5.000000 :live-caching=1 :screen-top=%d :screen-left=%d :screen-width=%d :screen-height=%d' % (PATH_TO_VLC, self.y-30, self.x, self.width-30, self.height-30))
        self.Hide()
        

    def on_move(self, e):
        self.x, self.y = e.GetPosition()
        self.str_x.SetLabel(str(self.x))
        self.str_y.SetLabel(str(self.y))


    def on_resize(self, e):
        self.width, self.height = e.GetSize()
        self.str_w.SetLabel(str(self.width))
        self.str_h.SetLabel(str(self.height))


app = wx.App()

frame = ViewFrameGenerator(None, title='Simple VLC ViewPort Generator')
frame.Show()

app.MainLoop()