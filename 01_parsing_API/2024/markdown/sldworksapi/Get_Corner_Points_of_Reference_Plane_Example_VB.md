---
title: "Get Corner Points of a Reference Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corner_Points_of_Reference_Plane_Example_VB.htm"
---

# Get Corner Points of a Reference Plane Example (VBA)

This example shows how to obtain the four corner points of a reference plane.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the part.
' 2. Creates 3DSketch1 containing four corner points of the reference plane.
' 3. Gets the coordinates of each corner point.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim swFeature As SldWorks.Feature
Dim swRefPlane As SldWorks.RefPlane
Dim swModelExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim vMathPoints As Variant
Dim vArrayData As Variant
Dim pMathPoint As SldWorks.MathPoint
Dim i As Integer
Dim swSketch As SldWorks.Sketch
Dim sketchMgr As SldWorks.SketchManager
Dim sketchPt As SldWorks.SketchPoint
Dim swRefPlaneFeatData As SldWorks.RefPlaneFeatureData
Dim filename As String
Dim errors As swFileLoadError_e
Dim warnings As swFileLoadWarning_e
```

```
Sub main()
    filename = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\swutilities\bracket_a.sldprt"
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6(filename, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    Set sketchMgr = swModel.SketchManager
    boolstatus = swModelExt.SelectByID2("Plane4", "PLANE", 0, 0, 0, False, 0, Nothing, swSelectOptionDefault)
    Set swFeature = swSelMgr.GetSelectedObject5(1)
    Set swRefPlane = swFeature.GetSpecificFeature2
```

```
    vMathPoints = swRefPlane.CornerPoints 'Four (4) MathPoint objects are always returned
    sketchMgr.Insert3DSketch True
    For i = 0 To UBound(vMathPoints)
        vArrayData = vMathPoints(i).ArrayData
        Debug.Print " Point x = " & vArrayData(0)
        Debug.Print " Point y = " & vArrayData(1)
        Debug.Print " Point z = " & vArrayData(2)
        Debug.Print
        Set sketchPt = sketchMgr.CreatePoint(vArrayData(0), vArrayData(1), vArrayData(2))
    Next i
    sketchMgr.Insert3DSketch True
End Sub
```
