---
title: "Undo Feature and Fire Undo Post-Notify Event Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm"
---

# Undo Feature and Fire Undo Post-Notify Event Example (VB.NET)

## Undo Feature and Fire Undo Post-Notify Event (VB.NET)

This example shows how to fire an undo post-notification in a part.

```vb
 '-----------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 '
 ' Postconditions:
 ' 1. Creates a cut-extrude feature on the top face of the
 '    candlestick.
 ' 2. Undoes the cut-extrude feature and fires an undo post-notification.
 ' 3. Click OK to close the message box.
 ' 4. Deletes the cut-extrude sketch and all absorbed features.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 '-----------------------------------------------------------------------

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
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeatureManager As FeatureManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeature As Feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim openPart As Hashtable

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set up event notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openPart = New Hashtable
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create a cut-extrude feature on the
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' top face of the candlestick
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.01296, -0.006347, 0.0#)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeatureManager = swModel.FeatureManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeature = swFeatureManager.FeatureCut(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Undo the cut-extrude feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Fire undo notification

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select the circle and delete it
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.DeleteSelection2(swDeleteSelectionOptions_e.swDelete_Absorbed)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AddHandler swPart.UndoPostNotify, AddressOf Me.swPart_UndoPostNotify
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Function swPart_UndoPostNotify() As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Show message after undo action occurs
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' NOTE: Because the message box might be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' behind an open window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If so, then check the Taskbar.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox("An undo post-notification event has been fired.")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
