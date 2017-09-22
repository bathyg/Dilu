#!/usr/bin/env python
# -*- coding: CP1252 -*-
# Windows, anaconda2
# wxpython 3.0 installed by: conda install wxpython
# do not use pip install wxpython, that will install wxpython 4.0 and has some issues now

import wx
import gettext
from numpy import arange, sin, pi
import matplotlib
import os
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import \
    FigureCanvasWxAgg as FigCanvas, \
    NavigationToolbar2WxAgg as NavigationToolbar

gettext.bindtextdomain('myapplication',
'/path/to/my/language/directory')
gettext.textdomain('myapplication')
_ = gettext.gettext
# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
def read_helper(filename):
    if os.path.isfile(filename):
        file1=open(filename,'rb')
        text_content=file1.read()
        file1.close()
        return text_content
    else:
        file1=open(filename,'wb')
        file1.write('#This is %s file' % filename.replace('.',' '))
        file1.close()
        return ('#File %s does not exist, created new one' % filename.replace('.',' '))




class dilu_gui_main_frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: dilu_gui_main_frame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE | wx.FULL_REPAINT_ON_RESIZE
        wx.Frame.__init__(self, *args, **kwds)
        id_file_text=read_helper('identification.helper')
        rt_file_text=read_helper('internal_std.helper')
        self.notebook_1 = wx.Notebook(self, wx.ID_ANY)
        self.tab1_addfiles = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.button_1 = wx.Button(self.tab1_addfiles, wx.ID_ANY, _("Add raw files to Group 1"))
        self.list_ctrl_3 = wx.ListCtrl(self.tab1_addfiles, style=wx.LC_LIST)
        self.button_2 = wx.Button(self.tab1_addfiles, wx.ID_ANY, _("Add raw files to Group 2"))
        self.list_ctrl_4 = wx.ListCtrl(self.tab1_addfiles, style=wx.LC_LIST)
        self.radio_box_1 = wx.RadioBox(self.tab1_addfiles, wx.ID_ANY, "", choices=[_("No correction"), _("Global TIC"), _("Cohort TIC"), _("Internal standards")], majorDimension=4, style=wx.RA_SPECIFY_COLS)
        self.text_ctrl_1 = wx.TextCtrl(self.tab1_addfiles, wx.ID_ANY, id_file_text, style=wx.TE_MULTILINE)
        self.btn_save_iden = wx.Button(self.tab1_addfiles, wx.ID_ANY, _("Save identification"))
        self.text_ctrl_2 = wx.TextCtrl(self.tab1_addfiles, wx.ID_ANY, rt_file_text, style=wx.TE_MULTILINE)
        self.btn_save_internal_std = wx.Button(self.tab1_addfiles, wx.ID_ANY, _("Save internal standards"))
        self.btn_add_queue = wx.Button(self.tab1_addfiles, wx.ID_ANY, _("Add to queue"))
        self.btn_preview = wx.Button(self.tab1_addfiles, wx.ID_ANY, _("Preview raw file"))
        self.tab2_setparam = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.tab3_addqueue = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.tab4_viewres = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.tab5_advset = wx.Panel(self.notebook_1, wx.ID_ANY)

        self.panel = self.tab1_addfiles
        self.dpi = 100
        self.fig = Figure((3.0, 8.0), dpi=self.dpi)
        self.canvas = FigCanvas(self.panel, -1, self.fig)
        self.axes = self.fig.add_subplot(111)
        self.canvas.mpl_connect('pick_event', self.on_pick)
        self.toolbar = NavigationToolbar(self.canvas)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onOpenDirectory, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.onOpenDirectory2, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.draw_figure, self.btn_preview)
        self.Bind(wx.EVT_BUTTON, self.save_id_file, self.btn_save_iden)
        self.Bind(wx.EVT_BUTTON, self.save_std_file, self.btn_save_internal_std)
        # end wxGlade
        #self.draw_figure()

    def save_id_file(self, event):
        file_content=self.text_ctrl_1.GetValue()
        file1=open('identification.helper', 'wb')
        file1.write(file_content)
        file1.close()

    def save_std_file(self, event):
        file_content=self.text_ctrl_2.GetValue()
        file1=open('internal_std.helper', 'wb')
        file1.write(file_content)
        file1.close()

    def scale_bitmap(self, bitmap, width, height):
        image = bitmap.ConvertToImage()
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.Bitmap(image)
        return result

    def __set_properties(self):
        # begin wxGlade: dilu_gui_main_frame.__set_properties
        self.SetTitle(_("frame"))
        self.SetSize((1200, 800))
        self.radio_box_1.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: dilu_gui_main_frame.__do_layout
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self.tab1_addfiles, wx.ID_ANY, _("Group 1   "))
        sizer_1.Add(label_1, 0, 0, 0)
        sizer_1.Add(self.button_1, 1, 0, 0)
        sizer_5.Add(sizer_1, 0, wx.EXPAND, 0)
        sizer_5.Add(self.list_ctrl_3, 1, wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 0)
        label_2 = wx.StaticText(self.tab1_addfiles, wx.ID_ANY, _("Group 2   "))
        sizer_2.Add(label_2, 0, 0, 0)
        sizer_2.Add(self.button_2, 1, 0, 0)
        sizer_5.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_5.Add(self.list_ctrl_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.radio_box_1, 0, wx.EXPAND, 0)
        sizer_4.Add(sizer_5, 2, wx.EXPAND, 0)

        sizer_7.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        sizer_7.Add(self.toolbar,0, wx.EXPAND)
        sizer_7.AddSpacer(10)
        sizer_7.Add(self.btn_preview,0,wx.ALIGN_CENTER,0)
        #sizer_7.Fit(self)
        sizer_4.AddSpacer(10)
        sizer_4.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_4.AddSpacer(10)

        sizer_6.Add(self.text_ctrl_1, 3, wx.ALL | wx.EXPAND, 0)
        sizer_6.Add(self.btn_save_iden, 0, wx.ALIGN_CENTER, 0)
        sizer_6.Add(self.text_ctrl_2, 3, wx.ALL | wx.EXPAND, 0)
        sizer_6.Add(self.btn_save_internal_std, 0, wx.ALIGN_CENTER, 0)
        sizer_6.Add(self.btn_add_queue, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        self.tab1_addfiles.SetSizer(sizer_4)
        self.notebook_1.AddPage(self.tab1_addfiles, _("1. Add raw files"))
        self.notebook_1.AddPage(self.tab2_setparam, _("2. Viewer"))
        self.notebook_1.AddPage(self.tab3_addqueue, _("3. Job scheduler"))
        self.notebook_1.AddPage(self.tab4_viewres, _("4. View result"))
        self.notebook_1.AddPage(self.tab5_advset, _("5. Advanced settings"))
        sizer_3.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_3)
        self.Layout()
        self.SetSize((1200, 800))
        # end wxGlade

    def on_pick(self, event):
        # The event received here is of the type
        # matplotlib.backend_bases.PickEvent
        #
        # It carries lots of information, of which we're using
        # only a small amount here.
        #
        box_points = event.artist.get_bbox().get_points()
        msg = "You've clicked on a bar with coords:\n %s" % box_points

        dlg = wx.MessageDialog(
            self,
            msg,
            "Click!",
            wx.OK | wx.ICON_INFORMATION)

        dlg.ShowModal()
        dlg.Destroy()



    def onOpenDirectory(self, event):
        """"""
        with wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="Thermo raw file (*.raw;*.RAW)|*.raw;*.RAW|" \
           "All files (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        ) as dlg:
            self.list_ctrl_3.DeleteAllItems()
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            paths = dlg.GetPaths()
            for index, path in enumerate(paths):
                self.list_ctrl_3.InsertItem(index, path)




    def onOpenDirectory2(self, event):
        """"""
        with wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="Thermo raw file (*.raw;*.RAW)|*.raw;*.RAW|" \
           "All files (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        ) as dlg:
            self.list_ctrl_4.DeleteAllItems()
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            paths = dlg.GetPaths()
            for index, path in enumerate(paths):
                self.list_ctrl_4.InsertItem(index, path)

    def draw_figure(self, event):
        """ Redraws the figure
        """
        str = "1 2 4 6"
        self.data = map(int, str.split())
        x = range(len(self.data))

        # clear the axes and redraw the plot anew
        #
        self.axes.bar
        self.axes.clear()

        self.axes.bar(left=x, height=self.data, width=20 / 100.0, align='center', alpha=0.44, picker=5)

        self.canvas.draw()
# end of class dilu_gui_main_frame
