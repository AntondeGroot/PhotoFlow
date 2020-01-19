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
        
        
        self.settextctrl()    
        
        
        
        
        dirs = [self.dirsettings]
        
        for item in dirs:
            if not item.exists():
                item.mkdir()
        
        
        self.m_grid.SetColLabelValue(0, "View Pic")
        self.m_grid.SetColLabelValue(1, "View Folder")
        self.m_grid.SetColLabelValue(2, "Delete")
        self.m_grid.SetColLabelValue(3, "Lightroom")
        
        
    def m_buttonOnButtonClick(self,parent):
        
        directory = r'C:\Users\aammd\Desktop'
        
        piclist = []
        self.dirlist = []
        self.pathlist = []
        for root, dirs, files in os.walk(directory, topdown=True):
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
                    self.pathlist.append(path)
                    print(Path(path).parents[1])
                    
                    #self.dirlist.append()
                    if CheckIfPrint(path):
                        pass
        rownr = self.m_grid.GetNumberRows()
        nr = len(piclist) - rownr
        self.m_grid.AppendRows(numRows=nr, updateLabels=True)
        for i,item in enumerate(piclist):
            
            self.m_grid.SetCellValue(i, 0,f"{item}")
            self.m_grid.SetCellBackgroundColour(i, 2, 'red')
        self.m_grid.AutoSizeColumn(0, setAsMin = True)
        
        self.Update()
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
            subprocess.Popen([r"C:\Program Files\Adobe\Adobe Lightroom\lightroom.exe", filename], stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
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
                
                
                
    
if __name__ == "__main__":
    # start the application
    app = wx.App(False) 
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
    del app
