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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 862,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 235, 238, 215 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button = wx.Button( self, wx.ID_ANY, u"Search Pics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial Black" ) )
		
		bSizer1.Add( self.m_button, 0, wx.ALL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Root Directory :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textDir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textDir.SetMinSize( wx.Size( 400,-1 ) )
		
		bSizer6.Add( self.m_textDir, 1, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonDirpicker = wx.Button( self, wx.ID_ANY, u"Pick Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDirpicker.SetFont( wx.Font( 9, 70, 90, 90, False, "Arial" ) )
		
		bSizer6.Add( self.m_buttonDirpicker, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Edit Queue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 18, 74, 90, 92, False, "Arial Black" ) )
		
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Finished List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 18, 74, 90, 92, False, "Arial Black" ) )
		
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid.CreateGrid( 5, 4 )
		self.m_grid.EnableEditing( True )
		self.m_grid.EnableGridLines( False )
		self.m_grid.EnableDragGridSize( False )
		self.m_grid.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid.AutoSizeColumns()
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
		fgSizer2.Add( self.m_grid, 1, wx.ALL, 5 )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 5, 4 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.AutoSizeColumns()
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer2.Add( self.m_grid1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer2, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick )
		self.m_buttonDirpicker.Bind( wx.EVT_BUTTON, self.m_buttonDirpickerOnButtonClick )
		self.m_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.m_gridOnGridCellLeftClick )
		self.m_grid1.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.m_gridOnGridCellLeftClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonDirpickerOnButtonClick( self, event ):
		event.Skip()
	
	def m_gridOnGridCellLeftClick( self, event ):
		event.Skip()
	
	

###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Are you sure you want to delete the image?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		bSizer5.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

