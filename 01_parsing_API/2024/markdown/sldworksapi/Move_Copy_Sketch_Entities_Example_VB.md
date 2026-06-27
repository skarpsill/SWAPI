---
title: "Move Copy Sketch Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Copy_Sketch_Entities_Example_VB.htm"
---

# Move Copy Sketch Entities Example (VBA)

This example shows how to move, copy, and move and copy sketch entities.

```
'----------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Step through the macro by pressing F8.
'     1.  Opens a new part document.
'     2.  Opens a sketch and sketches a line and a circle.
'     3.  Examine the sketch.
'     4.  Selects the line and circle.
'     5.  Moves the line and circle.
'     6.  Examine the sketch.
'     7.  Moves and copies the line and circle once.
'     8.  Examine the sketch.
'     9.  Moves and copies the line and circle twice.
'    10. Examine the sketch.
' 2. Close the part document without saving it.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp              As SldWorks.SldWorks
Dim swModel            As SldWorks.ModelDoc2
Dim swModelDocExt      As SldWorks.ModelDocExtension
Dim swPart             As SldWorks.PartDoc
Dim swFeature          As SldWorks.Feature
Dim swSketchMgr        As SldWorks.SketchManager
Dim swSketchSegment    As SldWorks.SketchSegment
Dim lIdx               As Long
Dim bCopy              As Boolean
Dim lNumCopies         As Long
Dim aBasePoint(2)      As Double
Dim aMoveVector(2)     As Double
Dim errors             As Long
Dim status             As Boolean
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open a new part document and sketch a line and a circle
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    swApp.ActivateDoc3 "Part1", True, False, errors
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch True
    Set swSketchSegment = swSketchMgr.CreateLine(-0.096389, 0.032667, 0#, -0.062943, 0.019437, 0#)
    Set swSketchSegment = swSketchMgr.CreateCircle(-0.084504, 0.013823, 0#, -0.087932, 0.006083, 0#)
```

```
    Set swFeature = swPart.FeatureByName("Sketch1")
    status = swFeature.Select2(False, 0)
    swModel.EditSketch
```

```
    aBasePoint(0) = 0#
    aBasePoint(1) = 0#
    aBasePoint(2) = 0#
```

```
    aMoveVector(0) = 0.1
    aMoveVector(1) = 0#
    aMoveVector(2) = 0#
```

```
    For lIdx = 0 To 2
        swModel.ClearSelection2 True
        status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -7.52087432116777E-02, 3.68667656031986E-02, 1.46398923143701E-02, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", -8.02420935887737E-02, 3.33695230163339E-02, 0.019671897706856, True, 0, Nothing, 0)
```

```
        Select Case (lIdx)
            Case 0
            ' Move
                bCopy = False
                lNumCopies = 0
            Case 1
            ' Move and copy once
                bCopy = True
                lNumCopies = 1
            Case 2
            ' Move and copy twice
                bCopy = True
                lNumCopies = 2
        End Select
```

```
        If (Not bCopy) Then
            lNumCopies = 0
        End If
```

```
        swModelDocExt.MoveOrCopy bCopy, lNumCopies, True, aBasePoint(0), aBasePoint(1), 0#, aBasePoint(0) + aMoveVector(0), aBasePoint(1) + aMoveVector(1), aBasePoint(2) + aMoveVector(2)
        swModel.ClearSelection2 True
```

```
        ' Undo so that you can do it again, but differently
        swModel.EditUndo2 1
```

```
    Next lIdx
```

```
    swSketchMgr.InsertSketch True
```

```
End Sub
```
