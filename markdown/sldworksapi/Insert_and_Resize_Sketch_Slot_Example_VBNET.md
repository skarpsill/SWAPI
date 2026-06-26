---
title: "Insert and Resize Sketch Slot Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Resize_Sketch_Slot_Example_VBNET.htm"
---

# Insert and Resize Sketch Slot Example (VB.NET)

This example shows how to insert a sketch slot and resize it.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Open the Immediate window..
'
' Postconditions:
' 1. Creates a sketch and inserts a sketch slot.
' 2. Press F5 after examining the graphics area.
' 3. Resizes the slot.
' 4. Examine the graphics area and Immediate window.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swExt As ModelDocExtension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swPart As PartDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim skManager As SketchManager

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
```

```vb
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swExt = swModel.Extension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}skManager = swModel.SketchManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}skManager.InsertSketch(True)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchSlot As SketchSlot
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSlot = skManager.CreateSketchSlot(swSketchSlotCreationType_e.swSketchSlotCreationType_line, swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter, 0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, False)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim lengthType As swSketchSlotLengthType_e
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}lengthType = swSketchSlot.LengthType

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Length: " & swSketchSlot.Length)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Length Type: " & lengthType.ToString())
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Width: " & swSketchSlot.Width)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Stop

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Edit the original slot
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSlot.Width = swSketchSlot.Width * 2.0#
         Debug.Print "Modified width: " & swSketchSlot.Width
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}skManager.InsertSketch(True)

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
 End Class
```
