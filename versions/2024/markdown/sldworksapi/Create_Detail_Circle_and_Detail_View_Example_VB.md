---
title: "Create Detail Circle and Detail View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Detail_Circle_and_Detail_View_Example_VB.htm"
---

# Create Detail Circle and Detail View Example (VBA)

This example shows how to create a detail circle and a detail view.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the drawing to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified drawing.
' 2. Activates Drawing View4.
' 3. Creates a detail circle and a detail view using the visible
'    corner of Drawing View4.
' 4. Activates the detail view.
' 5. Gets and sets some properties of the detail circle and detail view.
' 6. Examine the drawing document and Immediate window.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swView As SldWorks.View
Dim swDetailCircle As SldWorks.DetailCircle
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSelData As SldWorks.SelectData
Dim fileName As String
Dim status As Boolean
Dim errors As Long, warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open drawing
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\replaceview.slddrw"
    Set swModel = swApp.OpenDoc6(fileName, swDocDRAWING, swOpenDocOptions_Silent, "", errors, warnings)
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swDrawing = swModel
    swApp.ActivateDoc3 "replaceview - Sheet1", False, swDontRebuildActiveDoc, errors
```

```
    ' Activate Drawing View4 and create detail circle and detail view
    status = swDrawing.ActivateView("Drawing View4")
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateCircle(0.007581, 0.053509, 0#, 0.013533, 0.016475, 0#)
    Set swView = swDrawing.CreateDetailViewAt4(0.22305342706156, 7.62140266484527E-02, 0, swDetViewSTANDARD, 1, 1, "A", swDetCircleCIRCLE, True, True, False, 5)
```

```
    swModel.ClearSelection2 True
```

```
    ' Activate detail view
    status = swDrawing.ActivateView("Drawing View5")
```

```
    ' Get and set some properties of detail circle and detail view
    Set swDetailCircle = swView.GetDetail
    Debug.Print "Detail circle:"
    Debug.Print "  Selected: " & swDetailCircle.Select(True, Nothing)
    Debug.Print "  Label: " & swDetailCircle.GetLabel
    Dim xpos as Double
    Dim ypos as Double
    swDetailCircle.GetLabelPosition xpos, ypos
    Debug.Print "  Label X position: " & xpos
    Debug.Print "  Label Y position: " & ypos
    Debug.Print "  Type of circle: " & swDetailCircle.GetDisplay
    Debug.Print "  Name: " & swDetailCircle.GetName
    Debug.Print "  Style: " & swDetailCircle.GetStyle
    Debug.Print "  Default document text formatting? " & swDetailCircle.GetUseDocTextFormat
    If Not swDetailCircle.NoOutline Then
        Debug.Print "  No outline? False"
        If swDetailCircle.JaggedOutline Then
            swDetailCircle.ShapeIntensity = 2
            Debug.Print "  Jagged outline and shape intensity? True and 2"
        End If
    End If
```

```
End Sub
```
