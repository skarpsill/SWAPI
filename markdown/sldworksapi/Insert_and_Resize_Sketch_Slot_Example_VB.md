---
title: "Insert and Resize Sketch Slot Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Resize_Sketch_Slot_Example_VB.htm"
---

# Insert and Resize Sketch Slot Example (VBA)

This example shows how to insert and resize a sketch slot.

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
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As ModelDoc2
    Dim swExt As ModelDocExtension
    Dim swSelMgr As SelectionMgr
    Dim boolstatus As Boolean
    Dim swPart As PartDoc
    Dim skManager As SketchManager
```

```
    Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set skManager = swModel.SketchManager
    Set swPart = swModel
```

```
    boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
```

```
    skManager.InsertSketch (True)
    Dim swSketchSlot As SketchSlot
    ' Insert a sketch slot
    Set swSketchSlot = skManager.CreateSketchSlot(swSketchSlotCreationType_e.swSketchSlotCreationType_line, swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter, 0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, False)
    Dim lengthType As swSketchSlotLengthType_e
    lengthType = swSketchSlot.lengthType
    Debug.Print "Length: " & swSketchSlot.Length
    Debug.Print "Length Type: " & lengthType
    Debug.Print "Width: " & swSketchSlot.Width
```

```
    Stop
```

```
    ' Edit the slot
    swSketchSlot.Width = swSketchSlot.Width * 2#
    Debug.Print "Modified width: " & swSketchSlot.Width
    skManager.InsertSketch (True)
```

```
End Sub
```
