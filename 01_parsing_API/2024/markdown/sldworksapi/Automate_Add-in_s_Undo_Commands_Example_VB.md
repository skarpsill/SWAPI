---
title: "Automate Add-in's Undo Commands Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Automate_Add-in_s_Undo_Commands_Example_VB.htm"
---

# Automate Add-in's Undo Commands Example (VBA)

This example shows how to automate an add-in's undo commands.

- Module
- Class modules
- [swUndoApiHdlr1](#swUndoApiHdlr1)
- [swUndoApiHdlr2](#swUndoApiHdlr2)

Module
macro1

'----------------------------------------------------

'

' Preconditions: Model document is open.

'

' Postconditions: None

'

'----------------------------------------------------

Option Explicit

Dim swApp As Object

Dim swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

Dim swModExt As SldWorks.ModelDocExtension

Dim Retval As Boolean

Dim name As String

Dim i As Long

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModExt = swModel.Extension()

For i = 1 To 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUndoObj1 As swUndoApiHdlr1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swUndoObj1 = New swUndoApiHdlr1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUndoObj1.a
= i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}name
= "AddinUndo : " & i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Retval
= swModExt.SetApiUndoObject(swUndoObj1,
name)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

Next i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

For i = 1 To 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swUndoObj2 As swUndoApiHdlr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swUndoObj2 = New swUndoApiHdlr2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swUndoObj2.a
= i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}name
= "AddinUndoReset : " & i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Retval
= swModExt.SetApiUndoObject(swUndoObj2,
name)

Next i

End Sub

[Back to top](#Top)

Class moduleswUndoApiHdlr1

Option Explicit

Implements SwUndoAPIHandler

Public a As Long

Private SubSwUndoAPIHandler_DoUndo()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
"Add-in's undo called " & vbCrLf & "Undo object
count : " + Str(a)

End Sub

Private SubSwUndoAPIHandler_UndoReSet()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
("Add-in's undo list reset")

End Sub

[Back to top](#Top)

Class module swUndoApiHdlr2

Option Explicit

Implements SwUndoAPIHandler

Public a As Long

Private SubSwUndoAPIHandler_DoUndo()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
"Undo called " & vbCrLf & "Undo count : "
+ Str(a)

End Sub

Private SubSwUndoAPIHandler_UndoReSet()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MsgBox
("Undo reset called ")

End Sub

[Back to top](#Top)
