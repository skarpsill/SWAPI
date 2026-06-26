---
title: "Create CommandManager Tab Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_CommandManager_Tab_Example_VB.NET.htm"
---

# Create CommandManager Tab Example (VB.NET)

This example shows how to create a CommandManager command tab.

NOTES:

- This example is only a code snippet. The complete
  project is available in the SOLIDWORKS API SDK.
- Your add-in must check to see if the tab already
  exists. If the tab already exists, then you must use that tab instead
  of creating a new tab. If your add-in does not check for an existing tab,
  then SOLIDWORKS will create a new tab each time it starts up.

...

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdGroup As ICommandGroup

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
iBmp As New BitmapHandler

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
thisAssembly As Assembly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdIndex0 As Integer, cmdIndex1 As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Title As String = "VB Addin"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ToolTip As String = "VB Addin"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
docTypes() As Integer = {swDocumentTypes_e.swDocASSEMBLY, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDocumentTypes_e.swDocDRAWING,
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDocumentTypes_e.swDocPART}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}thisAssembly
= System.Reflection.Assembly.GetAssembly(Me.GetType())

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup
= iCmdMgr.CreateCommandGroup(1,
Title, ToolTip, "", -1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.LargeIconList= iBmp.CreateFileFromResourceBitmap("SwVBAddin3.ToolbarLarge.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.SmallIconList= iBmp.CreateFileFromResourceBitmap("SwVBAddin3.ToolbarSmall.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.LargeMainIcon= iBmp.CreateFileFromResourceBitmap("SwVBAddin3.MainIconLarge.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.SmallMainIcon= iBmp.CreateFileFromResourceBitmap("SwVBAddin3.MainIconSmall.bmp",
thisAssembly)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIndex0
= cmdGroup.AddCommandItem("CreateCube",
-1, "Create a cube", "Create cube", 0, "CreateCube",
"", 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdIndex1
= cmdGroup.AddCommandItem("Show
PMP", -1, "Display sample property manager", "Show
PMP", 2, "ShowPMP", "PMPEnable", 2)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.HasToolbar= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.HasMenu= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdGroup.Activate()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Each docType As Integer In docTypes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdTabs() As Object = iCmdMgr.CommandTabs(docType)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
cmdTab As ICommandTab

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
tabExists As Boolean = False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i As Integer = 0 To iCmdMgr.GetCommandTabCount(docType)
- 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab
= cmdTabs(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
cmdTab.TabName= Title Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}tabExists
= True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
For

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not tabExists Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab
= iCmdMgr.CreateCommandTab(-1,
Title, docType)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.AddCommand(cmdGroup.CommandID(cmdIndex0))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.SetTextDisplay(cmdGroup.CommandID(cmdIndex0),
swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.AddCommand(cmdGroup.CommandID(cmdIndex1))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.SetTextDisplay(cmdGroup.CommandID(cmdIndex1),
swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.AddCommand(cmdGroup.ToolbarId)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.SetTextDisplay(cmdGroup.ToolbarId, swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cmdTab.AddSeparator(cmdGroup.ToolbarId)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}thisAssembly
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}iBmp.Dispose()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

...
