---
title: "Undo Hidden Component and Fire Undo Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm"
---

# Undo Hidden Component and Fire Undo Post-Notify Event Example (VB.NET)

This example shows how to fire an undo post-notification in
an assembly document.

```vb
'--------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
 '
 ' Postconditions:
 ' 1. Selects and hides the base-plate<1> component.
 ' 2. Undoes the hiding of the base-plate<1> component.
 ' 3. Fires a post-notification indicating that an undo action occurred.
 ' 4. Click OK to close the message box.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '--------------------------------------------------------------------------
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
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Fire undo post-notification

kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}' Rebuild the model
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swAssemblyDoc.UndoPostNotify, AddressOf Me.swAssembly_UndoPostNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Function swAssembly_UndoPostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Display message after undo event occurs
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An undo post-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
