# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Flashbook", pos = wx.DefaultPosition, size = wx.Size( 1474,402 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel0 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel0.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 71, 90, 90, False, wx.EmptyString ) )
		self.panel0.SetBackgroundColour( wx.Colour( 254, 240, 231 ) )
		
		bSizer84 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer87 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer87.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText63 = wx.StaticText( self.panel0, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		bSizer87.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		
		bSizer84.Add( bSizer87, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button = wx.Button( self.panel0, wx.ID_ANY, u"Search Photos", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button, 0, wx.ALL, 5 )
		
		self.m_staticText66 = wx.StaticText( self.panel0, wx.ID_ANY, u"Root Directory :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		fgSizer1.Add( self.m_staticText66, 0, wx.ALL, 5 )
		
		self.m_textDir = wx.TextCtrl( self.panel0, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		fgSizer1.Add( self.m_textDir, 0, wx.ALL, 5 )
		
		self.m_buttonDirpicker = wx.Button( self.panel0, wx.ID_ANY, u"Pick Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_buttonDirpicker, 0, wx.ALL, 5 )
		
		self.m_emptytext = wx.StaticText( self.panel0, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_emptytext.Wrap( -1 )
		fgSizer1.Add( self.m_emptytext, 0, wx.ALL, 5 )
		
		self.m_staticText661 = wx.StaticText( self.panel0, wx.ID_ANY, u"Executable path:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText661.Wrap( -1 )
		fgSizer1.Add( self.m_staticText661, 0, wx.ALL, 5 )
		
		self.m_textDirExe = wx.TextCtrl( self.panel0, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		fgSizer1.Add( self.m_textDirExe, 0, wx.ALL, 5 )
		
		self.m_buttonDirpickerExe = wx.Button( self.panel0, wx.ID_ANY, u"Pick Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_buttonDirpickerExe, 0, wx.ALL, 5 )
		
		
		bSizer24.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		
		bSizer84.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceChoices = []
		self.m_choice = wx.Choice( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceChoices, 0 )
		self.m_choice.SetSelection( 0 )
		bSizer91.Add( self.m_choice, 0, wx.ALL, 5 )
		
		
		bSizer84.Add( bSizer91, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer84.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticline32 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline32, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self.panel0, wx.ID_ANY, u"Editing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer17.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer16.Add( bSizer17, 0, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnEdit = wx.Button( self.panel0, wx.ID_ANY, u"Edit Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.btnEdit, 0, wx.ALL, 5 )
		
		self.m_buttonImDir = wx.Button( self.panel0, wx.ID_ANY, u"Open Image Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_buttonImDir, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer18, 0, wx.EXPAND, 5 )
		
		
		bSizer92.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText5 = wx.StaticText( self.panel0, wx.ID_ANY, u"Add to Print Queue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer12.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		
		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer12, 0, wx.EXPAND, 0 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnPrintQueue = wx.Button( self.panel0, wx.ID_ANY, u"This Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnPrintQueue, 0, wx.ALL, 5 )
		
		self.btnPrintQueueBoth = wx.Button( self.panel0, wx.ID_ANY, u"RAW+JPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnPrintQueueBoth, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		
		bSizer92.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self.panel0, wx.ID_ANY, u"Delete Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer14.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnDelete = wx.Button( self.panel0, wx.ID_ANY, u"This Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btnDelete, 0, wx.ALL, 5 )
		
		self.btnDeleteBoth = wx.Button( self.panel0, wx.ID_ANY, u"RAW+JPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btnDeleteBoth, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		
		bSizer92.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		self.m_staticline311 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline311, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self.panel0, wx.ID_ANY, u"Image size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer241.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_txtImageSize = wx.TextCtrl( self.panel0, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), wx.TE_READONLY )
		bSizer241.Add( self.m_txtImageSize, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer241, 1, wx.EXPAND, 5 )
		
		bSizer261 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText17 = wx.StaticText( self.panel0, wx.ID_ANY, u"Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer261.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_txtImageDate = wx.TextCtrl( self.panel0, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer261.Add( self.m_txtImageDate, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer261, 1, wx.EXPAND, 5 )
		
		
		bSizer92.Add( bSizer25, 0, wx.EXPAND, 5 )
		
		self.m_staticline3113 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline3113, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer251 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText151 = wx.StaticText( self.panel0, wx.ID_ANY, u"RAW images", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		bSizer2411.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer2411, 1, wx.EXPAND, 5 )
		
		bSizer2611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_radioBtnBW = wx.RadioButton( self.panel0, wx.ID_ANY, u"Quickload (BW)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2611.Add( self.m_radioBtnBW, 0, wx.ALL, 5 )
		
		self.m_radioBtnColor = wx.RadioButton( self.panel0, wx.ID_ANY, u"Slow (color)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtnColor.SetValue( True ) 
		bSizer2611.Add( self.m_radioBtnColor, 0, wx.ALL, 5 )
		
		
		bSizer251.Add( bSizer2611, 1, wx.EXPAND, 5 )
		
		
		bSizer92.Add( bSizer251, 0, wx.EXPAND, 5 )
		
		self.m_staticline3112 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline3112, 0, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer92.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_btnDown = wx.Button( self.panel0, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 0,0 ), 0 )
		bSizer92.Add( self.m_btnDown, 0, wx.ALL, 5 )
		
		self.m_btnUp = wx.Button( self.panel0, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 0,0 ), 0 )
		bSizer92.Add( self.m_btnUp, 0, wx.ALL, 5 )
		
		self.m_staticline3111 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline3111, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self.panel0, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer20.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_checkBoxRAW = wx.CheckBox( self.panel0, wx.ID_ANY, u"RAW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxRAW.SetValue(True) 
		bSizer20.Add( self.m_checkBoxRAW, 0, wx.ALL, 5 )
		
		
		bSizer20.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer20, 0, wx.EXPAND, 0 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnMovePrints = wx.Button( self.panel0, wx.ID_ANY, u"Move files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.btnMovePrints, 0, wx.ALL, 5 )
		
		self.btnCopyPrints = wx.Button( self.panel0, wx.ID_ANY, u"Duplicate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.btnCopyPrints, 0, wx.ALL, 5 )
		
		
		bSizer21.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer21, 0, wx.EXPAND, 5 )
		
		
		bSizer92.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		self.m_staticline33 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline33, 0, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer84.Add( bSizer92, 0, wx.EXPAND, 5 )
		
		self.m_staticline7 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer84.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 0 )
		
		
		self.panel0.SetSizer( bSizer84 )
		self.panel0.Layout()
		bSizer84.Fit( self.panel0 )
		bSizer7.Add( self.panel0, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel3.SetBackgroundColour( wx.Colour( 254, 240, 231 ) )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel31 = wx.Panel( self.panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel31.SetFont( wx.Font( 9, 74, 90, 90, False, "Verdana" ) )
		self.m_panel31.SetBackgroundColour( wx.Colour( 254, 240, 231 ) )
		self.m_panel31.SetMaxSize( wx.Size( 500,-1 ) )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer30.Add( ( 25, 0), 1, wx.EXPAND, 5 )
		
		self.m_grid = wx.grid.Grid( self.m_panel31, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid.CreateGrid( 1, 3 )
		self.m_grid.EnableEditing( True )
		self.m_grid.EnableGridLines( True )
		self.m_grid.EnableDragGridSize( False )
		self.m_grid.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid.EnableDragColMove( False )
		self.m_grid.EnableDragColSize( True )
		self.m_grid.SetColLabelSize( 30 )
		self.m_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid.EnableDragRowSize( True )
		self.m_grid.SetRowLabelSize( 80 )
		self.m_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer30.Add( self.m_grid, 0, 0, 5 )
		
		
		bSizer30.Add( ( 25, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panel31.SetSizer( bSizer30 )
		self.m_panel31.Layout()
		bSizer30.Fit( self.m_panel31 )
		bSizer26.Add( self.m_panel31, 0, wx.EXPAND|wx.TOP, 0 )
		
		self.m_panelBitmap = wx.Panel( self.panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelBitmap.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_panelBitmap.SetBackgroundColour( wx.Colour( 254, 240, 231 ) )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap = wx.StaticBitmap( self.m_panelBitmap, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_bitmap, 0, wx.ALL, 5 )
		
		
		self.m_panelBitmap.SetSizer( bSizer28 )
		self.m_panelBitmap.Layout()
		bSizer28.Fit( self.m_panelBitmap )
		bSizer26.Add( self.m_panelBitmap, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 0 )
		
		
		self.panel3.SetSizer( bSizer26 )
		self.panel3.Layout()
		bSizer26.Fit( self.panel3 )
		bSizer7.Add( self.panel3, 1, wx.EXPAND |wx.ALL, 0 )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer7.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menuHelp = wx.Menu()
		self.m_menuItemShortcuts = wx.MenuItem( self.m_menuHelp, wx.ID_ANY, u"Shortcuts", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuHelp.AppendItem( self.m_menuItemShortcuts )
		
		self.m_menubar1.Append( self.m_menuHelp, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick )
		self.m_buttonDirpicker.Bind( wx.EVT_BUTTON, self.m_buttonDirpickerOnButtonClick )
		self.m_buttonDirpickerExe.Bind( wx.EVT_BUTTON, self.m_buttonDirpickerExeOnButtonClick )
		self.m_choice.Bind( wx.EVT_CHOICE, self.m_choiceOnChoice )
		self.btnEdit.Bind( wx.EVT_BUTTON, self.btnEditOnButtonClick )
		self.m_buttonImDir.Bind( wx.EVT_BUTTON, self.m_buttonImDirOnButtonClick )
		self.btnPrintQueue.Bind( wx.EVT_BUTTON, self.btnPrintQueueOnButtonClick )
		self.btnPrintQueueBoth.Bind( wx.EVT_BUTTON, self.btnPrintQueueBothOnButtonClick )
		self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDeleteOnButtonClick )
		self.btnDeleteBoth.Bind( wx.EVT_BUTTON, self.btnDeleteBothOnButtonClick )
		self.m_btnDown.Bind( wx.EVT_BUTTON, self.m_btnDownOnButtonClick )
		self.m_btnUp.Bind( wx.EVT_BUTTON, self.m_btnUpOnButtonClick )
		self.btnMovePrints.Bind( wx.EVT_BUTTON, self.btnMovePrintsOnButtonClick )
		self.btnCopyPrints.Bind( wx.EVT_BUTTON, self.btnCopyPrintsOnButtonClick )
		self.m_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.m_gridOnGridCellLeftClick )
		self.m_bitmap.Bind( wx.EVT_LEFT_DOWN, self.m_bitmapOnLeftDown )
		self.m_bitmap.Bind( wx.EVT_RIGHT_DOWN, self.m_bitmapOnRightDown )
		self.Bind( wx.EVT_MENU, self.m_menuItemShortcutsOnMenuSelection, id = self.m_menuItemShortcuts.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonDirpickerOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonDirpickerExeOnButtonClick( self, event ):
		event.Skip()
	
	def m_choiceOnChoice( self, event ):
		event.Skip()
	
	def btnEditOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonImDirOnButtonClick( self, event ):
		event.Skip()
	
	def btnPrintQueueOnButtonClick( self, event ):
		event.Skip()
	
	def btnPrintQueueBothOnButtonClick( self, event ):
		event.Skip()
	
	def btnDeleteOnButtonClick( self, event ):
		event.Skip()
	
	def btnDeleteBothOnButtonClick( self, event ):
		event.Skip()
	
	def m_btnDownOnButtonClick( self, event ):
		event.Skip()
	
	def m_btnUpOnButtonClick( self, event ):
		event.Skip()
	
	def btnMovePrintsOnButtonClick( self, event ):
		event.Skip()
	
	def btnCopyPrintsOnButtonClick( self, event ):
		event.Skip()
	
	def m_gridOnGridCellLeftClick( self, event ):
		event.Skip()
	
	def m_bitmapOnLeftDown( self, event ):
		event.Skip()
	
	def m_bitmapOnRightDown( self, event ):
		event.Skip()
	
	def m_menuItemShortcutsOnMenuSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, u"Short cuts" ), wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Delete RAW+JPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Add RAW+JPG \nto print queue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Add This image\nto print queue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer2.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Spacebar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( sbSizer1 )
		self.m_panel5.Layout()
		sbSizer1.Fit( self.m_panel5 )
		bSizer25.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		bSizer25.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

