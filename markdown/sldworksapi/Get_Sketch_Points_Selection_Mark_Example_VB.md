---
title: "Get Sketch Point's Selection Mark Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Points_Selection_Mark_Example_VB.htm"
---

# Get Sketch Point's Selection Mark Example (VBA)

This example shows how to get the selection mark of a sketch point.

```
'------------------------------------------------
' Preconditions:
' 1. Open a part containing a sketch point.
' 2. Select the sketch containing the sketch point.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the selection mark of the sketch point.
' 2. Examine the Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As Sketch
    Dim sketchPoints As Variant
    Dim swSketchPoint As SldWorks.SketchPoint
    Dim swSelData As SldWorks.SelectData
    Dim status As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = swFeat.GetSpecificFeature2
    sketchPoints = swSketch.GetSketchPoints2
    Set swSketchPoint = sketchPoints(0)
```

```
    ' Get selection mark of sketch point
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    status = swSketchPoint.Select4(True, swSelData)
    Debug.Print "Selection mark of sketch point: " & swSelData.Mark

End Sub
```
