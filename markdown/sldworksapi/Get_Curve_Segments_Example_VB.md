---
title: "Get Curve Segments Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Curve_Segments_Example_VB.htm"
---

# Get Curve Segments Example (VBA)

This examples shows how to get the curve segments in a reference curve.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Verify that the part document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Selects a face and sketches a spline on that face.
' 3. Selects the sketch of the spline and a face.
' 4. Inserts a projected curve feature and selects it.
' 5. Gets the number of curve segments and the curve segment.
' 6. Examine the Immediate window, FeatureManager design tree, and
'    the graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeature As SldWorks.Feature
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swRefCurve As SldWorks.ReferenceCurve
Dim swCurve As SldWorks.Curve
Dim swEdge As SldWorks.Edge
Dim swSketch As SldWorks.Sketch
Dim swEntity As SldWorks.Entity
Dim pointArray As Variant
Dim points(10) As Double
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()

    Set swApp = Application.SldWorks
```

```
    'Open part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Sketch a spline on the selected face
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("", "FACE", -4.99223104334874E-02, 3.96239999998897E-02, 7.38137362270663E-03, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
    points(0) = -6.24778997860176E-02
    points(1) = 7.29572078180673E-03
    points(2) = 0
    points(3) = -3.64588790258153E-02
    points(4) = 3.24586288177215E-02
    points(5) = 0
    points(6) = 1.04252377344665E-02
    points(7) = 1.40473535914225E-02
    points(8) = 0
    points(9) = 6.46002912861796E-02
    points(10) = 1.00590221094308E-02
    pointArray = points
    Set swSketchSegment = swSketchManager.CreateSpline2((pointArray), False)
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
```

```
    'Insert projected curve
    status = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", -4.97146993259321E-02, 0, -2.56283866693252E-02, True, 0, Nothing, 0)
    Set swFeature = swModel.InsertProjectedSketch2(1)
```

```
    'Select reference curve and get number of reference curve segments
    status = swModelDocExt.SelectByID2("Curve1", "REFCURVE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionManager = swModel.SelectionManager
    Set swFeature = swSelectionManager.GetSelectedObject6(1, -1)
    Set swRefCurve = swFeature.GetSpecificFeature2
    Debug.Print "Number of curve segments: " & swRefCurve.GetSegmentCount
    Set swEdge = swRefCurve.GetFirstSegment
    Debug.Print " Feature = " & swFeature.Name
```

```
    'Select each edge
    Do While Not swEdge Is Nothing
    Set swEntity = swEdge
        status = swEntity.Select4(True, Nothing)
        Debug.Print "    Type of entity (1 = edge): " & swEntity.GetType
        Set swEdge = swRefCurve.GetNextSegment
    Loop

End Sub
```
