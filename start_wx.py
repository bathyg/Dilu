import new_gui
import wx

'''
#Need to add to wxglade_out.py
import gettext
gettext.bindtextdomain('myapplication',
'/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext
'''

class MyFrame(new_gui.dilu_gui_main_frame):
    """"""
    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        new_gui.dilu_gui_main_frame.__init__(self, None, title="Dilu by Yu (Tom) Gao @TSRI", size=(850, 500))
        self.Show()


if __name__ == "__main__":

    run_queue=[]
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
