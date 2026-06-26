---
title: "Undo Deleted Note and Fire Undo Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm"
---

# Undo Deleted Note and Fire Undo Post-Notify Event Example (VB.NET)

## Undo Deleted Note and Fire Undo Pre- and Post-notify Events Example
(VB.NET)

This example demonstrates firing Undo pre- and post-notification events
in a drawing document.

```vb
'---------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\AutoCAD\7550-021.slddrw.
 '
 ' Postconditions:
 ' 1. Selects and deletes the note in Drawing View1.
 ' 2. Undoes the deleted note.
 ' 3. Fires pre-notification event indicating that an undo action is about to
 '    occur and fires post-notification event indicating that an undo
 '    action occurred.
 ' 4. Click OK to close each message box.
 '
 ' NOTE: Because the drawing is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Collections
Imports System.Windows.Forms

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swDrawing As DrawingDoc

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openDrawing As Hashtable

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Event notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDrawing = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openDrawing = New Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventhandlers()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Activate the drawing view that contains
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' the note you want to delete
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swDrawing.ActivateView("Drawing View3")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("DetailItem77@Drawing View3", "NOTE", 0.3058741216774, 0.1870419466786, 0, False, 0, Nothing, 0)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Delete the selected note
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditDelete()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Undo deletion of note
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Pre- and post-notifications fired
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Rebuild the drawing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swDrawing.UndoPostNotify, AddressOf Me.swDrawing_UndoPostNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swDrawing.UndoPreNotify, AddressOf Me.swDrawing_UndoPreNotify
```

```vb
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swDrawing_UndoPostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An undo post-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swDrawing_UndoPreNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An Undo pre-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
