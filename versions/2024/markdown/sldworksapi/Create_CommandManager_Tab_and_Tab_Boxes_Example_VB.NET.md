---
title: "Create CommandManager Tab and Tab Boxes Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_CommandManager_Tab_and_Tab_Boxes_Example_VB.NET.htm"
---

# Create CommandManager Tab and Tab Boxes Example (VB.NET)

This example shows how to create an add-in that creates a CommandManager
tab and tab boxes.

NOTES:

- This sample code is part of a project that was
  built using the VB.NET Add-In Wizard.
- To run this sample code, you need to create a
  complete VB.NET project.
- Your add-in must check to see if the tab already
  exists. If the tab already exists, then you should use that tab instead
  of creating a new tab. If your add-in does not check for an existing tab,
  then SOLIDWORKS will create a new tab each time it starts up.
- Users can add buttons to and remove buttons from
  your CommandManager tab. However, if your add-in removes the CommandManager
  tab upon exiting SOLIDWORKS, then any user customizations will be lost.

'------------------------------------------------------------------------------------------------------------------------------

#### ' SwAddin.vb

Imports System

Imports System.Windows.Forms

Imports System.Collections

Imports System.Reflection

Imports System.Runtime.InteropServices

Imports SolidWorks.Interop.sldworks

Imports SolidWorks.Interop.swconst

Imports SolidWorks.Interop.swpublished

Imports SolidWorksTools

Imports SolidWorksTools.File

<Guid("c5ede50f-7484-416b-9425-ca49f565e48e")>
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}<ComVisible(True)>
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}<SwAddin(
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Description:="test
description", _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Title:="test",
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LoadAtStartup:=True
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}})>
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Class SwAddin

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Implements
SolidWorks.Interop.swpublished.SwAddin

#Region "Local Variables"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
WithEvents iSwApp As SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iCmdMgr As ICommandManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
addinID As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
openDocs As Hashtable

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SwEventPtr As SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ppage As UserPMPage

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Public Properties

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReadOnly
Property SwApp() As SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Return
iSwApp

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Get

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Property

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReadOnly
Property CmdMgr() As ICommandManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Return
iCmdMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Get

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Property

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReadOnly
Property OpenDocumentsTable() As Hashtable

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Get

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Return
openDocs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Get

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Property

#End Region

#Region "SOLIDWORKS Registration"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}<ComRegisterFunction()>
Public Shared Sub RegisterFunction(ByVal t As Type)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get Custom Attribute: SwAddinAttribute

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
attributes() As Object

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SWattr As SwAddinAttribute = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}attributes
= System.Attribute.GetCustomAttributes(GetType(SwAddin), GetType(SwAddinAttribute))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
attributes.Length > 0 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SWattr
= DirectCast(attributes(0), SwAddinAttribute)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString()
+ "}"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
addinkey As Microsoft.Win32.RegistryKey = hklm.CreateSubKey(keyname)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}addinkey.SetValue(Nothing,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}addinkey.SetValue("Description",
SWattr.Description)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}addinkey.SetValue("Title",
SWattr.Title)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}keyname
= "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString()
+ "}"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}addinkey
= hkcu.CreateSubKey(keyname)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}addinkey.SetValue(Nothing,
SWattr.LoadAtStartup,Microsoft.Win32.RegistryValueKind.DWord)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}<ComUnregisterFunction()>
Public Shared Sub UnregisterFunction(ByVal t As Type)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString()
+ "}"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hklm.DeleteSubKey(keyname)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}keyname
= "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString()
+ "}"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}hkcu.DeleteSubKey(keyname)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

#End Region

#Region "ISwAddin Implementation"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Integer) As Boolean
Implements SolidWorks.Interop.swpublished.SwAddin.ConnectToSW

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iSwApp
= ThisSW

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}addinID
= Cookie

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Setup callbacks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iSwApp.SetAddinCallbackInfo(0, Me, addinID)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Setup the Command Manager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iCmdMgr
= iSwApp.GetCommandManager(Cookie)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddCommandMgr()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Setup
the Event Handlers

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SwEventPtr
= iSwApp

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocs
= New Hashtable

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AttachEventHandlers()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Setup
Sample Property Manager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddPMP()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ConnectToSW
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
DisconnectFromSW() As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.DisconnectFromSW

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RemoveCommandMgr()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RemovePMP()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DetachEventHandlers()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iSwApp
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'The
addin _must_ call GC.Collect() here in order to retrieve all managed code
pointers

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GC.Collect()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DisconnectFromSW
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

#End Region

#Region "UI Methods"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub AddCommandMgr()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdGroup As ICommandGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iBmp As New BitmapHandler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
thisAssembly As Assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdIndex0 As Integer, cmdIndex1 As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Title As String = "VB Addin"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ToolTip As String = "VB Addin"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
docTypes() As Integer = {swDocumentTypes_e.swDocASSEMBLY, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDocumentTypes_e.swDocDRAWING,
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDocumentTypes_e.swDocPART}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}thisAssembly
= System.Reflection.Assembly.GetAssembly(Me.GetType())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup
= iCmdMgr.CreateCommandGroup(1,
Title, ToolTip, "", -1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.LargeIconList
= iBmp.CreateFileFromResourceBitmap("test.ToolbarLarge.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.SmallIconList
= iBmp.CreateFileFromResourceBitmap("test.ToolbarSmall.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.LargeMainIcon
= iBmp.CreateFileFromResourceBitmap("test.MainIconLarge.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.SmallMainIcon
= iBmp.CreateFileFromResourceBitmap("test.MainIconSmall.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIndex0
= cmdGroup.AddCommandItem2("CreateCube",
-1, "Create a cube", "Create cube", 0, "CreateCube",
"", 0, 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIndex1
= cmdGroup.AddCommandItem2("Show
PMP", -1, "Display sample property manager", "Show
PMP", 2, "ShowPMP", "PMPEnable", 2, 1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.HasToolbar= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.HasMenu= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.Activate()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each docType As Integer In docTypes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdTab As ICommandTab = iCmdMgr.GetCommandTab(docType,
Title)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bResult As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
cmdTab Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab
= iCmdMgr.AddCommandTab(docType,
Title)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdBox As CommandTabBox = cmdTab.AddCommandTabBox

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdIDs(3) As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
TextType(3) As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIDs(0)
= cmdGroup.CommandID(cmdIndex0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextType(0)
= swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIDs(1)
= cmdGroup.CommandID(cmdIndex1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextType(1)
= swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIDs(2)
= cmdGroup.ToolbarId

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextType(2)
= swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bResult
= cmdBox.AddCommands(cmdIDs, TextType)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Call GetCommands to confirm

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
buttonNumber As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
idObject As Object = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
textTypeObject As Object = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}buttonNumber
= cmdBox.GetCommands(idObject,
textTypeObject)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Added
" + buttonNumber.ToString() + " commands.")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdBox1 As CommandTabBox = cmdTab.AddCommandTabBox()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
cmdIDs(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReDim
TextType(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIDs(0)
= cmdGroup.ToolbarId

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextType(0)
= swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}bResult
= cmdBox1.AddCommands(cmdIDs,
TextType)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.AddSeparator(cmdBox1, cmdGroup.ToolbarId)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}thisAssembly
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iBmp.Dispose()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub RemoveCommandMgr()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iCmdMgr.RemoveCommandGroup(1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
AddPMP() As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ppage
= New UserPMPage

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ppage.Init(iSwApp,
Me)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
RemovePMP() As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ppage
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

#End Region

#Region "Event Methods"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
AttachEventHandlers()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AttachSWEvents()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Listen
for events on all currently open docs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AttachEventsToAllDocuments()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
DetachEventHandlers()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DetachSWEvents()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Close
events on all currently open docs

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
docHandler As DocumentEventHandler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
key As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
numKeys As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}numKeys
= openDocs.Count

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
numKeys > 0 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
keys() As Object = New Object(numKeys - 1) {}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Remove
all document event handlers

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocs.Keys.CopyTo(keys,
0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each key In keys

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler
= openDocs.Item(key)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler.DetachEventHandlers()
'This also removes the pair from the hash

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}key
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
AttachSWEvents()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddHandler
iSwApp.ActiveDocChangeNotify,
AddressOf Me.SldWorks_ActiveDocChangeNotify

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddHandler
iSwApp.DocumentLoadNotify2, AddressOf
Me.SldWorks_DocumentLoadNotify2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddHandler
iSwApp.FileNewNotify2, AddressOf
Me.SldWorks_FileNewNotify2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddHandler
iSwApp.ActiveModelDocChangeNotify,
AddressOf Me.SldWorks_ActiveModelDocChangeNotify

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddHandler
iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
DetachSWEvents()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RemoveHandler
iSwApp.ActiveDocChangeNotify,
AddressOf Me.SldWorks_ActiveDocChangeNotify

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RemoveHandler
iSwApp.DocumentLoadNotify2, AddressOf
Me.SldWorks_DocumentLoadNotify2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RemoveHandler
iSwApp.FileNewNotify2, AddressOf
Me.SldWorks_FileNewNotify2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RemoveHandler
iSwApp.ActiveModelDocChangeNotify,
AddressOf Me.SldWorks_ActiveModelDocChangeNotify

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RemoveHandler
iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
AttachEventsToAllDocuments()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
modDoc As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}modDoc
= iSwApp.GetFirstDocument()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}While
Not modDoc Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not openDocs.Contains(modDoc) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AttachModelDocEventHandler(modDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}modDoc
= modDoc.GetNext()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
While

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
AttachModelDocEventHandler(ByVal modDoc As ModelDoc2) As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
modDoc Is Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Return
False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
docHandler As DocumentEventHandler = Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not openDocs.Contains(modDoc) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Select
Case modDoc.GetType

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
swDocumentTypes_e.swDocPART

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler
= New PartEventHandler()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
swDocumentTypes_e.swDocASSEMBLY

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler
= New AssemblyEventHandler()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Case
swDocumentTypes_e.swDocDRAWING

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler
= New DrawingEventHandler()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Select

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler.Init(iSwApp,
Me, modDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler.AttachEventHandlers()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocs.Add(modDoc,
docHandler)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
DetachModelEventHandler(ByVal modDoc As ModelDoc2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
docHandler As DocumentEventHandler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler
= openDocs.Item(modDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}openDocs.Remove(modDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}modDoc
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}docHandler
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

#End Region

#Region "Event Handlers"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
SldWorks_ActiveDocChangeNotify() As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'TODO:
Add your implementation here

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
SldWorks_DocumentLoadNotify2(ByVal docTitle As String, ByVal docPath As
String) As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
modDoc As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}modDoc
= iSwApp.GetFirstDocument()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}While
Not modDoc Is Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
modDoc.GetTitle= docTitle Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not openDocs.Contains(modDoc) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AttachModelDocEventHandler(modDoc)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}modDoc
= modDoc.GetNext()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
While

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
SldWorks_FileNewNotify2(ByVal newDoc As Object, ByVal doctype As Integer,
ByVal templateName As String) As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AttachEventsToAllDocuments()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
SldWorks_ActiveModelDocChangeNotify() As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'TODO:
Add your implementation here

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
SldWorks_FileOpenPostNotify(ByVal FileName As String) As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AttachEventsToAllDocuments()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

#End Region

#Region "UI Callbacks"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
CreateCube()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'make
sure we have a part open

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
partTemplate As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
model As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
featMan As FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partTemplate
= iSwApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}model
= iSwApp.NewDocument(partTemplate,
swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}model.InsertSketch2(True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}model.SketchRectangle(0, 0, 0, 0.1, 0.1, 0.1,
False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Extrude
the sketch

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featMan
= model.FeatureManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}featMan.FeatureExtrusion(True, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}False,
False, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swEndConditions_e.swEndCondBlind,
swEndConditions_e.swEndCondBlind, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0.1,
0.0, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}False,
False, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}False,
False, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}0.0,
0.0, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}False,
False, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}False,
False, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}True,
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}False,
False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Sub
ShowPMP()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ppage.Show()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Function
PMPEnable() As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
iSwApp.ActiveDocIs Nothing Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PMPEnable
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PMPEnable
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Function

#End Region

End Class
