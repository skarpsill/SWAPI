---
title: "Insert Free Point Curve Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Free_Point_Curve_Feature_Example_VB.htm"
---

# Insert Free Point Curve Feature Example (VBA)

This example shows how to insert a free point curve feature.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Create c:\temp, if this folder does not exist.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part document.
' 2. Inserts a free point curve feature.
' 3. Gets some free point curve feature data.
' 4. Saves the free point curve feature's points to a file.
' 5. Examine the graphics area, FeatureManager design tree,
'    Immediate window, and c:\temp.
'---------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swFreePointCurveFeatureData As SldWorks.FreePointCurveFeatureData
Dim status As Boolean
Dim nbrPoints As Long
Dim pointArray As Variant
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create new part document
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
```

```
    'Insert free point curve feature
    swModel.InsertCurveFileBegin
    status = swModel.InsertCurveFilePoint(0, 0, 0)
    status = swModel.InsertCurveFilePoint(0, 0, 0.0127)
    status = swModel.InsertCurveFilePoint(0, 0, 0.0254)
    status = swModel.InsertCurveFilePoint(0, 0, 0.0381)
    status = swModel.InsertCurveFilePoint(0, 0.0254, 0.0381)
    status = swModel.InsertCurveFilePoint(0, 0.0381, 0.0381)
    status = swModel.InsertCurveFileEnd()
```

```
    'Get free point curve feature
    Set swModelDocExt = swModel.Extension
    Set swSelectionMgr = swModel.SelectionManager
    status = swModelDocExt.SelectByID2("Curve1", "REFERENCECURVES", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    'Get number of points in free point curve feature
    Set swFreePointCurveFeatureData = swFeature.GetDefinition
    nbrPoints = swFreePointCurveFeatureData.GetPointCount
    Debug.Print ("Number of points in free point curve feature: " & nbrPoints)
    'Get the points in free point curve feature
    pointArray = swFreePointCurveFeatureData.pointArray
    Debug.Print "Points in free point curve feature: "
    For i = 0 To nbrPoints - 1
        Debug.Print "  " & pointArray(i)
    Next i
    'Save the points in free point curve feature to file
    status = swFreePointCurveFeatureData.SavePointsToFile("c:\temp\MyFreePointCurveFeature.sldcrv")
    Debug.Print "Curve file created in specified folder: " & status
```

```
End Sub
```
