import wx
import numpy as np 


height=1500
width=1500


class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Chess Game')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        btnStart = wx.Button(panel, label='Start', pos=(5, 55))
        btnExit = wx.Button(panel, label='Exit', pos=(100, 55))             
        my_sizer = wx.BoxSizer(wx.VERTICAL)        
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        

        #my_sizer.Add(btnStart, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer) 

        png1 = wx.Image('C:/Users/Mohamed-Lemine/Chess Project/GameBoard.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png1,(1,1),(width, height))  
        png2 = wx.Image('C:/Users/Mohamed-Lemine/Chess Project/Chess_bdt60.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png2, (50, 50), (40, 40))      
        self.Show()
        
class ImgPanel(wx.Panel):
    def __init__(self, parent, image):
        wx.Panel.__init__(self, parent)

        img = wx.Image(image, wx.BITMAP_TYPE_ANY)
        self.sBmp = wx.StaticBitmap(self, wx.ID_ANY, wx.BitmapFromImage(img))

        sizer = wx.BoxSizer()
        sizer.Add(item=self.sBmp, proportion=0, flag=wx.ALL, border=10)
        self.SetBackgroundColour('green')
        self.SetSizerAndFit(sizer)



if __name__ == '__main__':
    app = wx.App()
    Img = ImgPanel(parent=wx.App, image='C:/Users/Mohamed-Lemine/Chess Project/GameBoard.png')   
    frame = MyFrame()

    app.MainLoop()