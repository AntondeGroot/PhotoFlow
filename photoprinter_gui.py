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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Flashbook", pos = wx.DefaultPosition, size = wx.Size( 971,402 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel0 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel0.SetBackgroundColour( wx.Colour( 254, 240, 231 ) )
		
		bSizer84 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer87 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer87.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText63 = wx.StaticText( self.panel0, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		bSizer87.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		
		bSizer84.Add( bSizer87, 0, wx.EXPAND, 5 )
		
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
		
		
		bSizer84.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceChoices = []
		self.m_choice = wx.Choice( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceChoices, 0 )
		self.m_choice.SetSelection( 0 )
		bSizer91.Add( self.m_choice, 0, wx.ALL, 5 )
		
		
		bSizer84.Add( bSizer91, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer84.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnEdit = wx.Button( self.panel0, wx.ID_ANY, u"Edit Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer92.Add( self.btnEdit, 0, wx.ALL, 5 )
		
		self.m_buttonImDir = wx.Button( self.panel0, wx.ID_ANY, u"Open Image Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer92.Add( self.m_buttonImDir, 0, wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.panel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer92.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.btnPrintQueue = wx.Button( self.panel0, wx.ID_ANY, u"Add to Print Queue", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer92.Add( self.btnPrintQueue, 0, wx.ALL, 5 )
		
		self.btnDelete = wx.Button( self.panel0, wx.ID_ANY, u"Delete Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer92.Add( self.btnDelete, 0, wx.ALL, 5 )
		
		self.btnDeleteBoth = wx.Button( self.panel0, wx.ID_ANY, u"Delete RAW+JPG", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer92.Add( self.btnDeleteBoth, 0, wx.ALL, 5 )
		
		
		bSizer92.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnCollectPrints = wx.Button( self.panel0, wx.ID_ANY, u"Export Print Queue", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer92.Add( self.btnCollectPrints, 0, wx.ALL, 5 )
		
		
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
		
		self.m_bitmap = wx.StaticBitmap( self.m_panelBitmap, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_HELP_BOOK,  ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer28.Add( self.m_bitmap, 0, 0, 10 )
		
		
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
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick )
		self.m_buttonDirpicker.Bind( wx.EVT_BUTTON, self.m_buttonDirpickerOnButtonClick )
		self.m_buttonDirpickerExe.Bind( wx.EVT_BUTTON, self.m_buttonDirpickerExeOnButtonClick )
		self.m_choice.Bind( wx.EVT_CHOICE, self.m_choiceOnChoice )
		self.btnEdit.Bind( wx.EVT_BUTTON, self.btnEditOnButtonClick )
		self.m_buttonImDir.Bind( wx.EVT_BUTTON, self.m_buttonImDirOnButtonClick )
		self.btnPrintQueue.Bind( wx.EVT_BUTTON, self.btnPrintQueueOnButtonClick )
		self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDeleteOnButtonClick )
		self.btnDeleteBoth.Bind( wx.EVT_BUTTON, self.btnDeleteBothOnButtonClick )
		self.btnCollectPrints.Bind( wx.EVT_BUTTON, self.btnCollectPrintsOnButtonClick )
		self.m_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.m_gridOnGridCellLeftClick )
	
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
	
	def btnDeleteOnButtonClick( self, event ):
		event.Skip()
	
	def btnDeleteBothOnButtonClick( self, event ):
		event.Skip()
	
	def btnCollectPrintsOnButtonClick( self, event ):
		event.Skip()
	
	def m_gridOnGridCellLeftClick( self, event ):
		event.Skip()
	

