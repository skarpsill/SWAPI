---
title: "Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VBNET.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VB.NET)

This example shows how to fire Undo and Redo pre- and post-notifications
in an assembly document.

```vb
'---------------------------------------------------------------------------
' Preconditions: Open  public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
 '
 ' Postconditions:
 ' 1. Selects  and hides the base-plate<1> component and
 '    fires pre- and post-notifications indicating that an
 '    Undo has occurred.
 ' 2. Performs a Redo and fires pre- and post-notifications.
 ' 3. Performs another Undo and fires pre- and post-notifications
 '    so that the assembly document returns to its just-opened state.
 ' 4. Click OK to close each message box.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Collections
Imports System.Windows.Forms
Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public WithEvents swAssemblyDoc As AssemblyDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openAssembly As Hashtable

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Event notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAssemblyDoc = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openAssembly = New Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select a component and hide it
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("base_plate-1@stepped_shaft", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.HideComponent2()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Undo hiding of the component
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' and fire pre- and post notifications
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Redo hiding of the component
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' and fire pre- and post-notifications
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditRedo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Undo hiding of the component
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' so that the assembly document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' is unchanged
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Rebuild model
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssemblyDoc.UndoPostNotify, AddressOf Me.swAssembly_UndoPostNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssemblyDoc.UndoPreNotify, AddressOf Me.swAssembly_UndoPreNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssemblyDoc.RedoPostNotify, AddressOf Me.swAssembly_RedoPostNotify
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssemblyDoc.RedoPreNotify, AddressOf Me.swAssembly_RedoPreNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swAssembly_UndoPostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An Undo post-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swAssembly_UndoPreNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it. kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An Undo pre-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swAssembly_RedoPostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Redo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("A Redo post-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swAssembly_RedoPreNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("A Redo pre-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}

''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
