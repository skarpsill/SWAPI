---
title: "Get Sketch Point's View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Point_s_View_Example_VB.htm"
---

# Get Sketch Point's View Example (VBA)

This example shows how to get the name of the drawing view for the selected sketch point.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a drawing in which a sketch point
'    exists in a drawing view.
' 2. Select the sketch point.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the sketch point feature
'    and the name of the drawing view in which
'    the sketch point exists.
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
    Dim swSkPt As SldWorks.SketchPoint
    Dim swSketch As SldWorks.Sketch
    Dim swSketchFeat As SldWorks.Feature
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    Dim swViewSketch As SldWorks.Sketch
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swSkPt = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swSkPt.GetSketch
    Set swSketchFeat = swSketch
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swSketchFeat.Name
```

```
    Set swView = swDraw.GetFirstView
    Do While Not Nothing Is swView
        Set swViewSketch = swView.GetSketch
        If swSketch Is swViewSketch Then
            Debug.Print "    -- > " & swView.Name
            Exit Do
        End If
        Set swView = swView.GetNextView
    Loop
```

```
End Sub
```
