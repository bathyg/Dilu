import glob
import os
import wx
import subprocess
import shutil
import time

wildcard = "Thermo raw file (*.raw;*.RAW)|*.raw;*.RAW|" \
           "All files (*.*)|*.*"
tic_mode = 2
pos_neg = 'negative'

########################################################################
class MyPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        self.list_ctrl = wx.ListCtrl(self,
                                     style=wx.LC_REPORT
                                           | wx.BORDER_SUNKEN
                                     )
        self.list_ctrl.InsertColumn(0, 'Group1')
        self.list_ctrl.SetColumnWidth(0, 300)
        self.list_ctrl2 = wx.ListCtrl(self,
                                      style=wx.LC_REPORT
                                            | wx.BORDER_SUNKEN
                                      )

        self.list_ctrl2.InsertColumn(0, 'Group2')
        self.list_ctrl2.SetColumnWidth(0, 300)

        btn = wx.Button(self, label="Open raw files")
        btn.Bind(wx.EVT_BUTTON, self.onOpenDirectory)
        btn2 = wx.Button(self, label="Open raw files")
        btn2.Bind(wx.EVT_BUTTON, self.onOpenDirectory2)
        btn3 = wx.Button(self, label="Add to queue")
        btn3.Bind(wx.EVT_BUTTON, self.Add_Queue)
        btn4 = wx.Button(self, label="Run queue")
        btn4.Bind(wx.EVT_BUTTON, self.Run_Dilu)
        rb1 = wx.RadioButton(self, -1, label="Global tic")
        rb2 = wx.RadioButton(self, -1, label="Cohort tic")
        rb3 = wx.RadioButton(self, -1, label="No correction")
        lblList = ['Negative mode', 'Positive mode']

        self.rbox = wx.RadioBox(self, label='Mode', pos=(80, 10), choices=lblList,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.rbox.Bind(wx.EVT_RADIOBOX, self.OnRadiogroup2)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

        # rbox = wx.RadioBox(-1,label='Correction method', majorDimension=1, style=wx.RA_SPECIFY_COLS)
        # rbox.Bind(wx.EVT_RADIOBOX, self.onRadioBox)
        sizer0=wx.BoxSizer(wx.HORIZONTAL)
        sizer4=wx.BoxSizer(wx.VERTICAL)
        sizer5=wx.BoxSizer(wx.HORIZONTAL)
        self.textbox= wx.TextCtrl(self,size = (500,380),style = wx.TE_MULTILINE)
        sizer4.Add(self.textbox,  0, wx.ALL | wx.CENTER, 5)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer2 = wx.BoxSizer(wx.VERTICAL)
        sizer3 = wx.BoxSizer(wx.HORIZONTAL)

        sizer3.Add(rb1, 0, wx.ALL | wx.CENTER, 5)
        sizer3.Add(rb2, 0, wx.ALL | wx.CENTER, 5)
        sizer3.Add(rb3, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(sizer3, 1, wx.ALL | wx.EXPAND, 0)
        sizer.Add(sizer1, 1, wx.ALL | wx.EXPAND, 0)
        sizer.Add(sizer2, 1, wx.ALL | wx.EXPAND, 0)
        sizer1.Add(self.list_ctrl, 1, wx.ALL | wx.EXPAND, 5)
        sizer1.Add(btn, 0, wx.ALL | wx.CENTER, 5)
        sizer2.Add(self.list_ctrl2, 1, wx.ALL | wx.EXPAND, 5)
        sizer2.Add(btn2, 0, wx.ALL | wx.CENTER, 5)
        sizer5.Add(self.rbox,0, wx.ALL | wx.CENTER, 5)
        sizer5.Add(btn4, 0, wx.ALL | wx.CENTER, 5)
        sizer2.Add(btn3, 0, wx.ALL | wx.CENTER, 5)
        sizer4.Add(sizer5, 1, wx.ALL | wx.EXPAND, 0)
        sizer0.Add(sizer, 1, wx.ALL | wx.EXPAND, 0)

        sizer0.Add(sizer4, 1, wx.ALL | wx.EXPAND, 0)


        self.SetSizer(sizer0)

    # ----------------------------------------------------------------------
    def OnRadiogroup(self, e):
        global tic_mode
        rb = e.GetEventObject()
        label_get = rb.GetLabel()
        if label_get == "Global tic":
            tic_mode = 1
        if label_get == "Cohort tic":
            tic_mode = 2
        if label_get == "No correction":
            tic_mode = 3

    def OnRadiogroup2(self, e):
        global pos_neg

        label_get = self.rbox.GetStringSelection()
        if label_get == "Positive mode":
            pos_neg = 'positive'
        if label_get == "Negative mode":
            pos_neg = 'negative'

    def onOpenDirectory(self, event):
        """"""
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
        )
        self.list_ctrl.DeleteAllItems()
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for index, path in enumerate(paths):
                self.list_ctrl.InsertStringItem(index, path)
        dlg.Destroy()

    # ----------------------------------------------------------------------



    def onOpenDirectory2(self, event):
        """"""
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
        )
        self.list_ctrl2.DeleteAllItems()
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for index, path in enumerate(paths):
                if path[-4:]=='.raw' or path[-4:]=='.RAW':
                    self.list_ctrl2.InsertStringItem(index, path)
        dlg.Destroy()

    def Run_Dilu(self, event):

        for each_item in run_queue:
            p_q=subprocess.Popen(each_item)
            p_q.communicate()


    def Add_Queue(self, event):
        count = self.list_ctrl.GetItemCount()
        count2 = self.list_ctrl2.GetItemCount()
        filenames = []
        for row in range(count):
            item = self.list_ctrl.GetItem(itemId=row, col=0)
            filenames.append(item.GetText())
        for row in range(count2):
            item = self.list_ctrl2.GetItem(itemId=row, col=0)
            filenames.append(item.GetText())
        filenames2 = []

        dilu_analysis_dir = os.path.dirname(filenames[0]) + '\\dilu_analysis'+time.strftime("%Y%m%d_%H%M%S")
        if not os.path.exists(dilu_analysis_dir):
            os.makedirs(dilu_analysis_dir)

        for each_name in filenames:
            new_each_name = each_name[:-4] + '.ms1'
            new_each_name2 = each_name[:-4] + '.ms2'
            print(new_each_name,dilu_analysis_dir)
            shutil.move(new_each_name, dilu_analysis_dir)
            shutil.move(new_each_name2, dilu_analysis_dir)
            new_each_name = dilu_analysis_dir+'\\'+os.path.basename(each_name)[:-4]+'.ms1'
            new_each_name2 = dilu_analysis_dir+'\\'+os.path.basename(each_name)[:-4]+'.ms2'
            filenames2.append(new_each_name)
        ret_corr=' '.join(['0']*len(filenames))
        tic_corr = ' '.join(['1'] * len(filenames))
        exe_line = 'python ' + own_path + '\\go.py --input ' + ' '.join(filenames2) + ' --corr ' + str(tic_mode) + ' --output ' + dilu_analysis_dir + ' --ret_corr '+ ret_corr +' --tic_corr '+tic_corr+' --database lmsd.tsv 15 '+pos_neg
        self.textbox.AppendText(exe_line)
        self.textbox.AppendText('\n')
        run_queue.append(exe_line)
        """
        print exe_line
        p = subprocess.Popen(exe_line)
        p.communicate()
        """

########################################################################
class MyFrame(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Dilu by Yu (Tom) Gao @TSRI", size=(850, 500))
        panel = MyPanel(self)
        self.Show()


if __name__ == "__main__":
    global own_path
    own_path = os.path.dirname(os.path.realpath(__file__))
    run_queue=[]
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
