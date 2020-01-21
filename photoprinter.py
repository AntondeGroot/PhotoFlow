# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:08:39 2020

@author: aammd
"""
from PIL import Image
import wx
import os
import photoprinter_gui as gui

try:
    del app
except:
    pass

from pathlib import Path

#sources: http://www.blog.pythonlibrary.org/2011/11/02/wxpython-an-intro-to-the-ultimatelistctrl/
# https://stackoverflow.com/questions/15466244/adding-a-button-to-every-row-in-listctrl-wxpython


import json


from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

#packages = [('abiword', '5.8M', 'base'), ('adie', '145k', 'base'),
#    ('airsnort', '71k', 'base'), ('ara', '717k', 'base'), ('arc', '139k', 'base'),
#    ('asc', '5.8M', 'base'), ('ascii', '74k', 'base'), ('ash', '74k', 'base')]

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):

    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT |
                wx.SUNKEN_BORDER )
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)
        #self.setResizeColumn(1)

from pathlib import Path

def GetShortPath(dirpath):
    path = Path(dirpath)    
    a = os.path.basename(path.parent.parent)
    b = os.path.basename(path.parent)
    shortpath = os.path.join(a,b)
    return shortpath


class settings():
    
    def __init__(self):
        pass
    
    def settings_get(self):
        try:
            with open(Path(self.dirsettings,"settings.txt"), 'r') as file:
                settings = json.load(file)
                self.root_directory          = settings['root_directory']
            file.close()
        except:
            # Just in case when the settings.txt has been tempered with        
            settingsfile = Path(self.dirsettings,"settings.txt")
            if settingsfile.exists():
                settingsfile.unlink()
            self.settings_create()
            self.settings_get()
            
    def settings_create(self):
        settingsfile = Path(self.dirsettings,"settings.txt")
        if not settingsfile.exists():   
            with settingsfile.open(mode='w') as file:
                file.write(json.dumps({'root_directory'     : False
                                       }))
                file.close()
                
    def settings_set(self):
        settingsfile = Path(self.dirsettings,"settings.txt")
        with settingsfile.open(mode='w') as file:
            file.write(json.dumps({'root_directory' : self.root_directory
                                   }))
            file.close()

rawtypes = ['3fr','ari','arw','bay','braw','crw','cr2','cr3','cap','data','dcs','dcr','dng','drf','eip','erf','fff','gpr',
            'iiq','k25','kdc','mdc','mef','mos','mrw','nef','nrw','obm','orf','pef', 'ptx','pxn','r3d', 'raf', 'raw', 'rwl', 
            'rw2', 'rwz','sr2', 'srf', 'srw','tif','x3f']

ext = ['jpg','png','nef']
import subprocess
listofextensions = ['.'+x for x in ext]

def CheckIfPrint(picname):
    pass
    if True:
        return True
    else:
        return False






class MainFrame(wx.Frame,settings):
    
    def settextctrl(self):
        self.m_textDir.SetValue(self.root_directory)    
    
    
    """ INITIALIZE """
    def __init__(self,parent): 
        gui.MyFrame1.__init__(self,parent)
        datadir = os.getenv("LOCALAPPDATA")
        app = Path(datadir,"PicPrinter")
        if not app.exists():
            app.mkdir()
        self.dirsettings = Path(app,"settings")
        # settings
        self.settings_create()
        self.settings_get()
        
        
        #
        self.m_listCtrl = CheckListCtrl(self.m_panel)
        self.m_listCtrl.InsertColumn(0, '#',width=60)
        self.m_listCtrl.InsertColumn(1, 'Name')
        self.m_listCtrl.InsertColumn(2, 'Type')
        self.m_listCtrl.InsertColumn(3, 'Directory')
        
        
        
        a = dir(self.m_choice)
        for x in a:
            if 'set' in x:
                print(x)
                
        self.imagetypes = ['All','JPG & PNG','JPG','PNG','RAW']
        
        self.m_choice.SetItems(['Unedited','Edited','Print'])
        self.m_choice.SetSelection(0)
        self.m_choice2.SetItems(self.imagetypes)
        self.m_choice2.SetSelection(4)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.m_listCtrl, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        
        self.Update()
        self.settextctrl()    
        
        
        
        
        dirs = [self.dirsettings]
        
        for item in dirs:
            if not item.exists():
                item.mkdir()
                

    def imagetypelist(self):
        i = self.m_choice2.GetSelection()
        if i == 0:
            a = ['jpg','png','nef']
        elif i == 1:
            a = ['jpg','png']
        elif i == 2:
            a = ['jpg']
        elif i == 3:
            a = ['png']
        elif i == 4:
            a = ['nef']
        return a
            
    def MyFrame1OnSize(self,event):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.m_listCtrl, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Update()
        
        
    def m_choiceOnChoice(self,event):
        pass
    def m_choice2OnChoice(self,event):
        pass
    
    def m_buttonOnButtonClick(self,parent):
        
        
        
        piclist = []
        self.dirlist = []
        self.pathlist = []
        self.extensionlist = []
        for root, dirs, files in os.walk(self.root_directory, topdown=True):
            for name in files:       
                #print(f"name = {name}")
                #variables
                path = os.path.join(root, name)
                filename, file_extension = os.path.splitext(path)
                #print(f"bool = {file_extension in listofextensions}")
                if file_extension in listofextensions:
                    #relpath = os.path.relpath(path,basedir)
                    mtime = int(os.path.getmtime(path))
                    print(f"name = {name}")
                    print(f"mtime = {mtime}")
                    piclist.append(name)
                    self.extensionlist.append(file_extension)
                    self.pathlist.append(path)
                    print(Path(path).parents[1])
                    self.dirlist.append(GetShortPath(path))

        
        for i,item in enumerate(piclist):
            index = self.m_listCtrl.InsertItem(i, f"{i}")
            self.m_listCtrl.SetItem(index, 1, item)
            self.m_listCtrl.SetItem(index, 2, self.extensionlist[i])
            self.m_listCtrl.SetItem(index, 3, self.dirlist[i])
            
            
        
        
        for i in range(4):
            self.m_listCtrl.SetColumnWidth(i, wx.LIST_AUTOSIZE)
            
            print(self.m_listCtrl.GetColumn(i).GetText())
        
        self.Layout()
        self.Update()
    def m_listCtrlOnListColClick(self,click):
        pass
    def m_listCtrlOnListItemSelected(self,click):
        pass
    def m_gridOnGridCellLeftClick(self,click):
        #subprocess.Popen([r"C:\Program Files\Adobe\Adobe Lightroom\lightroom.exe", r'C:\Users\aammd\Desktop\coffee_idea.jpg'], stdin=None,
        #                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        col = click.GetCol()
        row = click.GetRow()
        print(f"col is {col}")
        if col == 0:
            try:
                path = self.pathlist[row]
                img = Image.open(path)
                img.show()
            except:
                print("Error opening image")
        if col == 1:
            filename = self.pathlist[row]
            dir_ = os.path.dirname(filename)
            subprocess.Popen(f"explorer {dir_}")
        if col == 3:
            
            filename = self.pathlist[row]
            subprocess.run([r"C:\Program Files\Adobe\Adobe Lightroom\lightroom.exe", filename], stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
    def m_buttonDirpickerOnButtonClick(self,event):
        
        with wx.DirDialog(self, "Choose which directory to select",style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,defaultPath=self.root_directory) as DirDialog:
            #fileDialog.SetPath(str(self.notesdir)+'\.')
            if DirDialog.ShowModal() == wx.ID_CANCEL:
                pass
                return None    # the user changed their mind
            else:
                self.root_directory = DirDialog.GetPath()
                self.settings_set()
                self.settextctrl()
                self.Update()
    
    def btnViewOnButtonClick( self, event ):
        selected = []
        for index in range(self.m_listCtrl.GetItemCount()):
            if self.m_listCtrl.IsChecked(index):
                selected.append(index)
                
        for index in selected:
            filename = self.pathlist[index]
            subprocess.run(f"explorer {filename}")
            
    def btnEditOnButtonClick( self, event ):
        selected = []
        for index in range(self.m_listCtrl.GetItemCount()):
            if self.m_listCtrl.IsChecked(index):
                selected.append(index)
        
        for index in selected:
            filename = self.pathlist[index]
            subprocess.Popen([r"C:\Program Files\Adobe\Adobe Lightroom\lightroom.exe", filename], stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        pass
	
    def btnDeleteOnButtonClick( self, event ):
        pass
    def m_btnFolderOnButtonClick(self,event):
        pass
                
                
    
if __name__ == "__main__":
    # start the application
    app = wx.App(False) 
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
    del app
