# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:08:39 2020

@author: aammd
"""
from PIL import Image
import wx
import os
import photoprinter_gui as gui
import subprocess
import json
from pathlib import Path
import rawpy #install rawpy not by using CMD's "pip install rawpy" but go to 'anaconda propt' then use "pip install rawpy"
import exifread #via 'Anaconda prompt'
from pathlib import Path
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
MB_ICONINFORMATION = 0x00000040

"""PIL images need to be converted using im=im.convert('RGB')
Otherwise it cannot deal with 32 bit images.
Now both 8-32 bit images work fine."""


def RAW_to_PIL(filename):
    raw = rawpy.imread(filename)
    rgb = raw.postprocess(use_auto_wb =True,gamma=None,use_camera_wb=False,no_auto_bright=False,bright = 1.3)
    img = PIL.Image.fromarray(rgb)
    return img

def JPG_to_PIL(filename):
    return PIL.Image.open(filename)

def mark_as_edited():
    pass
def mark_as_printqueue():
    pass
def mark_as_printed():
    pass

#from StringIO import StringIO



try:
    del app
except:
    pass

class pictures():
    
    def __init__(self):
        self.picturemodes = ['Unedited','Edited','Print']
        # modes
        self.edited = "_EE"
        self.queue = "_QQ" # queue to be printed
        self.finished = "_PP"
        self.finished = "_FF"
        
        
    
    def checktype(self,filename = '',mode = 'Unedited'):
        mode = mode.lower()
            
        if mode == 'unedited':
            if self.edited not in filename and self.queue not in filename and self.finished not in filename:
                return True
            else:
                return False
        elif mode == 'edited':
            if self.edited in filename and self.finished not in filename:
                return True
            else:
                return False
        elif mode == 'print':
            if self.queue in filename and self.finished not in filename:
                return True
            else:
                return False
        else:
             raise ValueError("input to method checktype was incorrect")
            
        
    def getmodes(self):
        return self.picturemodes
    
    def AddToPath(self,path_in,string):
        filename, file_extension = os.path.splitext(path_in)
        filename += string
        filename += file_extension 
        path_out = filename
        os.rename(path_in,path_out)
        return path_out
    
        
    def addpicmode(self,path = '',mode='Edit'):
        mode = mode.lower()
        
        if mode == 'edit':
            path_new = self.AddToPath(path,self.edited)
            return path_new
        elif mode == 'queue':
            path_new = self.AddToPath(path,self.queue)
            return path_new
        elif mode == 'finished':
            path_new = path.replace(self.queue,self.finished)
            os.rename(path,path_new)
            return path_new
        elif mode == 'finished':
            path_new = path.replace(self.queue,self.finished)
            os.rename(path,path_new)
            return path_new
        else:
             raise ValueError("input to method addpicmode was incorrect")
        
        
    



def GetShortPath(dirpath):
    path = Path(dirpath)    
    a = os.path.basename(path.parent.parent)
    b = os.path.basename(path.parent)
    shortpath = os.path.join(a,b)
    return shortpath

import PIL
def get_date_taken(path):
    """EXIF date taken: 2017:06:04 hh/mn/ss
    Turns it to 17-06-04"""
    try:
        #this handles both .JPG and .NEF images. If you use PIL it can only handle JPG
        with open(path, 'rb') as fh:
            tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
            dateTaken = str(tags["EXIF DateTimeOriginal"])
            dateTaken = dateTaken[2:10].replace(':','-')
        
    except:
        dateTaken = '00-00-00'
        
    return dateTaken



    

class settings():
    
    def __init__(self):
        pass
    
    def settings_get(self):
        try:
            with open(Path(self.dirsettings,"settings.txt"), 'r') as file:
                settings = json.load(file)
                self.root_directory          = settings['root_directory']
                self.edit_exe                = settings['edit_exe']
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
                file.write(json.dumps({'root_directory'     : '',
                                       'edit_exe'           : r"C:\Program Files\Adobe\Adobe Lightroom\lightroom.exe"
                                       }))
                file.close()
                
    def settings_set(self):
        settingsfile = Path(self.dirsettings,"settings.txt")
        with settingsfile.open(mode='w') as file:
            file.write(json.dumps({'root_directory' : self.root_directory,
                                   'edit_exe' : self.edit_exe
                                   }))
            file.close()

rawtypes = ['3fr','ari','arw','bay','braw','crw','cr2','cr3','cap','data','dcs','dcr','dng','drf','eip','erf','fff','gpr',
            'iiq','k25','kdc','mdc','mef','mos','mrw','nef','nrw','obm','orf','pef', 'ptx','pxn','r3d', 'raf', 'raw', 'rwl', 
            'rw2', 'rwz','sr2', 'srf', 'srw','tif','x3f']
nonrawtypes = ['jpg','jpeg','png']
jpgtypes = ['jpg','jpeg']
pngtypes = ['png']
alltypes = nonrawtypes + rawtypes 

ext = ['jpg','png','nef']

listofextensions = ['.'+x for x in ext]

def CheckIfPrint(picname):
    pass
    if True:
        return True
    else:
        return False

def IsRAW(filepath):
    
    filename, file_extension = os.path.splitext(filepath)
    file_extension = file_extension.replace('.','')
    return file_extension.lower() in rawtypes

def IsJPG(filepath):
    filename, file_extension = os.path.splitext(filepath)
    return file_extension in nonrawtypes

def path_to_basename(filepath):
    filename = os.path.basename(filepath)
    basename,_ = os.path.splitext(filename)
    return basename



class MainFrame(wx.Frame,settings):
    
    def settextctrl(self):
        print(f"rootdirectory = {self.root_directory}")
        try:
            self.m_textDir.SetValue(self.root_directory)    
        except:
            self.m_textDir.SetValue('')
    """ INITIALIZE """
    def __init__(self,parent): 
        gui.MyFrame.__init__(self,parent)
        datadir = os.getenv("LOCALAPPDATA")
        app = Path(datadir,"PicPrinter")
        self.pictures = pictures()
        self.picturepath = None
        
        if not app.exists():
            app.mkdir()
        self.dirsettings = Path(app,"settings")
        dirs = [self.dirsettings]
        for item in dirs:
            if not item.exists():
                item.mkdir()
        self.notseenimages = []
        # settings
        self.settings_create()
        self.settings_get()   
        
        self.selectedrow = None
        #set grid
        self.m_grid.SetColLabelValue(0, "Name")
        self.m_grid.SetColLabelValue(1, "Type")
        self.m_grid.SetColLabelValue(2, "Directory")
        
        a = dir(self.m_choice)
        for x in a:
            if 'set' in x:
                print(x)
                
        self.imagetypes = ['All','JPG & PNG','RAW']
        
        
        self.choiceindex = 0
        self.choice2index = 0
        self.m_choice.SetItems(self.pictures.getmodes())
        self.m_choice.SetSelection(self.choiceindex)
        self.m_choice2.SetItems(self.imagetypes)
        self.m_choice2.SetSelection(self.choice2index)        
        
        self.Update()
        self.settextctrl()    
            
    def MyFrame1OnSize(self,event):
        pass
        
        
    def m_choiceOnChoice(self,event):
        self.choiceindex = self.m_choice.GetSelection()
        print(f"choice is now = {self.choiceindex}")
        pass
    
    def m_choice2OnChoice(self,event):
        pass
    """ BUTTONS """
    def btnEditOnButtonClick( self, event ):
        if self.picturepath:        
            self.picturepath = self.pictures.addpicmode(path = self.picturepath,mode='Edit')
            subprocess.Popen([self.edit_exe, self.picturepath], stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            
    def btnPrintQueueOnButtonClick(self,event):
        if self.picturepath:
            self.picturepath = self.pictures.addpicmode(path = self.picturepath,mode='Queue')
        
    def btnCollectPrintsOnButtonClick(self,event):
        if self.picturepath:    
            self.picturepath = self.pictures.addpicmode(path = self.picturepath,mode='finished')
    
    """ EVENTS """
    
    def m_gridOnGridCellLeftClick(self,event):
        
        a = event.GetRow()
        
        self.m_grid.SelectRow( a, addToSelected=False)
        index = a
        self.selectedrow = index
        filepath = self.pathlist[index]
        self.picturepath = filepath
        
        PanelWidth, PH = self.m_panelBitmap.GetSize()
        
        if IsRAW(filepath):
            image = RAW_to_PIL(filepath)
        else:
            image = JPG_to_PIL(filepath)
        #use convert RGB to deal with 32 bit images, they will otherwise display weird images as if it is scattered over multiple lines
        image = image.convert('RGB')
        width, height = image.size
        
        PanelHeight = round(float(PanelWidth)*height/width)
        
        if PanelHeight > PH:
            fraction = float(PH)/PanelHeight 
            PanelHeight = PH
            PanelWidth = round(fraction*PanelWidth)
        
        image = image.resize((PanelWidth, PanelHeight), PIL.Image.ANTIALIAS)    
        
        
        width, height = image.size
        image2 = wx.Image( width, height )
        image.tobytes() 
        
        image2.SetData( image.tobytes() )
        self.m_bitmap.SetBitmap(wx.Bitmap(image2))   
        

    def m_buttonOnButtonClick(self,parent):
        
        #reset
        
        NrRows = self.m_grid.GetNumberRows()
        if NrRows:
            self.m_grid.DeleteRows(pos=0, numRows=NrRows, updateLabels=True)
        
        
        self.piclist = []
        self.dirlist = []
        self.pathlist = []
        self.extensionlist = []
        self.mtimelist = [] 
        for root, dirs, files in os.walk(self.root_directory, topdown=True):
            for name in files:                   
                #variables
                path = os.path.join(root, name)
                filename, file_extension = os.path.splitext(path)
                if file_extension.lower() in listofextensions:
                    modes = self.pictures.getmodes()
                    
                    if self.pictures.checktype(filename=filename,mode=modes[self.choiceindex]):
                        #print(f"name = {name}")
                    
                        
                        self.piclist.append(name)
                        self.extensionlist.append(file_extension)
                        self.pathlist.append(path)
                        self.dirlist.append(GetShortPath(path))
                        #self.mtimelist.append(mtime)
        
        if self.piclist:
            self.m_grid.AppendRows(len(self.piclist))
            for i,item in enumerate(self.piclist):
                self.m_grid.SetCellValue(i,0,self.piclist[i])
                self.m_grid.SetCellValue(i,1,self.extensionlist[i])
                self.m_grid.SetCellValue(i,2,self.dirlist[i])
            
            
            for i in range(3):
                
                self.m_grid.AutoSizeColumn(i, setAsMin=True)
        else:
            MessageBox(0, "No photos were found.", "Message", MB_ICONINFORMATION)
        self.m_grid.ForceRefresh()
        self.Layout()
        self.Update()
            
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
                
    
	
    def btnDeleteOnButtonClick( self, event ):
        print(f"selected = {self.selectedrow}")
        if isinstance(self.selectedrow,int):
            self.m_grid.DeleteRows(pos=self.selectedrow, numRows=1, updateLabels=True)
            
            path = self.picturepath
            print(f"path to remove is {path}")
            os.remove(path)
            #update lists
            index = self.selectedrow
            self.piclist.pop(index)
            self.extensionlist.pop(index)
            self.pathlist.pop(index)
            self.dirlist.pop(index)
            # reset
            self.selectedrow = None
            self.picturepath = None
            
    
        
    def btnDeleteBothOnButtonClick( self, event ):
        
        filelist = []
        filelist_check = []
        
        if isinstance(self.selectedrow,int):
            print("selected")
            targetpath = self.picturepath
            targetname,_ = os.path.splitext(os.path.basename(targetpath))
            date_check = get_date_taken(targetpath)
            
            for path in self.pathlist:
                basename = path_to_basename(path)
                if basename == targetname:
                    
                    date = get_date_taken(path)
                    print(date)
                    print(f"check = {date_check}")
                    if date == date_check: #exclude pictures from different folders that happen to have the same name
                        filelist_check.append(basename)
                        filelist.append(path)
                    
            
            for path in filelist:
                os.remove(path)
            #lazy way of resetting the grid and lists
            self.selectedrow = None
            self.picturepath = None
            self.m_buttonOnButtonClick(None)
            
        
        
                
    
if __name__ == "__main__":
    # start the application
    app = wx.App(False) 
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
    del app
