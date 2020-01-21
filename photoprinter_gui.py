# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 862,520 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 235, 238, 215 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button = wx.Button( self, wx.ID_ANY, u"Search Pics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial Black" ) )
		
		bSizer12.Add( self.m_button, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Root Directory :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer12.Add( self.m_staticText2, 0, wx.ALL, 10 )
		
		self.m_textDir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textDir.SetMinSize( wx.Size( 400,-1 ) )
		
		bSizer12.Add( self.m_textDir, 1, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_buttonDirpicker = wx.Button( self, wx.ID_ANY, u"Pick Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buttonDirpicker.SetFont( wx.Font( 9, 70, 90, 90, False, "Arial" ) )
		
		bSizer12.Add( self.m_buttonDirpicker, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_choiceChoices = []
		self.m_choice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceChoices, 0 )
		self.m_choice.SetSelection( 0 )
		bSizer13.Add( self.m_choice, 0, wx.ALL, 5 )
		
		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer13.Add( self.m_choice2, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btnFolder = wx.Button( self, wx.ID_ANY, u"Open Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_btnFolder, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnView = wx.Button( self.m_panel3, wx.ID_ANY, u"View Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnView, 0, wx.ALL, 5 )
		
		self.btnEdit = wx.Button( self.m_panel3, wx.ID_ANY, u"Edit Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnEdit, 0, wx.ALL, 5 )
		
		self.btnDelete = wx.Button( self.m_panel3, wx.ID_ANY, u"Delete Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.btnDelete, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button8 = wx.Button( self.m_panel3, wx.ID_ANY, u"Collect All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button8, 0, wx.ALL, 5 )
		
		
		self.m_panel3.SetSizer( bSizer10 )
		self.m_panel3.Layout()
		bSizer10.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_SIZE, self.MyFrame1OnSize )
		self.m_button.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick )
		self.m_buttonDirpicker.Bind( wx.EVT_BUTTON, self.m_buttonDirpickerOnButtonClick )
		self.m_choice.Bind( wx.EVT_CHOICE, self.m_choiceOnChoice )
		self.m_choice2.Bind( wx.EVT_CHOICE, self.m_choice2OnChoice )
		self.m_btnFolder.Bind( wx.EVT_BUTTON, self.m_btnFolderOnButtonClick )
		self.btnView.Bind( wx.EVT_BUTTON, self.btnViewOnButtonClick )
		self.btnEdit.Bind( wx.EVT_BUTTON, self.btnEditOnButtonClick )
		self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDeleteOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def MyFrame1OnSize( self, event ):
		event.Skip()
	
	def m_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonDirpickerOnButtonClick( self, event ):
		event.Skip()
	
	def m_choiceOnChoice( self, event ):
		event.Skip()
	
	def m_choice2OnChoice( self, event ):
		event.Skip()
	
	def m_btnFolderOnButtonClick( self, event ):
		event.Skip()
	
	def btnViewOnButtonClick( self, event ):
		event.Skip()
	
	def btnEditOnButtonClick( self, event ):
		event.Skip()
	
	def btnDeleteOnButtonClick( self, event ):
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
		
		
		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		bSizer4.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

