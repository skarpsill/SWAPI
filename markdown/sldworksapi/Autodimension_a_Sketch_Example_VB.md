---
title: "Autodimension a Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Autodimension_a_Sketch_Example_VB.htm"
---

# Autodimension a Sketch Example (VBA)

This example shows how to autodimension a sketch.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts a sketch of a rectangle.
' 3. Selects two sketch segments in the sketch.
'    * First selected sketch segment is used for horizontal datum.
'    * Second selected sketch segment is used for vertical datum.
' 4. Autodimensions the selected sketch segments.
' 5. Examine the Immediate window and graphics area.
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
    Dim swSketch As SldWorks.Sketch
    Dim swSketchManager As SldWorks.SketchManager
    Dim sketchLines As Variant
    Dim swSketchSegHoriz As SldWorks.SketchSegment
    Dim swSketchSegVert As SldWorks.SketchSegment
    Dim nRetVal As Long
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
```

```
    bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    Set swSketchManager = swModel.SketchManager
    sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 0.110951010058045, -0.066328380491143, 0)
    bRet = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 4.43505736694483E-03, -0.012832795562811, 6.37809258389225E-03, False, 0, Nothing, 0)
    bRet = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0.095835993249203, -3.06185999393385E-02, -2.97695225643872E-02, True, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swSketchSegHoriz = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketchSegVert = swSelMgr.GetSelectedObject6(2, -1)
```

```
    swModel.ClearSelection2 True
```

```
    ' Reselect sketch segments with correct marks
    ' for autodimensioning
    bRet = swSketchSegHoriz.Select3(True, swAutodimMarkHorizontalDatum, Nothing)
    bRet = swSketchSegVert.Select3(True, swAutodimMarkVerticalDatum, Nothing)
```

```
    Set swSketch = swModel.GetActiveSketch2
    nRetVal = swSketch.AutoDimension2(swAutodimEntitiesAll, swAutodimSchemeBaseline, swAutodimHorizontalPlacementBelow, swAutodimSchemeBaseline, swAutodimVerticalPlacementLeft)
```

```
    Debug.Print "Status of autodimensioning sketch (0 = success): " & nRetVal
```

```
    ' Redraw to display dimensions
    swModel.GraphicsRedraw2
```

```
End Sub
```
