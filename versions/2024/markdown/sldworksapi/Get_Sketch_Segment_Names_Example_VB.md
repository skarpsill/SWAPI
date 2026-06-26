---
title: "Get Sketch Segment Names Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Segment_Names_Example_VB.htm"
---

# Get Sketch Segment Names Example (VBA)

This example shows how to get the names of selected sketch segments.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts a sketch of a rectangle.
' 3. Selects two sketch segments and prints their names
'    to the Immediate window.
' 4. Examine the Immediate window.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSketchManager As SldWorks.SketchManager
    Dim sketchLines As Variant
    Dim swSketchSegHoriz As SldWorks.SketchSegment
    Dim swSketchSegVert As SldWorks.SketchSegment
    Dim ret As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    ret = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    ret = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    Set swSketchManager = swModel.SketchManager
    sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 0.110951010058045, -0.066328380491143, 0)
    ret = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 4.43505736694483E-03, -0.012832795562811, 6.37809258389225E-03, False, 0, Nothing, 0)
    ret = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0.095835993249203, -3.06185999393385E-02, -2.97695225643872E-02, True, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swSketchSegHoriz = swSelMgr.GetSelectedObject6(1, -1)
    Debug.Print "Name of selected horizontal sketch segment = " & swSketchSegHoriz.GetName
    Set swSketchSegVert = swSelMgr.GetSelectedObject6(2, -1)
    Debug.Print "Name of selected vertical sketch segment = " & swSketchSegVert.GetName
```

```
    swSketchManager.InsertSketch True
```

```
End Sub
```
