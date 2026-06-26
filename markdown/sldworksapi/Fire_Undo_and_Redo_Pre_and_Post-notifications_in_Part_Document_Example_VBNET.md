---
title: "Fire Undo and Redo Pre- and Post-notifications in Part Document (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VBNET.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Part Document (VB.NET)

This example shows how to fire undo and redo pre- and post-notifications
in a part document.

```vb
' --------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 '
 ' Postconditions:
 ' 1. Creates a circle, undoes it, redoes it, and undoes it again.
 ' 2. Fires a pre- and post-notification and displays a message box
 '    before and after each Undo and Redo.
 ' 3. Click OK to close each message box.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 ' --------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Collections
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swPart As PartDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchManager As SketchManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchSegment As SketchSegment
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openPart As Hashtable

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set up event notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openPart = New Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create a circle on the
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' top face of the candlestick
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.01296, -0.006347, 0.0#)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Undo creation of circle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' and fire an undo post-notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Redo creation of circle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' and fire a redo post-notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditRedo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Undo creation of circle
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' to leave model document unchanged
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' and fire an Undo post-notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.UndoPostNotify, AddressOf Me.swPart_UndoPostNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.UndoPreNotify, AddressOf Me.swPart_UndoPreNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.RedoPostNotify, AddressOf Me.swPart_RedoPostNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.RedoPostNotify, AddressOf Me.swPart_RedoPreNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Function swPart_UndoPostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box might be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An Undo post-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Function swPart_UndoPreNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box might be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An Undo pre-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Function swPart_RedoPostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box might be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("A Redo post-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Function swPart_RedoPreNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box might be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("A Redo pre-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
