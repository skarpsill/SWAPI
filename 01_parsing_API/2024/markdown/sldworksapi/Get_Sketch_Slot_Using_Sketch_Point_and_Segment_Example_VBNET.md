---
title: "Get Sketch Slot Using Sketch Point and Segment Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Slot_Using_Sketch_Point_and_Segment_Example_VBNET.htm"
---

# Get Sketch Slot Using Sketch Point and Segment Example (VB.NET)

This example shows you how to get a sketch slot using a sketch point
and a sketch segment.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a sketch slot.
' 2. Gets the length of the sketch slot.
' 3. Selects a sketch point on the sketch slot
'    and accesses the sketch slot using that
'    sketch point.
' 4. Gets the length of the sketch slot.
' 5. Selects a sketch segment on the sketch slot
'    and accesses the sketch slot using that
'    sketch segment.
' 6. Gets the length of the sketch slot.
' 7. Examine the Immediate window.
'-------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics
```

```vb
 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swExt As ModelDocExtension
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSketchManager As SketchManager
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSketchSlot As SketchSlot
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSketchPoint As SketchPoint
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSketchSegment As SketchSegment
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swExt = swModel.Extension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select a plane and open a sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.InsertSketch()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Insert a sketch of sketch slotkadov_tag{{<spaces>}}
         swSketchSlot = swSketchManager.CreateSketchSlot(swSketchSlotCreationType_e.swSketchSlotCreationType_line, swSketchSlotLengthType_e.swSketchSlotLengthType_CenterCenter, 0.05, -0.05, 0, 0, 0.05, 0, 0, 0, 0, 0, 1, False)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Length: " & swSketchSlot.Length)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.InsertSketch()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get a sketch point on the sketch slot
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swExt.SelectByID2("Point1@Sketch1", "EXTSKETCHPOINT", 0.05, 0.025, 0, False, 0, Nothing, 0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchPoint = swSelMgr.GetSelectedObject6(1, -1)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get sketch slot
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSlot = swSketchPoint.GetSketchSlot
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Length: " & swSketchSlot.Length)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get a sketch segment on the sketch slot
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -0.03969355327396, -0.025, 0, False, 0, Nothing, 0)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSegment = swSelMgr.GetSelectedObject6(1, -1)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get sketch slot
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchSlot = swSketchSegment.GetSketchSlotkadov_tag{{<spaces>}}
         kadov_tag{{</spaces>}}Debug.Print("Length: " & swSketchSlot.Length)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

 End Class
```
