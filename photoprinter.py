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
import shutil
import json
from pathlib import Path
import rawpy #install rawpy not by using CMD's "pip install rawpy" but go to 'anaconda propt' then use "pip install rawpy"
import exifread #via 'Anaconda prompt'
import PIL
import ctypes
from send2trash import send2trash

MessageBox = ctypes.windll.user32.MessageBoxW
MB_ICONINFORMATION = 0x00000040
PIL.Image.MAX_IMAGE_PIXELS = 1000000000  #max image size of 1GB: otherwise it will throw errors for 300MB panoramas
                             

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



try:
    del app
except:
    pass

class pictures():
    
    def __init__(self):
        self.picturemodes = ['Unedited','Edited','Print queue','Printed']
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
        elif mode == 'print queue':
            if self.queue in filename and self.finished not in filename:
                return True
            else:
                return False
        elif mode == 'printed':
            if self.finished in filename:
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
            """If you want to edit an image it will add the appropriate suffix to the filename
            If it has already been edited before it will not add it again
            If it is already in the printqueue but you want to touch it up, it will not add it."""
            if self.edited not in path and self.queue not in path:
                path_new = self.AddToPath(path,self.edited)
            else:
                path_new = path
            return path_new
        
        elif mode == 'queue':
            if self.queue not in path:
                path_new = self.AddToPath(path,self.queue)
            else:
                path_new = path
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
                self.export_directory        = settings['export_directory']
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
                                       'edit_exe'           : r"C:\Program Files\Adobe\Adobe Lightroom\lightroom.exe",
                                       'export_directory'   : ''
                                       }))
                file.close()
                
    def settings_set(self):
        settingsfile = Path(self.dirsettings,"settings.txt")
        with settingsfile.open(mode='w') as file:
            file.write(json.dumps({'root_directory' : self.root_directory,
                                   'edit_exe' : self.edit_exe,
                                   'export_directory' : self.export_directory
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

def IsNotRAW(filepath):
    filename, file_extension = os.path.splitext(filepath)
    file_extension = file_extension.replace('.','')
    return file_extension.lower() in nonrawtypes

def path_to_basename(filepath):
    filename = os.path.basename(filepath)
    basename,_ = os.path.splitext(filename)
    return basename



class MainFrame(wx.Frame,settings):
    
    def settextctrl(self):
        try:
            self.m_textDir.SetValue(self.root_directory)    
        except:
            self.m_textDir.SetValue('')
        try:
            self.m_textDirExe.SetValue(self.edit_exe)    
        except:
            self.m_textDirExe.SetValue('')    
            
    """ INITIALIZE """
    def __init__(self,parent): 
        gui.MyFrame.__init__(self,parent)
        datadir = os.getenv("LOCALAPPDATA")
        app = Path(datadir,"PhotoPrinter")
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
        
        self.imagerotation = 0
        self.choiceindex = 0
        #self.choice2index = 0
        self.m_choice.SetItems(self.pictures.getmodes())
        self.m_choice.SetSelection(self.choiceindex)
        #self.m_choice2.SetItems(self.imagetypes)
        #self.m_choice2.SetSelection(self.choice2index)        
        
        self.Update()
        self.settextctrl()    
        
        #accelerators
        
        IDup = wx.NewIdRef()
        IDdown = wx.NewIdRef()
        IDdel = wx.NewIdRef()  #delete both
        IDenter = wx.NewIdRef() #select both to queue
        IDspace = wx.NewIdRef()
        self.Bind( wx.EVT_MENU, self.m_btnUpOnButtonClick, id = IDup    )
        self.Bind( wx.EVT_MENU, self.m_btnDownOnButtonClick, id = IDdown    )
        self.Bind( wx.EVT_MENU, self.btnDeleteBothOnButtonClick, id = IDdel    )
        self.Bind( wx.EVT_MENU, self.btnPrintQueueBothOnButtonClick, id = IDenter    )
        self.Bind( wx.EVT_MENU, self.btnPrintQueueOnButtonClick, id = IDspace    )
        
        entries = wx.AcceleratorTable([(wx.ACCEL_NORMAL, wx.WXK_UP,   IDup),(wx.ACCEL_NORMAL, wx.WXK_DOWN,   IDdown),
                                       (wx.ACCEL_NORMAL, wx.WXK_DELETE,   IDdel),(wx.ACCEL_NORMAL, wx.WXK_RETURN,   IDenter),
                                       (wx.ACCEL_NORMAL, wx.WXK_SPACE,   IDspace)])
        self.SetAcceleratorTable(entries)    
        
    #%% functions
    def updategrid(self,index = None):
        if isinstance(index,int):
            self.pathlist.pop(index)
            self.m_grid.DeleteRows(pos=index, numRows=1, updateLabels=True)

    def resetimage(self):
        emptyimage = PIL.Image.new("RGB", (1,1),"white")
        image = wx.Image( 1, 1 )
        image.SetData( emptyimage.tobytes() )        
        self.m_bitmap.SetBitmap(wx.Bitmap(image))

    def selectlastrow(self):
        try:
            self.m_grid.SelectRow( self.selectedrow, addToSelected=False)
        except:
            if self.selectedrow:
                while True:
                    if self.selectedrow >= 0:
                        try:
                            self.selectedrow -= 1
                            self.m_grid.SelectRow( self.selectedrow, addToSelected=False)
                            break
                        except:
                            pass
                    else:
                        break

    def showimagefromindex(self,index):
        try:
            self.m_grid.SelectRow( index, addToSelected=False)
            
            self.selectedrow = index
            filepath = self.pathlist[index]
            self.picturepath = filepath
            
            PanelWidth, PH = self.m_panelBitmap.GetSize()
            
            if IsRAW(filepath):
                image = RAW_to_PIL(filepath)
            else:
                image = JPG_to_PIL(filepath)
            image = image.rotate(self.imagerotation)
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
        except:
            self.resetimage()
    def find_JPGRAW_files(self):
        """find both JPG and RAW files and return their indices in descending order
        so that you can easily delete their entries without making a counting mistake."""
        filelist = []
        filelist_check = []
        rowindices = []
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
                        rowindices.append(self.pathlist.index(path))
                    
            rowindices = sorted(rowindices,reverse=True)
            print(f"rowindices = {rowindices}")
        return rowindices, filelist
    def delete_JPGRAW_files(self,indices,filelist):
        if isinstance(self.selectedrow,int):
            for i,rowindex in enumerate(indices):
                path = filelist[0]
                filelist.pop(0)
                send2trash(path)
                self.updategrid(index = rowindex)
    def looknextimageinstance(self, mode):
        """"""
        if isinstance(self.selectedrow,int):
            try:
                filepath = self.pathlist[self.selectedrow]
                filename, file_extension = os.path.splitext(filepath)
                i = 0
                index = self.selectedrow
                while i < 10:
                    i += mode
                    try:
                        index += mode
                        filepath = self.pathlist[index]
                        _, extension = os.path.splitext(filepath)
                        if extension.lower() == file_extension.lower(): #.jpg and .JPG should be regarded as being the same
                            self.selectedrow = index
                            break
                    except:
                        print("error")
                        pass
            except:
                self.selectedrow = len(self.pathlist)-1
            self.resetimage()
            self.showimagefromindex(self.selectedrow)
    #%% button events  
    def m_menuItemShortcutsOnMenuSelection(self,event):
        pass
    
    def m_bitmapOnLeftDown(self,event):
        self.imagerotation += 90
        self.showimagefromindex(self.selectedrow)
    def m_bitmapOnRightDown(self,event):
        self.imagerotation -= 90
        self.showimagefromindex(self.selectedrow)
        
    def m_btnDownOnButtonClick(self,event):
        self.looknextimageinstance(1)
    def m_btnUpOnButtonClick(self,event):
        self.looknextimageinstance(-1)
        
    def m_choiceOnChoice(self,event):
        self.choiceindex = self.m_choice.GetSelection()
        self.m_buttonOnButtonClick(None)
    
    def btnEditOnButtonClick( self, event ):
        if self.picturepath:        
            #change filename
            self.picturepath = self.pictures.addpicmode(path = self.picturepath,mode='Edit')
            subprocess.Popen([self.edit_exe, self.picturepath], stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.resetimage()
    def m_buttonImDirOnButtonClick( self, event ):
        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        if self.picturepath:        
            path = self.picturepath
            if os.path.isdir(path):
                subprocess.run([FILEBROWSER_PATH, path])
            elif os.path.isfile(path):
                subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
            
            
    def btnPrintQueueOnButtonClick(self,event):
        if self.picturepath:
            self.picturepath = self.pictures.addpicmode(path = self.picturepath,mode='Queue')
            self.updategrid(index = self.selectedrow)
            # reset
            self.resetimage()
            self.showimagefromindex(self.selectedrow)
    def btnPrintQueueBothOnButtonClick(self,event):  
        rowindices,filelist = self.find_JPGRAW_files()
        if filelist:
            for i,imagepath in enumerate(filelist):
                self.picturepath = self.pictures.addpicmode(path = imagepath,mode='Queue')
                self.updategrid(index = rowindices[i])
            # reset
            self.resetimage()
            self.showimagefromindex(self.selectedrow)    
    
    def btnMovePrintsOnButtonClick(self,event):
        modes = self.pictures.getmodes() 
        mode = modes[self.choiceindex]
        #unfinished photos can just be moved around, but those that are in the print queue will have a name change to indicate they are finished
        exportfiles = False
        # open dir where to export it to 
        with wx.DirDialog(self, "Choose which directory to select",style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,defaultPath=self.export_directory) as DirDialog:
            #fileDialog.SetPath(str(self.notesdir)+'\.')
            if DirDialog.ShowModal() == wx.ID_CANCEL:
                pass
                return None    # the user changed their mind
            else:
                self.export_directory = DirDialog.GetPath()
                self.settings_set()
                self.settextctrl()
                self.Update()
                exportfiles = True
        
        if exportfiles and self.pathlist:
            for path in self.pathlist:
                if mode.lower() == 'print queue':
                    newpath = self.pictures.addpicmode(path = path,mode='finished') #printqueue to finished
                else:
                    newpath = path
                if self.m_checkBoxRAW.IsChecked():
                    #export both raw and jpg files
                    shutil.move(newpath,self.export_directory)
                else:
                    #only export nonraw files
                    if IsNotRAW(newpath):
                        shutil.move(newpath,self.export_directory)
        self.resetimage()
    
    def btnCopyPrintsOnButtonClick(self,event):
        
        exportfiles = False
        # open dir where to export it to 
        with wx.DirDialog(self, "Choose which directory to select",style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,defaultPath=self.export_directory) as DirDialog:
            #fileDialog.SetPath(str(self.notesdir)+'\.')
            if DirDialog.ShowModal() == wx.ID_CANCEL:
                pass
                return None    # the user changed their mind
            else:
                exportfiles = True
                self.export_directory = DirDialog.GetPath()
                self.settings_set()
                self.settextctrl()
                self.Update()
                
        if exportfiles and self.pathlist:
            for path in self.pathlist:
                newpath = self.pictures.addpicmode(path = path,mode='finished') #printqueue to finished
                if self.m_checkBoxRAW.IsChecked():
                    #export both raw and jpg files
                    shutil.copy2(newpath,self.export_directory)
                else:
                    #only export nonraw files
                    if IsNotRAW(newpath):
                        shutil.copy2(newpath,self.export_directory)
        self.resetimage()
    

    
    def m_gridOnGridCellLeftClick(self,event):
        
        try:
            index = event.GetRow()
            self.showimagefromindex(index)       
        except:#pressed on the grid when nothing was there
            pass
        

    def m_buttonOnButtonClick(self,parent):
        
        #reset
        NrRows = self.m_grid.GetNumberRows()
        if NrRows:
            self.m_grid.DeleteRows(pos=0, numRows=NrRows, updateLabels=True)
        
        
        self.pathlist = []
        for root, dirs, files in os.walk(self.root_directory, topdown=True):
            for name in files:         
                if not name.startswith('$'): 
                    """ recently deleted items may get a name that starts with $
                    This only occurs when you use os.walk on a directory like "G:\" then it will also walk through the trashbin """
                    path = os.path.join(root, name)
                    filename, file_extension = os.path.splitext(path)
                    if file_extension.lower() in listofextensions:
                        modes = self.pictures.getmodes()                    
                        if self.pictures.checktype(filename=filename,mode=modes[self.choiceindex]):
                            self.pathlist.append(path)
        
        if self.pathlist:
            self.m_grid.AppendRows(len(self.pathlist))
            for i,path in enumerate(self.pathlist):
                filename, file_extension = os.path.splitext(path)
                
                self.m_grid.SetCellValue(i,0,os.path.basename(path))
                self.m_grid.SetCellValue(i,1,file_extension)
                self.m_grid.SetCellValue(i,2,GetShortPath(path))
            
            
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
    def m_buttonDirpickerExeOnButtonClick(self,event):
        if not os.path.exists(self.edit_exe):
            self.edit_exe = r"C:\\"
            
        with wx.FileDialog(self, "Select multiples files to combine", wildcard="*.exe",style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST|wx.FD_MULTIPLE) as fileDialog:
            fileDialog.SetPath(str(self.edit_exe)+'\.')
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                pass
                return None    # the user changed their mind
            else:
                self.edit_exe = fileDialog.GetPath()
                self.settings_set()
                self.settextctrl()
                self.Update()            
                
    def btnDeleteOnButtonClick( self, event ):
        print(f"selected = {self.selectedrow}")
        if isinstance(self.selectedrow,int):            
            path = self.picturepath
            print(f"path to remove is {path}")
            send2trash(path)
            #update lists
            self.updategrid(index = self.selectedrow)
            self.resetimage()
            self.showimagefromindex(self.selectedrow)
            
        

                
    def btnDeleteBothOnButtonClick( self, event ):       
        rowindices,filelist = self.find_JPGRAW_files()
        self.delete_JPGRAW_files(rowindices,filelist)
        #reset
        self.picturepath = None
        self.resetimage()
        self.showimagefromindex(self.selectedrow)
            
        
        
                
    
if __name__ == "__main__":
    # start the application
    app = wx.App(False) 
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
    del app
